import pandas as pd
import os

df = pd.read_parquet("data/processed/race_results_combined.parquet")

df = df.sort_values(["DriverId", "Season", "Round"])

streak_results = []

for driver_id, group in df.groupby("DriverId"):

    group = group.reset_index(drop=True)

    win_streak = 0
    podium_streak = 0
    max_win_streak = 0
    max_podium_streak = 0

    driver_name = group["FullName"].iloc[0]

    for _, row in group.iterrows():

        if row["Position"] == 1:
            win_streak += 1
        else:
            win_streak = 0

        if row["Position"] <= 3:
            podium_streak += 1
        else:
            podium_streak = 0

        max_win_streak = max(max_win_streak, win_streak)
        max_podium_streak = max(max_podium_streak, podium_streak)

    streak_results.append({
        "DriverId": driver_id,
        "FullName": driver_name,
        "max_win_streak": max_win_streak,
        "max_podium_streak": max_podium_streak
    })


streak_df = pd.DataFrame(streak_results)

os.makedirs("data/analytics", exist_ok=True)

streak_df.to_parquet(
    "data/analytics/driver_streaks.parquet",
    index=False
)

print("Driver streak table created:", len(streak_df))