import pandas as pd
import os

df = pd.read_parquet("data/processed/race_results_combined.parquet")

os.makedirs("data/analytics", exist_ok=True)

# -------------------------
# Race winners table
# -------------------------

race_winners = df[df["Position"] == 1][
    ["Season", "Round", "RaceName", "DriverId", "FullName", "TeamName", "Points"]
]

race_winners.to_parquet(
    "data/analytics/race_winners.parquet",
    index=False
)

print("Race winners table created:", len(race_winners))


# -------------------------
# Driver season statistics
# -------------------------

driver_season_stats = (
    df.groupby(["Season", "DriverId", "FullName"])
    .agg(
        races=("Position", "count"),
        wins=("Position", lambda x: (x == 1).sum()),
        podiums=("Position", lambda x: (x <= 3).sum()),
        points=("Points", "sum"),
        avg_finish=("Position", "mean")
    )
    .reset_index()
)

driver_season_stats.to_parquet(
    "data/analytics/driver_season_stats.parquet",
    index=False
)

print("Driver season stats created:", len(driver_season_stats))


# -------------------------
# Constructor season stats
# -------------------------

constructor_season_stats = (
    df.groupby(["Season", "TeamId", "TeamName"])
    .agg(
        races=("Position", "count"),
        wins=("Position", lambda x: (x == 1).sum()),
        podiums=("Position", lambda x: (x <= 3).sum()),
        points=("Points", "sum")
    )
    .reset_index()
)

constructor_season_stats.to_parquet(
    "data/analytics/constructor_season_stats.parquet",
    index=False
)

print("Constructor season stats created:", len(constructor_season_stats))


print("Analytics tables built successfully")