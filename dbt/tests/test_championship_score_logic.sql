-- Test that championship scores are reasonable
-- Championship score should be greater than or equal to actual points
-- (since we add bonus points for wins and podiums)

select
    "Season",
    "DriverId",
    "FullName",
    points as actual_points,
    championship_score,
    wins,
    podiums
from {{ ref('driver_championship_scores') }}
where championship_score < points
  or championship_score > points + (wins * 10) + (podiums * 5)
  or championship_score < 0