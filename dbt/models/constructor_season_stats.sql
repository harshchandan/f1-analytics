{{ config(materialized='table') }}

select
    "Season",
    "TeamName",
    count(*) as races,
    sum(case when "Position" = 1 then 1 else 0 end) as wins,
    sum(case when "Position" <= 3 then 1 else 0 end) as podiums,
    sum("Points") as points,
    avg("Position") as avg_finish
from {{ ref('stg_race_results') }}
group by "Season", "TeamName"