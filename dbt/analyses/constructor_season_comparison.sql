-- Season-by-season comparison of top teams
-- Shows how constructor performance has evolved

select
    "Season",
    "TeamName",
    points,
    wins,
    podiums,
    round(points * 1.0 / nullif(races, 0), 2) as points_per_race,
    avg_finish,
    -- Rank teams within each season
    row_number() over (partition by "Season" order by points desc) as season_rank
from {{ ref('constructor_season_stats') }}
where "Season" >= 2018
order by "Season" desc, points desc