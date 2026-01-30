# JSE Stock Monitor

A Python-based system for monitoring and analyzing weekly share price movements
for a school stock market challenge.

## Current Features
- Load weekly share prices
- Calculate weekly percentage changes

## Tech Stack
- Python 3.14
- pandas
- numpy

## Data Source
- Prices are provided by the school challenge

Methodology

Weekly prices provided by school are treated as ground truth

Performance metrics include percentage change, cumulative change, and rankings

Trend direction is derived using moving averages

External news headlines provide contextual sentiment only

Assumptions

News sentiment reflects short-term market perception

Trends persist briefly into the next trading period

Limitations

Estimates are not guaranteed predictions

Sentiment analysis is keyword-based

No real-time or intraday data

Ethical Considerations

No financial advice is given

No real trading or price manipulation

Public data only