import pandas as pd

def determine_trend(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    df = df.copy()

    df["moving_avg"] = (
        df.groupby("company")["price"]
          .rolling(window=window)
          .mean()
          .reset_index(level=0, drop=True)
    )

    df["trend_direction"] = "Flat"

    df.loc[df["price"] > df["moving_avg"], "trend_direction"] = "Up"
    df.loc[df["price"] < df["moving_avg"], "trend_direction"] = "Down"

    return df
