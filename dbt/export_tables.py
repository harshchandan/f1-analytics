#!/usr/bin/env python3
"""
Export dbt models to parquet files for analytics.

This script connects to the DuckDB database created by dbt and exports
the analytics tables to parquet files in data/analytics/.
"""

import duckdb
import os

def export_tables():
    """Export dbt tables to parquet files."""
    # Connect to the dbt database
    con = duckdb.connect('f1_analytics.duckdb')

    # Create analytics directory
    os.makedirs('../data/analytics', exist_ok=True)

    # Tables to export
    tables = [
        'race_winners',
        'driver_season_stats',
        'constructor_season_stats',
        'driver_championship_scores',
        'race_results_with_circuits'
    ]

    for table in tables:
        # Export to parquet
        output_path = f'../data/analytics/{table}.parquet'
        con.execute(f"COPY {table} TO '{output_path}' (FORMAT PARQUET)")

        # Get row count
        result = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()
        print(f"Exported {table}: {result[0]} rows to {output_path}")

    con.close()
    print("✅ All tables exported successfully!")

if __name__ == "__main__":
    export_tables()