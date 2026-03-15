SELECT FullName, wins, podiums, points
FROM read_parquet('data/analytics/driver_career_stats.parquet')
ORDER BY wins DESC
LIMIT 10;