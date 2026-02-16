# Dataframe: `SE:ftsfr_cds_bond_basis_non_aggregated` - ftsfr_cds_bond_basis_non_aggregated

## CDS-Bond Basis (Non-Aggregated)

Bond-level implied arbitrage returns from CDS and corporate bond markets.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Bond CUSIP |
| ds | Date |
| y | Implied risk-free rate (percent) |

### Data Sources

- Markit CDS data from WRDS
- Corporate bond data from Open Source Bond Asset Pricing (openbondassetpricing.com)



## DataFrame Glimpse

```
Rows: 532356
Columns: 3
$ unique_id          <cat> 988498AR2
$ ds        <datetime[ns]> 2023-11-30 00:00:00
$ y                  <f64> 4.7417995836925755


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_cds_bond_basis_non_aggregated                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_cds_bond_basis_non_aggregated](../dataframes/SE/ftsfr_cds_bond_basis_non_aggregated.md)                                       |
| Data Sources                   | WRDS Markit, Open Source Bond Asset Pricing                                        |
| Data Providers                 | WRDS, openbondassetpricing.com                                      |
| Links to Providers             | https://wrds-www.wharton.upenn.edu, https://openbondassetpricing.com                             |
| Topic Tags                     | Cds, Bonds, Arbitrage, Basis, Fixed Income, Credit                                          |
| Type of Data Access            | WRDS,Public                                  |
| How is data pulled?            | Markit CDS from WRDS, bonds from Open Source Bond Asset Pricing                                                    |
| Data available up to (min)     | 2023-11-30 00:00:00                                                             |
| Data available up to (max)     | 2023-11-30 00:00:00                                                             |
| Dataframe Path                 | /Users/flavio/GitHub/p12_siriwardane_sunderam_wallen_2023/_data/ftsfr_cds_bond_basis_non_aggregated.parquet                                                   |


**Linked Charts:**

- None


## Pipeline Manifest

| Pipeline Name                   | p12_siriwardane_sunderam_wallen_2023                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [SE](../index.md)              |
| Lead Pipeline Developer         | Michelacci and Ferreira             |
| Contributors                    | Michelacci and Ferreira           |
| Git Repo URL                    | https://github.com/JacopoMichelacci/p12_siriwardane_sunderam_wallen_2023                        |
| Pipeline Web Page               | <a href="file:///Users/flavio/GitHub/p12_siriwardane_sunderam_wallen_2023/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-02-16 11:46:22           |
| OS Compatibility                |  |
| Linked Dataframes               |  [SE:ftsfr_cds_bond_basis_aggregated](../dataframes/SE/ftsfr_cds_bond_basis_aggregated.md)<br>  [SE:ftsfr_cds_bond_basis_non_aggregated](../dataframes/SE/ftsfr_cds_bond_basis_non_aggregated.md)<br>  |


