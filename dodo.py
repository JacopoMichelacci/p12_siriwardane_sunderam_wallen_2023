"""
Doit build file for CDS-Bond Basis pipeline.

Run with: doit
"""

import shutil
from os import environ, getcwd, path
from pathlib import Path
import sys

sys.path.insert(1, "./src/")

from colorama import Fore, Style, init
from doit.reporter import ConsoleReporter
from settings import config


try:
    in_slurm = environ["SLURM_JOB_ID"] is not None
except:
    in_slurm = False


class GreenReporter(ConsoleReporter):
    def write(self, stuff, **kwargs):
        doit_mark = stuff.split(" ")[0].ljust(2)
        task = " ".join(stuff.split(" ")[1:]).strip() + "\n"
        output = (
            Fore.GREEN
            + doit_mark
            + f" {path.basename(getcwd())}: "
            + task
            + Style.RESET_ALL
        )
        self.outstream.write(output)


if not in_slurm:
    DOIT_CONFIG = {
        "reporter": GreenReporter,
        # other config here...
        # "cleanforget": True, # Doit will forget about tasks that have been cleaned.
        "backend": "sqlite3",
        "dep_file": "./.doit-db.sqlite",
    }
else:
    DOIT_CONFIG = {"backend": "sqlite3", "dep_file": "./.doit-db.sqlite"}
init(autoreset=True)


BASE_DIR = config("BASE_DIR")
DATA_DIR = config("DATA_DIR")
MANUAL_DATA_DIR = config("MANUAL_DATA_DIR")
OUTPUT_DIR = config("OUTPUT_DIR")
OS_TYPE = config("OS_TYPE")
USER = config("USER")

## Helpers for handling Jupyter Notebook tasks
environ["PYDEVD_DISABLE_FILE_VALIDATION"] = "1"

# fmt: off
## Helper functions for automatic execution of Jupyter notebooks
def jupyter_execute_notebook(notebook_path):
    return f"jupyter nbconvert --execute --to notebook --ClearMetadataPreprocessor.enabled=True --inplace {notebook_path}"
def jupyter_to_html(notebook_path, output_dir=OUTPUT_DIR):
    return f"jupyter nbconvert --to html --output-dir={output_dir} {notebook_path}"
def jupyter_to_md(notebook_path, output_dir=OUTPUT_DIR):
    """Requires jupytext"""
    return f"jupytext --to markdown --output-dir={output_dir} {notebook_path}"
def jupyter_clear_output(notebook_path):
    """Clear the output of a notebook"""
    return f"jupyter nbconvert --ClearOutputPreprocessor.enabled=True --ClearMetadataPreprocessor.enabled=True --inplace {notebook_path}"
# fmt: on


def mv(from_path, to_path):
    """Move a file to a folder"""
    from_path = Path(from_path)
    to_path = Path(to_path)
    to_path.mkdir(parents=True, exist_ok=True)
    if OS_TYPE == "nix":
        command = f"mv {from_path} {to_path}"
    else:
        command = f"move {from_path} {to_path}"
    return command


def copy_file(origin_path, destination_path, mkdir=True):
    """Create a Python action for copying a file."""

    def _copy_file():
        origin = Path(origin_path)
        dest = Path(destination_path)
        if mkdir:
            dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(origin, dest)

    return _copy_file


##################################
## Begin rest of PyDoit tasks here
##################################


def task_config():
    """Create empty directories for data and output if they don't exist"""
    return {
        "actions": ["ipython ./src/settings.py"],
        "targets": [DATA_DIR, OUTPUT_DIR],
        "file_dep": ["./src/settings.py"],
        "clean": [],
    }


notebook_tasks_cds = {
    "summary_cds_bond_basis_ipynb": {
        "path": "./src/summary_cds_bond_basis_ipynb.py",
        "file_dep": [
            DATA_DIR / "ftsfr_cds_bond_basis_aggregated.parquet",
            DATA_DIR / "ftsfr_cds_bond_basis_non_aggregated.parquet",
        ],
        "targets": [],
    },
}


