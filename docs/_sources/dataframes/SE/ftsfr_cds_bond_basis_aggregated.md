# Dataframe: `SE:ftsfr_cds_bond_basis_aggregated` - ftsfr_cds_bond_basis_aggregated

## CDS-Bond Basis (Aggregated)

Measures the implied arbitrage return from CDS and corporate bond markets, aggregated by rating category.

### Columns

| Column | Description |
|--------|-------------|
| unique_id | Rating category (Investment Grade, High Yield) |
| ds | Date |
| y | Implied risk-free rate (percent) |

### Methodology

Based on Siriwardane, Sunderam, and Wallen's "Segmented Arbitrage":

CDS Basis:
$$
CB_{i, t, \tau} = CDS_{i, t, \tau} - FR_{i, t, \tau}
$$

Implied Risk-Free Rate:
$$
rfr^{CDS}_{i, t, \tau} = y_{t, \tau} - CB_{i, t, \tau}
$$

### Interpretation

- Negative CB: Investor could earn arbitrage profit by going long bond + buying CDS protection
- Positive rfr indicates positive arbitrage opportunity



## DataFrame Glimpse

```
Rows: 368
Columns: 3
$ unique_id          <str> 'Investment Grade'
$ ds        <datetime[ns]> 2023-11-30 00:00:00
$ y                  <f64> 6.191714845203802


```

## Dataframe Manifest

| Dataframe Name                 | ftsfr_cds_bond_basis_aggregated                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [ftsfr_cds_bond_basis_aggregated](../dataframes/SE/ftsfr_cds_bond_basis_aggregated.md)                                       |
| Data Sources                   | WRDS Markit, Open Source Bond Asset Pricing                                        |
| Data Providers                 | WRDS, openbondassetpricing.com                                      |
| Links to Providers             | https://wrds-www.wharton.upenn.edu, https://openbondassetpricing.com                             |
| Topic Tags                     | Cds, Bonds, Arbitrage, Basis, Fixed Income, Credit                                          |
| Type of Data Access            | WRDS,Public                                  |
| How is data pulled?            | Markit CDS from WRDS, bonds from Open Source Bond Asset Pricing                                                    |
| Data available up to (min)     | 2023-11-30 00:00:00                                                             |
| Data available up to (max)     | 2023-11-30 00:00:00                                                             |
| Dataframe Path                 | /Users/flavio/GitHub/p12_siriwardane_sunderam_wallen_2023/_data/ftsfr_cds_bond_basis_aggregated.parquet                                                   |


**Linked Charts:**


- [SE:cds_bond_basis_replication](../../charts/SE.cds_bond_basis_replication.md)



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


