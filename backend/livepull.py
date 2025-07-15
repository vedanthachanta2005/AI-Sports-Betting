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

# Optional: convert to DataFrame (eager) and print first 5 rows
df = lf.collect()
print("First 5 records:\n", df.head())

# Optional: Save as CSV locally
df.write_csv("backend/live_atp_tennis.csv")
print("✅ CSV successfully saved to backend/live_atp_tennis.csv")
