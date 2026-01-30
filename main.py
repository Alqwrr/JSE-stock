from analysis.performance import load_prices, calculate_weekly_change, calculate_cumulative_change
from analysis.ranking import rank_stocks_by_week
from analysis.summary import identify_poor_performers
from analysis.trends import determine_trend
from visualization.charts import plot_price_trend
from analysis.context import score_headlines
from scraper.news_scraper import fetch_headlines

DATA_PATH = "data/raw/weekly_prices.csv"
OUTPUT_PATH = "data/processed/analysis_results.csv"

def main():
    df = load_prices(DATA_PATH)
    df = calculate_weekly_change(df)
    df = calculate_cumulative_change(df)
    df = rank_stocks_by_week(df)
    df = determine_trend(df)
    
    latest_week = df["week"].max()
    latest_df = df[df["week"] == latest_week]


    poor_df = identify_poor_performers(df)
    poor_latest = poor_df[poor_df["week"] == latest_week]["company"].tolist()

    recommendations = []

    print("\nFull Analysis:\n")
    for company in latest_df["company"].unique():
        trend = latest_df[latest_df["company"] == company]["trend_direction"].iloc[0]

        headlines = fetch_headlines(f'{company}+South+Africa+market')
        sentiment_score = score_headlines(headlines)
        print(headlines)
        print(sentiment_score)

        is_poor = company in poor_latest

        if trend == "Up" and not is_poor and sentiment_score >= 0:
            recommendations.append(company)

        print(f"{company}")
        print(f"  Trend: {trend}")
        print(f"  Sentiment Score: {sentiment_score}")
        print(f"  Poor Performer This Week: {is_poor}")
        print()

    print("Recommended Stocks for Monday:")
    for stock in recommendations:
        print(f"- {stock}")

    for company in df["company"].unique():
        plot_price_trend(df, company)

    df.to_csv(OUTPUT_PATH, index=False)
    

if __name__ == "__main__":
    main()
