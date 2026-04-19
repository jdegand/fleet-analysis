import pandas as pd
from pathlib import Path

INTERIM_PATH = Path("data/interim/vehicles_trimmed.parquet")
EXPORT_PATH = Path("data/processed/vehicles_trimmed.csv")

# Optional: cap rows for Looker Studio performance
MAX_ROWS = 250_000   # adjust as needed


def convert_parquet_to_csv():
    if not INTERIM_PATH.exists():
        raise FileNotFoundError(f"Parquet file not found: {INTERIM_PATH}")

    print(f"Loading Parquet file: {INTERIM_PATH}")
    df = pd.read_parquet(INTERIM_PATH)

    print(f"Loaded {len(df):,} rows")

    # Optional downsample for Looker Studio
    if len(df) > MAX_ROWS:
        print(f"Sampling down to {MAX_ROWS:,} rows for Looker Studio")
        df = df.sample(MAX_ROWS, random_state=42)

    # Ensure output directory exists
    EXPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    print(f"Exporting CSV to: {EXPORT_PATH}")
    df.to_csv(EXPORT_PATH, index=False)

    print("CSV export complete.")
    print(f"Final CSV size: {EXPORT_PATH.stat().st_size / 1_000_000:.2f} MB")


if __name__ == "__main__":
    convert_parquet_to_csv()
