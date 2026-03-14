import pandas as pd
import sys

df = pd.read_parquet("data/processed/race_results_combined.parquet")

print("Total rows:", len(df))

# --------------------------
# Check seasons exist
# --------------------------

seasons = sorted(df["Season"].unique())

print("Seasons present:", seasons)

if len(seasons) == 0:
    print("ERROR: No seasons found")
    sys.exit(1)


# --------------------------
# Check race uniqueness
# --------------------------

races = df[["Season", "Round"]].drop_duplicates()

print("Total races:", len(races))


# --------------------------
# Check exactly one winner
# --------------------------

winners = df[df["Position"] == 1]

winner_counts = winners.groupby(["Season", "Round"]).size()

bad_races = winner_counts[winner_counts != 1]

if bad_races.empty:
    print("Winner validation passed")
else:
    print("ERROR: Some races do not have exactly one winner")
    print(bad_races)
    sys.exit(1)


# --------------------------
# Check position validity
# --------------------------

if (df["Position"] <= 0).any():
    print("ERROR: Invalid race position detected")
    sys.exit(1)

print("Position validation passed")


# --------------------------
# Check duplicate results
# --------------------------

duplicates = df.duplicated(
    subset=["Season", "Round", "DriverId"]
).sum()

if duplicates > 0:
    print("ERROR: Duplicate race results detected:", duplicates)
    sys.exit(1)

print("Duplicate validation passed")


print("\nAll validation checks passed")