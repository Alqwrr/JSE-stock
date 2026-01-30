import pandas as pd

def load_prices(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def calculate_weekly_change(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(["company", "week"])
    df["weekly_change_pct"] = (
        df.groupby("company")["price"].pct_change() * 100
    )
    return df

def calculate_cumulative_change(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["cumulative_change_pct"] = (
        df.groupby("company")["weekly_change_pct"]
          .cumsum()
    )

    return df
