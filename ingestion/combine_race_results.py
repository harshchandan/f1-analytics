import pandas as pd
import os
import glob

# Dynamically find all race_results_*.parquet files in data/raw/
raw_files = glob.glob("data/raw/race_results_*.parquet")

years = []
for file_path in raw_files:
    # Extract year from filename, e.g., race_results_2018.parquet -> 2018
    filename = os.path.basename(file_path)
    year_str = filename.replace("race_results_", "").replace(".parquet", "")
    try:
        year = int(year_str)
        years.append(year)
    except ValueError:
        print(f"Skipping invalid file: {filename}")

years.sort()  # Sort years in ascending order

all_results = []

for year in years:
    file_path = f"data/raw/race_results_{year}.parquet"
    if os.path.exists(file_path):
        df = pd.read_parquet(file_path)
        all_results.append(df)
        print(f"Loaded data for {year}")
    else:
        print(f"File for {year} not found: {file_path}")

if all_results:
    combined_df = pd.concat(all_results, ignore_index=True)
    os.makedirs("data/processed", exist_ok=True)
    combined_df.to_parquet("data/processed/race_results_combined.parquet", index=False)
    print("Saved combined dataset")
else:
    print("No data files found to combine")