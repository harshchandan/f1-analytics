# F1 Analytics Data Pipeline

A modern **Formula 1 historical analytics pipeline** built using **Python, FastF1, DuckDB, and GitHub Actions**.

This project ingests race results from the FastF1 API, processes them into structured datasets, and produces analytics-ready tables that can be queried using SQL. The pipeline is designed to automatically update the dataset using GitHub Actions.

---

# Project Goals

This repository demonstrates how to build a **modern data engineering pipeline** using real-world sports data.

Key objectives:

* Build a reproducible **data pipeline**
* Create a structured **Formula 1 analytics dataset**
* Demonstrate **layered data architecture**
* Enable fast analytics using **DuckDB**
* Automate data updates using **GitHub Actions**

---

# Data Source

The pipeline uses the **FastF1 API** to extract race session data from modern Formula 1 seasons.

The dataset includes information such as:

* Race results
* Driver details
* Constructor information
* Grid positions
* Points scored
* Race metadata

The project currently focuses on **modern F1 seasons (2018 onward)** where timing data is reliable.

---

# Data Architecture

The pipeline follows a layered data engineering architecture commonly used in modern analytics platforms.

```text
FastF1 API
    │
    ▼
Ingestion Scripts
    │
    ▼
Raw Data Layer
    │
    ▼
Processed Data Layer
    │
    ▼
Analytics Layer
    │
    ▼
DuckDB Query Engine
```

Each stage progressively transforms the data into more structured and analytics-ready datasets.

---

# Repository Structure

```text
f1-analytics/

├── data/
│   ├── raw/                # Yearly race results extracted from FastF1
│   ├── processed/          # Combined cleaned dataset
│   └── analytics/          # Aggregated analytics datasets

├── ingestion/
│   ├── fetch_race_results_*.py
│   └── combine_race_results.py

├── pipeline/
│   ├── validate_race_results.py
│   ├── build_dimensions.py
│   ├── build_analytics.py
│   ├── build_driver_career_stats.py
│   └── build_driver_streaks.py

├── queries/
│   └── example SQL queries for DuckDB

├── notebooks/
│   └── exploratory analysis

├── docs/
│   └── architecture documentation

├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

# Data Layers

## Raw Layer

The raw layer stores race results extracted directly from the FastF1 API.

Example files:

```text
data/raw/race_results_2018.parquet
data/raw/race_results_2019.parquet
data/raw/race_results_2020.parquet
```

Each dataset contains driver-level race results for each event.

---

## Processed Layer

Raw datasets are combined and cleaned into a unified dataset.

```text
data/processed/race_results_combined.parquet
```

This dataset contains:

* Driver information
* Team information
* Grid position
* Finishing position
* Points scored
* Race metadata

---

## Analytics Layer

The analytics layer contains aggregated tables used for analysis and dashboards.

```text
data/analytics/

race_winners.parquet
driver_season_stats.parquet
constructor_season_stats.parquet
driver_career_stats.parquet
driver_streaks.parquet
```

These datasets enable deeper insights such as:

* Race winners by season
* Driver career statistics
* Constructor dominance
* Podium streaks
* Win streaks

---

# Example Analytics

This dataset enables analysis such as:

* Which driver has the most wins
* Driver performance across seasons
* Constructor dominance patterns
* Longest winning streaks
* Podium consistency

---

# Running the Pipeline

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the pipeline

```bash
python run_pipeline.py
```

The pipeline performs the following steps:

1. Validate processed datasets
2. Build dimension tables
3. Generate analytics datasets

---

# Querying the Data

DuckDB is used to query parquet datasets directly.

Example query:

```sql
SELECT FullName, wins
FROM read_parquet('data/analytics/driver_career_stats.parquet')
ORDER BY wins DESC
LIMIT 10;
```

DuckDB allows SQL queries on parquet files without requiring a traditional database.

---

# Automation

The pipeline is automated using **GitHub Actions**.

The workflow performs the following tasks:

1. Fetch race results from FastF1
2. Update raw datasets
3. Rebuild processed datasets
4. Recompute analytics tables
5. Commit updated data to the repository

This ensures the dataset stays up to date throughout the Formula 1 season.

---

# Future Improvements

Planned enhancements include:

* Introducing **dbt** for transformation management
* Adding qualifying and lap-level analytics
* Creating additional advanced analytics datasets
* Building a **FastAPI analytics API**
* Developing interactive dashboards
* Extending the dataset to additional seasons

---

# License

MIT License