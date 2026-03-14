import fastf1
import pandas as pd
import os
import time

os.makedirs("f1_cache", exist_ok=True)
fastf1.Cache.enable_cache("f1_cache")

seasons = [2023]

all_results = []

for season in seasons:

    print(f"Fetching season {season}")

    schedule = fastf1.get_event_schedule(season)

    for _, event in schedule.iterrows():

        try:
            round_number = event["RoundNumber"]
            race_name = event["EventName"]

            session = fastf1.get_session(season, round_number, "R")

            session.load(laps=False, telemetry=False, weather=False)

            results = session.results.copy()

            results["Season"] = season
            results["Round"] = round_number
            results["RaceName"] = race_name

            all_results.append(results)

            print(f"Loaded {race_name}")

            time.sleep(8)

        except Exception as e:
            print(f"Error loading {race_name}: {e}")

df = pd.concat(all_results, ignore_index=True)

os.makedirs("data/raw", exist_ok=True)

df.to_parquet("data/raw/race_results_2023.parquet", index=False)

print("Saved dataset for 2023")