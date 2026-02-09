import pandas as pd
from pathlib import Path

DATA_DIR = Path("_data")

def main():
    url = "https://raw.githubusercontent.com/esiriwardane/arbitrage-spreads-public/main/raw/final_cds_bases.xlsx"
    df = pd.read_excel(url, sheet_name="Bases")
    # print(df)
    df.to_parquet(DATA_DIR / "markit_cds.parquet")

if __name__ == "__main__":
    main()

