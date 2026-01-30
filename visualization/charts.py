import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def plot_price_trend(df, company: str):
    company_df = df[df["company"] == company]

    plt.figure()
    plt.plot(company_df["week"], company_df["price"], marker="o")
    plt.title(f"{company} Price Trend")
    plt.xlabel("Week")
    plt.ylabel("Price")
    plt.grid(True)
    
    output_path = f"data/processed/{company}_trend.png"
    plt.savefig(output_path)
    plt.close()