# pip install kagglehub[polars-datasets] polars

import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the correct file name from the Kaggle dataset
file_path = "atp_tennis.csv"

# Load dataset as a lazy Polars DataFrame (lf = LazyFrame)
lf = kagglehub.load_dataset(
    KaggleDatasetAdapter.POLARS,
    "dissfya/atp-tennis-2000-2023daily-pull",
    file_path
)

# Collect into memory (eager execution)
df = lf.collect()

# Print first 5 records
print("First 5 records:\n", df.head())

# Print last 5 records
print("\nLast 5 records:\n", df.tail())

# Save as CSV locally
df.write_csv("backend/live_atp_tennis.csv")
print("✅ CSV successfully saved to backend/live_atp_tennis.csv")
