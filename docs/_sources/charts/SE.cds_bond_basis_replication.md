---
date: 2026-02-16 11:46:22
tags: WRDS Markit, Open Source Bond Asset Pricing
category: Cds, Bonds, Arbitrage, Basis, Replication
---

# Chart: CDS-Bond Basis Replication
CDS-Bond basis measuring implied arbitrage returns by rating category

## Chart
```{raw} html
<iframe src="../_static/SE/cds_bond_basis_replication.html" height="500px" width="100%"></iframe>

<p style="text-align: center;">Sources: WRDS Markit, Open Source Bond Asset Pricing</p>
```
[Full Screen Chart](../download_chart/SE/cds_bond_basis_replication.html)





## CDS-Bond Basis Replication

This chart shows the implied risk-free rate from CDS-bond arbitrage trades, aggregated by rating category.

### Methodology

Based on Siriwardane, Sunderam, and Wallen's "Segmented Arbitrage" methodology.

### Interpretation

- Positive values indicate arbitrage opportunity
- Investment Grade vs High Yield comparison shows relative opportunities



## Chart Specs

| Chart Name             | CDS-Bond Basis Replication                                             |
|------------------------|------------------------------------------------------------|
| Chart ID               | cds_bond_basis_replication                                               |
| Topic Tags             | Cds, Bonds, Arbitrage, Basis, Replication                                |
| Data Series Start Date |                                  |
| Data Frequency         |                                          |
| Observation Period     |                                      |
| Lag in Data Release    |                                     |
| Data Release Timing    |                                     |
| Seasonal Adjustment    |                                     |
| Units                  |                                                   |
| HTML Chart             | [HTML](../download_chart/SE/cds_bond_basis_replication.html)    |


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
| Data available up to (min)     |                                                              |
| Data available up to (max)     |                                                              |
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

