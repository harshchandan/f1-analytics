import subprocess
import time

def run_step(name, command):

    print(f"\n--- Running step: {name} ---")

    start = time.time()

    subprocess.run(command, check=True)

    duration = round(time.time() - start, 2)

    print(f"Step completed: {name} ({duration} sec)")


print("\n========== F1 DATA PIPELINE START ==========")

run_step(
    "Validate race results",
    ["python", "pipeline/validate_race_results.py"]
)

run_step(
    "Build dimension tables",
    ["python", "pipeline/build_dimensions.py"]
)

run_step(
    "Build analytics tables",
    ["python", "pipeline/build_analytics.py"]
)

print("\n========== PIPELINE COMPLETED ==========")