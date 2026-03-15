import pandas as pd
import os
import glob

RAW_PATH = "data/raw"
PROCESSED_FILE = "data/processed/race_results_combined.parquet"

print("\n--- Combining race results ---")

# ------------------------------------------------
# Detect raw parquet files
# ------------------------------------------------

raw_files = glob.glob(f"{RAW_PATH}/race_results_*.parquet")

if not raw_files:
    print("No raw files found")
    exit()

years = []

for file_path in raw_files:

    filename = os.path.basename(file_path)

    year_str = filename.replace("race_results_", "").replace(".parquet", "")

    try:
        year = int(year_str)
        years.append(year)

    except ValueError:
        print(f"Skipping invalid file: {filename}")

years.sort()

print("Detected seasons:", years)

# ------------------------------------------------
# Load raw datasets
# ------------------------------------------------

all_results = []

for year in years:

    file_path = f"{RAW_PATH}/race_results_{year}.parquet"

    if os.path.exists(file_path):

        df = pd.read_parquet(file_path)

        print(f"Loaded {year} rows: {len(df)}")

        all_results.append(df)

    else:

        print(f"Missing file: {file_path}")


if not all_results:
    print("No valid raw datasets found")
    exit()


# ------------------------------------------------
# Combine raw data
# ------------------------------------------------

new_data = pd.concat(all_results, ignore_index=True)

print("Total rows from raw files:", len(new_data))


# ------------------------------------------------
# Incremental merge if processed file exists
# ------------------------------------------------

if os.path.exists(PROCESSED_FILE):

    existing_data = pd.read_parquet(PROCESSED_FILE)

    print("Existing processed rows:", len(existing_data))

    combined = pd.concat([existing_data, new_data], ignore_index=True)

else:

    print("No existing processed dataset found")

    combined = new_data


# ------------------------------------------------
# Remove duplicates
# ------------------------------------------------

combined = combined.drop_duplicates(
    subset=["Season", "Round", "DriverId"]
)

print("Rows after deduplication:", len(combined))


# ------------------------------------------------
# Save processed dataset
# ------------------------------------------------

os.makedirs("data/processed", exist_ok=True)

combined.to_parquet(PROCESSED_FILE, index=False)

print("\nSaved processed dataset:", PROCESSED_FILE)
print("--- Combine step completed ---\n")