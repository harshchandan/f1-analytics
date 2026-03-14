import subprocess

print("\n--- Running data validation ---")
subprocess.run(["python", "pipeline/validate_race_results.py"], check=True)

print("\n--- Building dimension tables ---")
subprocess.run(["python", "pipeline/build_dimensions.py"], check=True)

print("\n--- Building analytics tables ---")
subprocess.run(["python", "pipeline/build_analytics.py"], check=True)

print("\n--- Pipeline completed successfully ---")