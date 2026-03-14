import pandas as pd
import os

# Load processed dataset
df = pd.read_parquet("data/processed/race_results_combined.parquet")

os.makedirs("data/processed/dimensions", exist_ok=True)

# -------------------------
# Drivers dimension
# -------------------------

drivers = df[
    ["DriverId", "FullName", "FirstName", "LastName", "CountryCode"]
].drop_duplicates()

drivers.to_parquet(
    "data/processed/dimensions/drivers.parquet",
    index=False
)

print("Drivers table created:", len(drivers))


# -------------------------
# Constructors dimension
# -------------------------

constructors = df[
    ["TeamId", "TeamName", "TeamColor"]
].drop_duplicates()

constructors.to_parquet(
    "data/processed/dimensions/constructors.parquet",
    index=False
)

print("Constructors table created:", len(constructors))


# -------------------------
# Races dimension
# -------------------------

races = df[
    ["Season", "Round", "RaceName"]
].drop_duplicates()

races.to_parquet(
    "data/processed/dimensions/races.parquet",
    index=False
)

print("Races table created:", len(races))


print("Dimension tables built successfully")