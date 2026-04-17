# Fleet Analysis

Data analysis of used‑car listings, exploring regional pricing, depreciation, optimal mileage replacement, and more.

The project is actively evolving with ongoing exploration and model improvements.

## Requirements

- Python and Pip
- (Optional) Docker

## Dataset Source

This project uses the [Used Cars Dataset](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data) from Kaggle.

The raw dataset is **not included** in this repository due to size (1GB+).  
Instead:

- The raw dataset can be downloaded from Kaggle using the link above. You need a Kaggle account.
- Place it in `data/raw/`.
- A **cleaned, filtered, and compressed subset** used for analysis is included in `data/processed/`  

This ensures the project remains lightweight, reproducible, and easy to clone.

## Reproducing the Environment With Docker (Recommended)

1. Download the Kaggle Dataset.
1. Create a folder: `data/raw`.
1. Place the downloaded dataset inside `data/raw/`.
1. Build the Docker image:

```bash
sudo docker build -t fleet-analysis .
```

1. Run the container:

```bash
sudo docker run -p 8888:8888 -v $(pwd):/home/jovyan/work fleet-analysis
```

1. Open the Jupyter URL printed in the terminal.
1. From the Jupyter home screen, open a new terminal.
1. Navigate to the `work` directory (should be default).
1. Run the dataset reduction script:

```bash
python reduce_dataset.py
```

This step drastically reduces the dataset size so the project runs smoothly even on low‑power hardware.

1. Open any notebook and load the processed dataframe using the first code cell.

### Updating Dataset Filters

If you want to change which columns or manufacturers are kept:

Edit `COLS_TO_KEEP` or `KEEP_MANUFACTURERS` inside `reduce_dataset.py`.

Re-run the script inside the Jupyter terminal.

The processed files will be overwritten automatically.

## Quick Start (Docker)

```bash
sudo docker build -t fleet-analysis .
sudo docker run -p 8888:8888 -v $(pwd):/home/jovyan/work fleet-analysis
```
