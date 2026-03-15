{% snapshot constructor_standings_snapshot %}

{{
    config(
      target_schema='snapshots',
      unique_key='constructor_season_key',
      strategy='timestamp',
      updated_at='snapshot_date',
      invalidate_hard_deletes=True,
    )
}}

select
    "Season" || '_' || "TeamName" as constructor_season_key,
    "Season",
    "TeamName",
    races,
    wins,
    podiums,
    points,
    avg_finish,
    CURRENT_TIMESTAMP as snapshot_date
from {{ ref('constructor_season_stats') }}

{% endsnapshot %}