import pandas as pd
import os

df = pd.read_parquet("data/processed/race_results_combined.parquet")

os.makedirs("data/analytics", exist_ok=True)

career_stats = (
    df.groupby(["DriverId", "FullName"])
    .agg(
        races=("Position", "count"),
        wins=("Position", lambda x: (x == 1).sum()),
        podiums=("Position", lambda x: (x <= 3).sum()),
        points=("Points", "sum"),
        avg_finish=("Position", "mean"),
        best_finish=("Position", "min")
    )
    .reset_index()
)

career_stats.to_parquet(
    "data/analytics/driver_career_stats.parquet",
    index=False
)

print("Driver career stats created:", len(career_stats))