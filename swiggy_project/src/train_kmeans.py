import pandas as pd
from sklearn.cluster import MiniBatchKMeans
import joblib
import os

ENCODED_PATH = "data/processed/encoded_data.csv"
MODEL_PATH = "models/kmeans_model.pkl"

print("🤖 Loading encoded data...")
df = pd.read_csv(ENCODED_PATH)
print("Encoded shape:", df.shape)

# Remove non-feature columns if present
if "restaurant_name" in df.columns:
    df = df.drop(columns=["restaurant_name"])

# 🔥 FIX 1: Remove rows with NaN
print("🧹 Cleaning missing values...")
df = df.dropna()

# OR (Better Option)
# df = df.fillna(0)

print("After cleaning:", df.shape)

# Auto-adjust cluster count
n_samples = df.shape[0]
n_clusters = min(5, n_samples)

print(f"⚡ Training MiniBatchKMeans ({n_clusters} clusters)...")

kmeans = MiniBatchKMeans(
    n_clusters=n_clusters,
    random_state=42,
    batch_size=10
)

# cluster_labels = kmeans.fit_predict(df)

# # Save model
# os.makedirs("models", exist_ok=True)
# joblib.dump(kmeans, MODEL_PATH)

# print("✅ Model saved successfully!")


# After fitting
cluster_labels = kmeans.fit_predict(df)

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(kmeans, MODEL_PATH)

print("✅ Model saved successfully!")