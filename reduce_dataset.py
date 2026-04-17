import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pathlib import Path

RAW_PATH = Path("data/raw/vehicles.csv")
INTERIM_PATH = Path("data/interim/vehicles_trimmed.parquet")
PROCESSED_PATH = Path("data/processed/fleet_model_inputs.parquet")

KEEP_MANUFACTURERS = [
    "infiniti", "toyota", "ford", "bmw",
    "mini", "mercedes-benz", "cadillac"
]

# just re-run script after changing columns
COLS_TO_KEEP = [
    "price", "year", "manufacturer", "model",
    "odometer", "state", "posting_date",
    "region"
]

def reduce_dataset():
    INTERIM_PATH.parent.mkdir(parents=True, exist_ok=True)

    writer = None  # ParquetWriter will be created after first chunk

    for i, chunk in enumerate(pd.read_csv(
        RAW_PATH,
        chunksize=50_000,
        low_memory=False,
        compression="infer"
    )):
        print(f"Processing chunk {i}")

        # Normalize manufacturer
        chunk["manufacturer"] = (
            chunk["manufacturer"]
            .astype(str)
            .str.lower()
            .str.strip()
        )

        # Filter manufacturers
        chunk = chunk[chunk["manufacturer"].isin(KEEP_MANUFACTURERS)]

        # Keep only needed columns
        chunk = chunk[COLS_TO_KEEP]

        # Basic sanity filters
        chunk = chunk[
            chunk["price"].between(500, 150000)
            & chunk["odometer"].between(1000, 300000)
            & chunk["year"].between(1995, 2024)
        ]

        if len(chunk) == 0:
            continue

        # Convert chunk to Arrow Table
        table = pa.Table.from_pandas(chunk, preserve_index=False)

        # Initialize writer on first valid chunk
        if writer is None:
            writer = pq.ParquetWriter(INTERIM_PATH, table.schema)

        writer.write_table(table)

    # Close writer
    if writer:
        writer.close()
    else:
        print("No matching rows found — nothing written.")
        return

    # Create sample
    df = pd.read_parquet(INTERIM_PATH)
    sample_size = min(50_000, len(df))

    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.sample(sample_size, random_state=42).to_parquet(PROCESSED_PATH, index=False)

    print("Dataset reduction complete.")
    print(f"Interim saved to: {INTERIM_PATH}")
    print(f"Processed saved to: {PROCESSED_PATH}")

if __name__ == "__main__":
    reduce_dataset()
