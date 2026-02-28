"""
This script pulls WRDS Bond Returns data from WRDS.
Pattern follows pull_wrds_markit.py: pull helpers + loader helpers + main write.
"""

import sys
from pathlib import Path

sys.path.insert(1, "./src/")

import pandas as pd
import wrds
import chartbook

BASE_DIR = chartbook.env.get_project_root()
DATA_DIR = BASE_DIR / "_data"
WRDS_USERNAME = chartbook.env.get("WRDS_USERNAME")
START_YEAR = 2020
END_YEAR = 2020
MIN_OUTSTANDING_THOUSANDS = 100


def _get_where_clauses(year: int) -> list[str]:
    """Build SQL filters for a given year."""
    where_clauses = [
        #f"date >= '{year}-01-01' AND date < '{year + 1}-01-01'",
        #"security_level = 'SEN'",
        #"maturity BETWEEN (date + INTERVAL '1 year') AND (date + INTERVAL '10 years')",
        ## amount_outstanding is stored in thousands: 100 == $100,000
        #f"amount_outstanding > {MIN_OUTSTANDING_THOUSANDS}",
        # Deterministic 0/1 flag: 1 means convertible, so keep conv = 0 only.
        #"conv = 0",
        #"price_eom >= 50",
        "isin IS NOT NULL AND TRIM(isin) <> ''",
    ]
    return where_clauses


def get_bondret_data_as_dict(
    wrds_username=WRDS_USERNAME,
    start_year: int = START_YEAR,
    end_year: int = END_YEAR,
):
    """
    Pull WRDS Bond Returns data by year from wrdsapps_bondret.bondret.

    Returns:
        dict[int, pd.DataFrame]: one DataFrame per year.
    """
    db = wrds.Connection(wrds_username=wrds_username)

    yearly_data = {}
    for year in range(start_year, end_year + 1):
        print(f"Pulling wrdsapps_bondret.bondret for {year}...", flush=True)
        where_clauses = _get_where_clauses(year)
        query = f"""
        SELECT
            date,
            issue_id,
            cusip,
            bond_sym_id,
            bsym,
            isin,
            company_symbol,
            bond_type,
            security_level,
            conv,
            offering_date,
            offering_amt,
            offering_price,
            principal_amt,
            maturity,
            treasury_maturity,
            coupon,
            day_count_basis,
            dated_date,
            first_interest_date,
            last_interest_date,
            ncoups,
            t_date,
            t_volume,
            t_dvolume,
            t_spread,
            t_yld_pt,
            yield,
            amount_outstanding,
            price_eom,
            price_ldm,
            price_l5m,
            gap,
            coupmonth,
            nextcoup,
            coupamt,
            coupacc,
            multicoups,
            ret_eom,
            ret_ldm,
            ret_l5m,
            tmt,
            remcoups,
            duration,
            r_sp,
            r_mr,
            r_fr,
            n_sp,
            n_mr,
            n_fr,
            rating_num,
            rating_cat,
            rating_class,
            defaulted,
            default_date,
            default_type,
            reinstated,
            reinstated_date
        FROM wrdsapps_bondret.bondret
        WHERE {' AND '.join(where_clauses)}
        """
        df = db.raw_sql(
            query,
            date_cols=[
                "date",
                "offering_date",
                "maturity",
                "dated_date",
                "first_interest_date",
                "last_interest_date",
                "t_date",
                "nextcoup",
                "default_date",
                "reinstated_date",
            ],
        )
        df["year"] = year
        yearly_data[year] = df
        print(f"Finished {year}: {len(df)} rows", flush=True)

    return yearly_data


def combine_bondret_data(bondret_data: dict[int, pd.DataFrame]) -> pd.DataFrame:
    """Concatenate year-keyed bond return DataFrames into one DataFrame."""
    if not bondret_data:
        return pd.DataFrame()
    return pd.concat(list(bondret_data.values()), ignore_index=True)


def pull_bondret_data(
    wrds_username=WRDS_USERNAME,
    start_year: int = START_YEAR,
    end_year: int = END_YEAR,
) -> pd.DataFrame:
    """Convenience wrapper: pull + combine."""
    data_by_year = get_bondret_data_as_dict(
        wrds_username=wrds_username, start_year=start_year, end_year=end_year
    )
    return combine_bondret_data(data_by_year)


def load_bondret_filtered(data_dir=DATA_DIR):
    path = Path(data_dir) / "wrds_bondret_filtered.parquet"
    return pd.read_parquet(path)


if __name__ == "__main__":
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df = pull_bondret_data(wrds_username=WRDS_USERNAME)
    out_path = DATA_DIR / "wrds_bondret_filtered.parquet"
    df.to_parquet(out_path)
    print(f"Saved {len(df)} rows to {out_path}", flush=True)
