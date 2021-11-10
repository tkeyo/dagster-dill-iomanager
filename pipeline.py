from dagster import op, job, io_manager
import pandas as pd

from my_io_manager import DillIOManager


@io_manager
def dill_io_manager(_):
    """Gets the DillIOManager."""
    return DillIOManager()


@op
def download_cereals() -> pd.DataFrame:
    """Loads the cereals DataFrame."""
    return pd.read_csv("https://docs.dagster.io/assets/cereal.csv")


@op
def find_highest_calorie_cereal(df: pd.DataFrame) -> pd.DataFrame:
    """Sorts the DataFrame"""
    return df.sort_values("calories")


@op
def print_top_three_values(df: pd.DataFrame) -> None:
    """Prints top 3 values of a DataFrame."""
    print(df[:3])


@job(resource_defs={"io_manager": dill_io_manager})
def cereals_job():
    """Full cereal pipeline."""

    cereals = download_cereals()
    sorted_df = find_highest_calorie_cereal(cereals)
    print_top_three_values(sorted_df)


if __name__ == "__main__":
    result = cereals_job.execute_in_process()
    print("FINISHED")