def task_run_cds_notebooks():
    """Execute CDS-bond basis summary notebooks."""
    for notebook in notebook_tasks_cds.keys():
        pyfile_path = Path(notebook_tasks_cds[notebook]["path"])
        notebook_path = pyfile_path.with_suffix(".ipynb")
        yield {
            "name": notebook,
            "actions": [
                f"jupytext --to notebook --output {notebook_path} {pyfile_path}",
                jupyter_execute_notebook(notebook_path),
                jupyter_to_html(notebook_path),
                mv(notebook_path, OUTPUT_DIR),
            ],
            "file_dep": [
                pyfile_path,
                *notebook_tasks_cds[notebook]["file_dep"],
            ],
            "targets": [
                OUTPUT_DIR / f"{notebook}.html",
                *notebook_tasks_cds[notebook]["targets"],
            ],
            "clean": True,
            "task_dep": ["calc"],
        }

###############################################################
## Changes New
###############################################################


def task_pull_open_source_bond():
    """Pull Open Source Bond data (public)."""
    targets = [
        DATA_DIR / "treasury_bond_returns.parquet",
        DATA_DIR / "treasury_bond_returns_README.pdf",
        DATA_DIR / "corporate_bond_returns.parquet",
        DATA_DIR / "corporate_bond_returns_README.txt",
    ]
    return {
        "actions": ["python ./src/pull_open_source_bond.py"],
        "verbosity": 2,
        "task_dep": ["config"],
        "targets": targets,
        "uptodate": [lambda: all(t.exists() for t in targets)],
    }


def task_pull_markit_mapping():
    """Pull RED-ISIN mapping from WRDS."""
    targets = [
        DATA_DIR / "RED_and_ISIN_mapping.parquet",
    ]
    return {
        "actions": ["python ./src/pull_markit_mapping.py"],
        "verbosity": 2,
        "task_dep": ["config"],
        "targets": targets,
        "uptodate": [lambda: all(t.exists() for t in targets)],
    }


def task_pull_wrds_markit():
    """Pull Markit CDS data from WRDS."""
    targets = [
        DATA_DIR / "markit_cds.parquet",
        DATA_DIR / "markit_red_crsp_link.parquet",
        DATA_DIR / "markit_cds_subsetted_to_crsp.parquet",
    ]
    return {
        "actions": ["python ./src/pull_wrds_markit.py"],
        "verbosity": 2,
        "task_dep": ["config"],
        "targets": targets,
        "uptodate": [lambda: all(t.exists() for t in targets)],
    }


def task_calc():
    """Calculate CDS-bond basis and create FTSFR datasets."""
    return {
        "actions": ["python ./src/create_ftsfr_datasets.py"],
        "verbosity": 2,
        "task_dep": ["pull_open_source_bond", "pull_markit_mapping", "pull_wrds_markit"],
        "file_dep": [
            DATA_DIR / "corporate_bond_returns.parquet",
            DATA_DIR / "RED_and_ISIN_mapping.parquet",
            DATA_DIR / "markit_cds.parquet",
            BASE_DIR / "src" / "create_ftsfr_datasets.py",
            BASE_DIR / "src" / "merge_cds_bond.py",
            BASE_DIR / "src" / "process_final_product.py",
        ],
        "targets": [
            DATA_DIR / "ftsfr_cds_bond_basis_aggregated.parquet",
            DATA_DIR / "ftsfr_cds_bond_basis_non_aggregated.parquet",
        ],
    }


def task_generate_charts():
    """Generate interactive HTML charts."""
    return {
        "actions": ["python ./src/generate_chart.py"],
        "file_dep": [
            "./src/generate_chart.py",
            DATA_DIR / "ftsfr_cds_bond_basis_aggregated.parquet",
        ],
        "targets": [
            OUTPUT_DIR / "cds_bond_basis_replication.html",
        ],
        "verbosity": 2,
        "task_dep": ["calc"],
    }


def task_generate_pipeline_site():
    """Generate pipeline documentation site."""
    notebook_files = [
        Path(notebook_tasks_cds[notebook]["path"])
        for notebook in notebook_tasks_cds.keys()
    ]
    return {
        "actions": ["chartbook build -f"],
        "verbosity": 2,
        "task_dep": ["run_cds_notebooks", "generate_charts"],
        "file_dep": [
            BASE_DIR / "chartbook.toml",
            *notebook_files,
            OUTPUT_DIR / "cds_bond_basis_replication.html",
        ],
        "targets": [
            BASE_DIR / "docs" / "index.html",
        ],
    }
