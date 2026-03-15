-- Top 10 drivers by championship points across all seasons
-- This analysis shows the all-time F1 greats

select
    "FullName",
    count(distinct "Season") as seasons_raced,
    sum(wins) as total_wins,
    sum(podiums) as total_podiums,
    sum(points) as total_points,
    round(avg(avg_finish), 2) as career_avg_finish,
    round(sum(points) * 1.0 / nullif(sum(races), 0), 2) as points_per_race
from {{ ref('driver_season_stats') }}
group by "FullName"
having sum(races) >= 10  -- Only drivers with significant F1 experience
order by total_points desc
limit 10