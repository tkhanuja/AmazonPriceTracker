import pandas as pd
import datetime
import time
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#plot items for visualization

df = pd.read_csv("price_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Plot
plt.figure(figsize=(10, 6))

# Loop through unique items and plot each
for item in df['Item'].unique():
    item_data = df[df['Item'] == item]
    plt.plot(item_data['Date'], item_data['Current Price'], label=item)

# Formatting
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.title('Price Trends Over Time')
plt.legend()


# Format x-axis to show ticks at the start of each month
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.MonthLocator())
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
#are there any patterns in the price trend?
#What date was the best time to buy