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
from {{ ref('stg_race_results') }}
where "Position" = 1