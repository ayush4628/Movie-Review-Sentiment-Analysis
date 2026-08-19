import os
from tensorflow.keras.models import load_model

MODEL_PATH = "imdb_gru_model.keras"

print("=" * 50)
print("Loading model...")
print("=" * 50)

model = load_model(
    MODEL_PATH,
    compile=False
)

print("\nMODEL SUMMARY")
print("=" * 50)

model.summary()

print("\nMODEL SIZE")
print("=" * 50)

size_mb = os.path.getsize(MODEL_PATH) / (1024 * 1024)

print(f"Model file size: {size_mb:.2f} MB")

print("\nTOTAL PARAMETERS")
print("=" * 50)

print(f"Total params: {model.count_params():,}")