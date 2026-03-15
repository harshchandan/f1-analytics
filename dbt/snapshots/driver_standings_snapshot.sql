{% snapshot driver_standings_snapshot %}

{{
    config(
      target_schema='snapshots',
      unique_key='driver_season_key',
      strategy='timestamp',
      updated_at='snapshot_date',
      invalidate_hard_deletes=True,
    )
}}

select
    "Season" || '_' || "DriverId" as driver_season_key,
    "Season",
    "DriverId",
    "FullName",
    races,
    wins,
    podiums,
    points,
    avg_finish,
    CURRENT_TIMESTAMP as snapshot_date
from {{ ref('driver_season_stats') }}

{% endsnapshot %}