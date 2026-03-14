# F1 Analytics

A data analytics project for Formula 1 race results from 2018-2024.

## Project Structure

```
f1-analytics/
├── data/
│   ├── raw/           # Individual year race results (parquet)
│   └── processed/     # Combined and processed datasets
├── ingestion/         # Data ingestion scripts
│   ├── fetch_race_results_*.py    # Year-wise data fetching
│   └── combine_race_results.py    # Combine raw data
├── notebooks/         # Jupyter notebooks for analysis
└── README.md
```

## Data Pipeline

### 1. Fetch Data
Run individual year scripts to fetch race results:

```bash
python ingestion/fetch_race_results_2018.py
python ingestion/fetch_race_results_2019.py
# ... etc
```

**Note:** Due to API rate limits (500 calls/hour), run scripts with delays between them.

### 2. Combine Data
Combine all fetched years into a single dataset:

```bash
python ingestion/combine_race_results.py
```

This creates `data/processed/race_results_combined.parquet`

### 3. Explore Data
Open the exploration notebook:

```bash
jupyter notebook notebooks/explore_race_results.ipynb
```

## Data Sources

- **FastF1 API**: Race results, driver info, team data
- **Years**: 2018-2024

## Current Status

- ✅ Data fetched: 2018, 2019, 2020, 2021, 2022, 2023, 2024
- 📊 Combined dataset available in `data/processed/`

## Next Steps

1. **Fetch remaining years** (2021-2024) with appropriate delays
2. **Data validation** - Check for missing races/drivers
3. **Advanced analytics** - Qualifying analysis, pit stops, etc.
4. **Visualization dashboard** - Streamlit or similar
5. **Predictive modeling** - Race outcome predictions
