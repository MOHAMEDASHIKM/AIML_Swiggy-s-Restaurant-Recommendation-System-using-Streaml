# import streamlit as st
# import pandas as pd
# import joblib

# st.set_page_config(page_title="Swiggy Restaurant Recommender", layout="wide")

# # ==============================
# # LOAD DATA
# # ==============================
# @st.cache_resource
# def load_all_data():
#     clean_df = pd.read_csv("data/processed/cleaned_data.csv")
#     encoded_df = pd.read_csv("data/processed/encoded_data.csv")
#     kmeans = joblib.load("models/kmeans_model.pkl")
#     return clean_df, encoded_df, kmeans


# clean_df, encoded_df, kmeans = load_all_data()

# # ==============================
# # DEBUG (Shows actual columns)
# # ==============================
# st.write("Available Columns in Dataset:")
# st.write(clean_df.columns.tolist())

# # ==============================
# # UI
# # ==============================
# st.title("🍽️ Swiggy Restaurant Recommendation System")

# # Safe city column detection
# if "city" not in clean_df.columns:
#     st.error("❌ 'city' column not found in dataset.")
#     st.stop()

# city_options = ["-- Select City --"] + sorted(
#     clean_df["city"].dropna().unique().tolist()
# )

# selected_city = st.selectbox("Select City", city_options)

# if selected_city != "-- Select City --":

#     filtered_df = clean_df[clean_df["city"] == selected_city]

#     st.subheader(f"Restaurants in {selected_city}")

#     # Show all available columns safely
#     st.dataframe(filtered_df)

# else:
#     st.info("Please select a city to see restaurants.")




# =============codde 2=======================================================================================================





import streamlit as st
import pandas as pd
import joblib
import pickle

st.set_page_config(page_title="Swiggy Restaurant Recommender", layout="wide")

# ==============================
# LOAD DATA
# ==============================
@st.cache_resource
def load_all():
    clean_df = pd.read_csv("data/processed/cleaned_data.csv")
    kmeans = joblib.load("models/kmeans_model.pkl")
    city_enc = pickle.load(open("data/processed/city_encoder.pkl", "rb"))
    cuisine_list = pickle.load(open("data/processed/cuisine_list.pkl", "rb"))
    return clean_df, kmeans, city_enc, cuisine_list

clean_df, kmeans, city_enc, cuisine_list = load_all()

# ==============================
# TITLE
# ==============================
st.title("🍽️ Swiggy Restaurant Recommendation System")
st.markdown("### Find the best restaurants for your cravings!")

# ==============================
# SIDEBAR FILTERS
# ==============================
st.sidebar.header("🔎 Filter Options")

city = st.sidebar.selectbox(
    "Select City",
    sorted(clean_df["city"].unique())
)

cuisine = st.sidebar.selectbox(
    "Select Cuisine",
    sorted(cuisine_list)
)

min_rating = st.sidebar.slider("Minimum Rating", 1.0, 5.0, 3.5)
max_cost = st.sidebar.slider("Maximum Cost", 100, 5000, 600)

# ==============================
# RECOMMEND FUNCTION
# ==============================
def recommend(city, cuisine, min_rating, max_cost, top_n=10):

    city_vec = city_enc.transform([[city]])[0]
    cuisine_vec = [1 if c == cuisine.lower() else 0 for c in cuisine_list]

    user_vector = list(city_vec) + cuisine_vec + [min_rating, 10, max_cost]

    cluster_id = kmeans.predict([user_vector])[0]

    cluster_data = clean_df.copy()

    results = cluster_data[
        (cluster_data["city"] == city) &
        (cluster_data["cuisine"].str.contains(cuisine, case=False)) &
        (cluster_data["rating"] >= min_rating) &
        (cluster_data["cost"] <= max_cost)
    ]

    return results.head(top_n)

# ==============================
# SHOW RESULTS AS CARDS
# ==============================
if st.button("🍴 Get Recommendations"):

    results = recommend(city, cuisine, min_rating, max_cost)

    if results.empty:
        st.warning("No restaurants found. Try changing filters.")
    else:
        st.success(f"Found {len(results)} restaurants!")

        cols = st.columns(3)

        for idx, row in results.iterrows():
            with cols[idx % 3]:
                st.markdown(
                    f"""
                    <div style="
                        border:1px solid #ddd;
                        padding:25px;
                        border-radius:12px;
                        margin-bottom:20px;
                        transition: 3.3s;
                        box-shadow:10px 6px 10px rgba(0,0,0,0.1);
                    ">
                        <h4>🍽️ {row['name']}</h4>
                        <p><b>City:</b> {row['city']}</p>
                        <p><b>Cuisine:</b> {row['cuisine']}</p>
                        <p>⭐ <b>Rating:</b> {row['rating']}</p>
                        <p>💰 <b>Cost:</b> ₹{row['cost']}</p>
                        <a href="{row['link']}" target="_blank" class="order-btn">
                            🛒 Order on Swiggy
                        </a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )




