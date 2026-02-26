# 🍽️ Swiggy Restaurant Recommendation System

A Machine Learning based Restaurant Recommendation Web App built using **Python, Streamlit, and KMeans Clustering**.

This project recommends restaurants based on:
- 📍 City
- 🍴 Cuisine
- ⭐ Minimum Rating
- 💰 Maximum Cost

It displays restaurants in a modern **card-style UI** with:
- Food images
- Restaurant details
- Swiggy order link button

---

## 🚀 Live Features

✅ Restaurant recommendations using KMeans  
✅ Beautiful Swiggy-style card UI  
✅ Image preview inside cards  
✅ Clickable "Order on Swiggy" button  
✅ Rating & cost filtering  
✅ Sidebar filtering system  

---

## 🛠️ Tech Stack

- Python 3.10
- Pandas
- Scikit-Learn (MiniBatchKMeans)
- Streamlit
- Joblib
- Pickle

---

## 📂 Project Structure

```
Swiggy-Restaurant-Recommendation-System/
│
├── app.py
├── preprocess.py
├── train_kmeans.py
│
├── data/
│   ├── raw/
│   │   └── swiggy.csv
│   └── processed/
│       ├── cleaned_data.csv
│       ├── encoded_data.csv
│       ├── city_encoder.pkl
│       └── cuisine_list.pkl
│
├── models/
│   └── kmeans_model.pkl
│
└── README.md
```

---

## 📊 Dataset Columns

| Column | Description |
|--------|------------|
| name | Restaurant name |
| city | City name |
| cuisine | Type of cuisine |
| rating | Restaurant rating |
| rating_count | Number of reviews |
| cost | Approx cost for two |
| address | Restaurant location |
| link | Swiggy order link |
| image | Restaurant food image |

---

## ⚙️ Installation & Setup (Run in VS Code)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Swiggy-Restaurant-Recommendation-System.git
cd Swiggy-Restaurant-Recommendation-System
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

If requirements.txt not available:

```bash
pip install streamlit pandas scikit-learn joblib
```

---

### 4️⃣ Run Preprocessing

```bash
python preprocess.py
```

---

### 5️⃣ Train KMeans Model

```bash
python train_kmeans.py
```

---

### 6️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 🎯 How It Works

1. Data is cleaned and encoded
2. Cities and cuisines are transformed into numerical features
3. KMeans clustering groups similar restaurants
4. User input is converted into feature vector
5. Model predicts cluster
6. Filtered results are shown as interactive cards

---

## 🖼️ UI Preview

- Swiggy style design
- 3-column responsive layout
- Hover animation
- Image + restaurant details
- Direct Swiggy order button

---

## 🔥 Future Improvements

- ⭐ Real star rating UI
- ❤️ Add to Cart functionality
- 📊 Admin dashboard with analytics
- 🌐 Deploy on Streamlit Cloud
- 🤖 Add Content-Based Recommendation
- 📱 Mobile responsive UI

---

## 👨‍💻 Author

**Mohamed Ashik**

Aspiring Data Scientist & Machine Learning Developer  
India 🇮🇳  

---

## ⭐ If You Like This Project

Give this repo a ⭐ on GitHub!
