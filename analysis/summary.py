import pandas as pd

def identify_poor_performers(df: pd.DataFrame, bottom_n: int = 2) -> pd.DataFrame:
    df = df.copy()

    poor_performers = (
        df.sort_values(["week", "weekly_change_pct"])
          .groupby("week")
          .head(bottom_n)
    )

    poor_performers["poor_performer"] = True

    return poor_performers
