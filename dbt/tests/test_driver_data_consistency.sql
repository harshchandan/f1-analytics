-- Test data consistency between driver_season_stats and driver_championship_scores
-- Both tables should have the same drivers for each season

select
    coalesce(dss."Season", dcs."Season") as season,
    coalesce(dss."DriverId", dcs."DriverId") as driver_id,
    case
        when dss."DriverId" is null then 'Missing from driver_season_stats'
        when dcs."DriverId" is null then 'Missing from driver_championship_scores'
        else 'OK'
    end as status
from {{ ref('driver_season_stats') }} dss
full outer join {{ ref('driver_championship_scores') }} dcs
    on dss."Season" = dcs."Season"
    and dss."DriverId" = dcs."DriverId"
where dss."DriverId" is null
   or dcs."DriverId" is null