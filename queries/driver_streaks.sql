SELECT FullName, max_win_streak, max_podium_streak
FROM read_parquet('data/analytics/driver_streaks.parquet')
ORDER BY max_win_streak DESC
LIMIT 10;