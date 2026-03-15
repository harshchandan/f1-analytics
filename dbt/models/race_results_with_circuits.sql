{{ config(materialized='table') }}

select
    r.*,
    c.circuit_name,
    c.country as circuit_country,
    c.city as circuit_city,
    c.first_race_year as circuit_first_race_year
from {{ ref('stg_race_results') }} r
left join {{ ref('circuits') }} c
    on r."RaceName" = c.race_name