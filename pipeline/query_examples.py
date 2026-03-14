import duckdb

# Connect to DuckDB (creates DB file if not present)
con = duckdb.connect("f1_analytics.duckdb")

print("\n--- Race winners example ---")

query = """
SELECT Season, RaceName, FullName, TeamName
FROM read_parquet('data/analytics/race_winners.parquet')
ORDER BY Season DESC
LIMIT 10
"""

result = con.execute(query).fetchdf()

print(result)

print("\n--- Driver wins leaderboard ---")

query = """
SELECT FullName, COUNT(*) AS wins
FROM read_parquet('data/analytics/race_winners.parquet')
GROUP BY FullName
ORDER BY wins DESC
LIMIT 10
"""

result = con.execute(query).fetchdf()

print(result)