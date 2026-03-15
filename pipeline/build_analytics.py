#!/usr/bin/env python3
"""
Build analytics tables using dbt.

This script runs the dbt models to transform raw data into analytics tables.
"""

import subprocess
import sys
import os

def run_dbt():
    """Run dbt build command."""
    try:
        # Change to dbt directory
        os.chdir('dbt')

        # Run dbt build
        result = subprocess.run(['dbt', 'build'], capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ dbt build completed successfully!")
            print(result.stdout)
        else:
            print("❌ dbt build failed!")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            sys.exit(1)

        # Export tables to parquet
        result2 = subprocess.run(['python', 'export_tables.py'], capture_output=True, text=True)

        if result2.returncode == 0:
            print("✅ Table export completed successfully!")
            print(result2.stdout)
        else:
            print("❌ Table export failed!")
            print("STDOUT:", result2.stdout)
            print("STDERR:", result2.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_dbt()