import pandas as pd

df = pd.read_parquet("data/processed/race_results_combined.parquet")

print("Total rows:", len(df))

# check seasons
print("Seasons present:", sorted(df["Season"].unique()))

# check number of races
races = df[["Season","Round","RaceName"]].drop_duplicates()
print("Total races:", len(races))

# check winners
winners = df[df["Position"] == 1]

print("Total winners:", len(winners))

# check that each race has exactly one winner
winner_check = winners.groupby(["Season","Round"]).size()

bad_races = winner_check[winner_check != 1]

print("Races with incorrect number of winners: ", len(bad_races))

print("Validation complete")