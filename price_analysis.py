import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter

# Load and preprocess data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Analyze prices for given items
def analyze_prices(df, items_to_analyze):
    results = []
    for item in items_to_analyze:
        filtered_df = df[df['Item'] == item]
        if filtered_df.empty:
            results.append(f"No data available for '{item}'.")
            continue

        best_day = filtered_df.loc[filtered_df['Current Price'].idxmin()]
        filtered_df['Week'] = filtered_df['Date'].dt.isocalendar().week
        weekly_data = filtered_df.groupby('Week').agg(
            Avg_Price=('Current Price', 'mean'),
            Start_Date=('Date', 'min')
        )
        best_week = weekly_data['Avg_Price'].idxmin()
        best_week_data = weekly_data.loc[best_week]

        results.append(
            f"--- Analysis for '{item}' ---\n"
            f"Best time to buy: {best_day['Date'].date()} at ${best_day['Current Price']:.2f}\n"
            f"Best week to buy: Week {best_week}, starting on {best_week_data['Start_Date'].date()}, "
            f"with an average price of ${best_week_data['Avg_Price']:.2f}\n"
        )
    return results

# Calculate volatility
def calculate_volatility(df):
    return df.groupby('Item')['Current Price'].std()

# Calculate descriptive statistics
def calculate_statistics(df):
    stats = df.groupby('Item')['Current Price'].agg(
        Mean='mean',
        Median='median'
    ).reset_index()
    modes = df.groupby('Item')['Current Price'].agg(lambda x: x.mode().iloc[0])
    stats['Mode'] = stats['Item'].map(modes)
    return stats

# Identify patterns
def identify_patterns(df):
    df['Rolling Avg'] = df.groupby('Item')['Current Price'].transform(lambda x: x.rolling(window=7, min_periods=1).mean())
    return df

# Highlight high volatility items
def highlight_high_volatility(volatility, threshold):
    high_volatility_items = volatility[volatility > threshold].index
    return list(high_volatility_items)

# Plot data
def plot_price_trends(df, unique_items, output_path):
    plt.figure(figsize=(10, 6))
    for item in unique_items:
        item_data = df[df['Item'] == item]
        plt.plot(item_data['Date'], item_data['Current Price'], label=item)

        # Annotate best day
        best_day = item_data.loc[item_data['Current Price'].idxmin()]
        plt.annotate(
            f"${best_day['Current Price']:.2f}",
            xy=(best_day['Date'], best_day['Current Price']),
            xytext=(10, -10),
            textcoords="offset points",
            arrowprops=dict(arrowstyle="->", color='red')
        )

    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.title('Price Trends Over Time')
    plt.legend()
    plt.gca().xaxis.set_major_locator(MonthLocator())
    plt.gca().xaxis.set_major_formatter(DateFormatter('%b %Y'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.show()

# Main function
def main():
    file_path = "price_data_all_items.csv"
    output_path = "prices_trends.png"
    df = load_data(file_path)

    unique_items = df['Item'].unique()
    print("Unique items:", unique_items)

    price_volatility = calculate_volatility(df)
    print("Price Volatility (Standard Deviation):")
    print(price_volatility)

    stats = calculate_statistics(df)
    print("Descriptive Statistics:")
    print(stats)

    threshold = 5  # Define a threshold for high volatility
    high_volatility_items = highlight_high_volatility(price_volatility, threshold)
    print("High Volatility Items:", high_volatility_items)

    analysis_results = analyze_prices(df, unique_items)
    for result in analysis_results:
        print(result)

    df = identify_patterns(df)
    plot_price_trends(df, unique_items, output_path)

if __name__ == "__main__":
    main()
