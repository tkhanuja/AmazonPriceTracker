Project Overview and Benefits:
This project analyzes the price volatility and trends of two items—an Epomaker keyboard and a Gym Bag—to help consumers make informed purchasing decisions. By identifying the best times to buy based on historical price data, this analysis empowers consumers to purchase specific items at the lowest prices. It also provides insights into market behavior, which can be valuable for understanding pricing patterns across different product categories.
Data Description and Origins:
The analysis is based on a dataset of prices collected starting in September 2024. The dataset includes price information for the Epomaker keyboard and Gym Bag, with dates and prices. The data was scraped daily using an Amazon price tracker tool. The key variables considered in this analysis are the price, date, and item name.



Price Analysis Insights:
1. Unique Items Analyzed:
Epomaker Keyboard
Gym Bag
2. Price Volatility (Standard Deviation):
Epomaker Keyboard: 5.88
Gym Bag: 0.51
The Epomaker keyboard shows high price volatility, meaning its price fluctuates more frequently than the Gym Bag, which has a relatively stable price.
3. Descriptive Statistics:
Epomaker Keyboard:
Average Price: $91.17
Median Price: $94.04
Most Frequent Price: $95.00
Gym Bag:
Average Price: $33.72
Median Price: $34.00
Most Frequent Price: $34.00
The Epomaker keyboard has a higher average price, but its price distribution is more spread out, which aligns with its higher volatility.
4. High Volatility Item:
Epomaker Keyboard is identified as an item with high price volatility.

Detailed Item Analysis:
Epomaker Keyboard:
Best time to buy: September 2, 2024, at $71.46
Best week to buy: Week 35 (starting on September 1, 2024), with an average price of $73.60
Gym Bag:
Best time to buy: November 24, 2024, at $32.28
Best week to buy: Week 35 (starting on September 1, 2024), with an average price of $32.46

Key Insights from the Data:
Seasonality and Best Time to Buy:
Both items showed their lowest prices during Week 35/52 (September 1-7, 2024). However, this is based on data starting from September, which means the price may have been lower earlier in the year.
For the Epomaker keyboard, the price has been increasing over the period analyzed, suggesting that it may be wise to purchase soon before it potentially rises further.
The Gym Bag price has remained stable throughout the analysis, with slight variation.
Need for Additional Historical Data:
The current data only covers the period starting from September, and there could have been fluctuations earlier in the year that might provide additional context. For instance, if prices have been rising steadily for an extended period, purchasing soon could be beneficial for volatile items like the keyboard.
Industry-Wide Trends:
It would be insightful to compare the price patterns of similar items (e.g., other keyboards) to see if this trend of rising prices is widespread in the industry. If it is, it could be due to factors such as supply chain issues, increased demand, or competition among brands.
The price behavior of the Gym Bag, which has remained stable, could indicate that price increases in other industries (like electronics) may not have the same impact on categories like bags and accessories.

Follow-up Questions:
How long have prices been increasing for the Epomaker Keyboard? If the price increase has been prolonged, it may indicate that waiting longer could lead to higher prices, and buying sooner might be the better option.
Are other items in the same category experiencing similar price increases? This could reveal trends in specific markets, like keyboards or electronics, and might be influenced by factors such as competition, material costs, or changes in consumer demand.

In conclusion, while we’ve identified the best times to buy based on the data available, further historical data and comparison with similar items would provide a clearer picture of whether these price trends are consistent across categories and time periods.


Steps Taken in the Process:
Writing the Amazon Price Tracker:
Tool Setup: The project began with creating a web scraper to collect real-time price data from Amazon listings. This scraper was designed to track price fluctuations of specific products by pulling data from product pages on Amazon.
Data Collection: The scraper was scheduled to collect price information daily to create a time series of prices for the tracked products.
Storage: The collected data was saved into a csv file for easy access and analysis. Each entry included product details like name, price, and the date of the price capture.
Data Preprocessing:
Cleaning the Data: The raw data collected by the scraper was cleaned and preprocessed to ensure accuracy. This included removing missing price values, removing duplicate entries, and ensuring the data was in the correct format (e.g., converting dates into a consistent format).
Analyzing the Data:
Price Volatility: Calculations for price volatility were performed using standard deviation to measure the fluctuation of prices over time for both products.
Descriptive Statistics: Key statistics like mean, median, and mode of prices were calculated to understand the price distribution and trends.
Identifying Best Times to Buy: The analysis identified the lowest prices for each product, as well as the weeks with the most favorable average prices. This was done by comparing the historical price data and identifying the optimal times to purchase.
Visualizing the Data:
Price Trends: Graphs were generated to visualize how prices fluctuated over time for each product. These visuals helped highlight significant price trends.
Volatility Comparison: A comparison of price volatility between the two products was visualized to emphasize the stability of the Gym Bag versus the Epomaker keyboard.
Best Times to Buy: Visuals were created to show the best days to buy the products at the lowest prices.
Conclusion and Reporting:
Synthesizing Findings: The results of the data analysis were summarized in a factual, objective manner. Key insights were drawn about price trends, volatility, and the best times to buy.
Actionable Insights: Recommendations were made based on the analysis, advising consumers on when to purchase each product for the best value.


Usage:
Add .env file 
EMAIL_ADDRESS= "your email"
EMAIL_PASSWORD= "your password"


Go to your Google Account's Security settings.
Enable 2-Step Verification.
Once 2-Step Verification is enabled, go to the App passwords section.
Generate an app password for your application (e.g., name it "Amazon Price Tracker").
Use this app password in your .env file instead of your regular email password.# AmazonPriceTracker
