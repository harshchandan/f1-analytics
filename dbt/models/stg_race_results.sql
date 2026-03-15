{{ config(materialized='table') }}

select
    "Season",
    "Round",
    "RaceName",
    "DriverId",
    "FullName",
    "TeamName",
    "Position",
    "Points"
from read_parquet('../data/processed/race_results_combined.parquet')