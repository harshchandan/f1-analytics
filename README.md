# F1 Analytics Data Pipeline

A modern Formula 1 historical analytics pipeline built using Python, FastF1, DuckDB, and GitHub Actions.

This project ingests race results from the FastF1 API, processes them into structured datasets, and produces analytics-ready tables that can be queried using SQL. The pipeline automatically updates the dataset weekly using GitHub Actions.

---

## Project Goals

The purpose of this project is to demonstrate how to build a modern data engineering pipeline around real-world sports data.

Key goals include:

* Building a structured data pipeline
* Creating a historical Formula 1 analytics dataset
* Demonstrating layered data lake architecture
* Enabling fast SQL analytics using DuckDB
* Automating dataset updates using GitHub Actions

---

## Data Source

The project uses the FastF1 API to extract race session data from modern Formula 1 seasons.

FastF1 provides access to:

* Race results
* Driver information
* Team information
* Session metadata

The dataset currently focuses on modern Formula 1 seasons (2018 onward) where telemetry and timing data are reliable.

---

## Architecture

The project follows a layered data engineering architecture commonly used in modern data platforms.

FastF1 API
↓
Ingestion Scripts
↓
Raw Data Layer
↓
Processed Data Layer
↓
Analytics Layer
↓
DuckDB Query Engine

The pipeline extracts data, transforms it into structured datasets, and generates analytics tables used for analysis.

---

## Repository Structure

f1-analytics/

data/
 raw/       # yearly race results extracted from FastF1
 processed/   # combined cleaned dataset
 analytics/   # aggregated analytics datasets

ingestion/
 fetch_race_results_*.py
 combine_race_results.py

pipeline/
 validate_race_results.py
 build_dimensions.py
 build_analytics.py
 build_driver_career_stats.py
 build_driver_streaks.py

queries/
 example SQL queries for DuckDB

notebooks/
 exploratory analysis notebooks

docs/
 architecture documentation

run_pipeline.py

requirements.txt

README.md

---

## Data Layers

### Raw Layer

The raw layer stores race results extracted from the FastF1 API for each season.

Example files:

data/raw/race_results_2018.parquet
data/raw/race_results_2019.parquet
data/raw/race_results_2020.parquet

These datasets contain driver-level race results for each event.

---

### Processed Layer

Raw datasets are combined into a unified dataset.

data/processed/race_results_combined.parquet

This dataset includes columns such as:

* Driver information
* Team information
* Grid position
* Race finishing position
* Points scored
* Race metadata

---

### Analytics Layer

The analytics layer contains aggregated tables used for analysis and dashboards.

data/analytics/

race_winners.parquet
driver_season_stats.parquet
constructor_season_stats.parquet
driver_career_stats.parquet
driver_streaks.parquet

These tables enable advanced analysis such as:

* Race winners by season
* Driver career statistics
* Constructor dominance
* Podium and win streaks

---

## Example Analytics

The dataset allows analysis such as:

* Which driver has the most wins
* Season-level driver performance
* Constructor dominance patterns
* Longest winning streaks
* Podium consistency

Modern seasons show strong dominance periods from drivers like Max Verstappen and Lewis Hamilton.

---

## Running the Pipeline

Install dependencies:

pip install -r requirements.txt

Run the pipeline:

python run_pipeline.py

This will:

1. Validate the processed dataset
2. Build dimension tables
3. Generate analytics datasets

---

## Querying the Data

DuckDB is used to query parquet datasets directly.

Example query:

SELECT FullName, wins
FROM read_parquet('data/analytics/driver_career_stats.parquet')
ORDER BY wins DESC
LIMIT 10;

DuckDB allows SQL queries on parquet files without requiring a traditional database.

---

## Automation

The pipeline is automated using GitHub Actions.

The workflow runs weekly and performs the following steps:

1. Fetch race results from FastF1
2. Update raw datasets
3. Rebuild processed datasets
4. Recompute analytics tables
5. Commit updated data to the repository

---

## Future Improvements

Planned improvements include:

* Introducing dbt for transformation management
* Adding additional analytics datasets
* Incorporating qualifying and lap data
* Building a FastAPI analytics API
* Creating interactive dashboards
* Extending the dataset to additional seasons

---

## License

MIT License
