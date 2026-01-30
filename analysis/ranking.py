import pandas as pd

def rank_stocks_by_week(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["weekly_rank"] = (
        df.groupby("week")["weekly_change_pct"]
          .rank(ascending=False, method="min")
    )

    return df
