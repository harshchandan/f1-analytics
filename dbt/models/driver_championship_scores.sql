{{ config(materialized='table') }}

select
    "Season",
    "DriverId",
    "FullName",
    races,
    wins,
    podiums,
    points,
    avg_finish,
    {{ calculate_championship_points('wins', 'podiums', 'points') }} as championship_score
from {{ ref('driver_season_stats') }}