from analysis.performance import load_prices, calculate_weekly_change, calculate_cumulative_change
from analysis.ranking import rank_stocks_by_week
from analysis.summary import identify_poor_performers
from analysis.confidence import calculate_confidence_score
from analysis.trends import determine_trend
from visualization.charts import plot_price_trend
from analysis.context import score_headlines
from scraper.news_scraper import fetch_headlines
from scraper.moneyweb_scraper import fetch_moneyweb_headlines
import time

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
    biggest_risers = []
    avoid = []
    confidence_scores = []

    print("\nAnalysis:\n")
    for company in latest_df["company"].unique():


        trend = latest_df[latest_df["company"] == company]["trend_direction"].iloc[0]

        weekly_pct_change = latest_df[latest_df["company"] == company]["weekly_change_pct"].iloc[0].round(1)
        cumulative_pct_change = latest_df[latest_df["company"] == company]["cumulative_change_pct"].iloc[0].round(1)

        headlines = fetch_headlines(f'{company}+South+Africa+investors')
        sentiment_score = score_headlines(headlines)

        moneyweb = fetch_moneyweb_headlines(f'{company}')
        sentiment_score2 = score_headlines(moneyweb)

        is_poor = company in poor_latest
        confidence_score = calculate_confidence_score(sentiment_score,sentiment_score2,weekly_pct_change,cumulative_pct_change)

        
        
        if confidence_score > 20:
            recommendations.append(company)

        if trend == "Up":
            biggest_risers.append(company)

            
        if is_poor and confidence_score < 10:
            avoid.append(company)

        print(f"{company}")
        print(f"  Trend: {trend}")
        print(f"  Bing Search Sentiment Score: {sentiment_score}")
        print(f"  MoneyWeb Sentinemt Score: {sentiment_score2}")
        print(f"  Poor Performer last Week: {is_poor}")
        print(f"  weekly % change: {weekly_pct_change}")
        print(f"  cumulative % change: {cumulative_pct_change}")
        print()
        print(f"  confidence score: {confidence_score}")
        print()
        print()
        time.sleep(2.5)

    print("Recommended Stocks for Monday:")
    for stock in recommendations:
        print(f"- {stock}")

    print("less Sure Stocks for Monday:")
    for stock in avoid:
        print(f"- {stock}")

    for company in df["company"].unique():
        plot_price_trend(df, company)

    if len(biggest_risers) > 2:
        print(f"  Biggest 3 risers this Week: {biggest_risers[0]},{biggest_risers[1]},{biggest_risers[2]}")
    elif len(biggest_risers) == 2:
        print(f"  Biggest 2 risers this Week: {biggest_risers[0]},{biggest_risers[1]}")
    elif len(biggest_risers) == 1:
        print(f"  Only riser this Week: {biggest_risers[0]}")
    else:
        print("   no stock price rose")


    df.to_csv(OUTPUT_PATH, index=False)
    

if __name__ == "__main__":
    main()
