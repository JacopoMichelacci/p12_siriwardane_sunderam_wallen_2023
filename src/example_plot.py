from pathlib import Path

from settings import config

OUTPUT_DIR = Path(config("OUTPUT_DIR"))

import seaborn as sns
from matplotlib import pyplot as plt

sns.set()

# Placeholder for future data pull:
# import pull_fred
# DATA_DIR = Path(config("DATA_DIR"))
# df = pull_fred.load_fred(data_dir=DATA_DIR)
# (
#     100
#     * df[["CPIAUCNS", "GDPC1"]]
#     .rename(columns={"CPIAUCNS": "Inflation", "GDPC1": "Real GDP"})
#     .dropna()
#     .pct_change(4)
# ).plot()
# plt.title("Inflation and Real GDP, Seasonally Adjusted")
# plt.ylabel("Percent change from 12-months prior")
# filename = OUTPUT_DIR / "example_plot.png"
# plt.savefig(filename)
