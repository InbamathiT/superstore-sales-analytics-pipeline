import pandas as pd
import sqlite3
import os

# Load cleaned data
df = pd.read_csv("data/clean/superstore_clean.csv")

os.makedirs("outputs", exist_ok=True)

# Create SQLite database and load data into a table
conn = sqlite3.connect("outputs/superstore.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

# Query 1: Top 5 products by total sales
q1 = """
SELECT Product_Name, ROUND(SUM(Sales), 2) AS Total_Sales
FROM sales
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 5
"""
df_q1 = pd.read_sql(q1, conn)
df_q1.to_csv("outputs/top5_products.csv", index=False)
print("Top 5 Products:")
print(df_q1)

# Query 2: Monthly sales and profit trend
q2 = """
SELECT STRFTIME('%Y-%m', Order_Date) AS Month,
       ROUND(SUM(Sales), 2) AS Monthly_Sales,
       ROUND(SUM(Profit), 2) AS Monthly_Profit
FROM sales
GROUP BY Month
ORDER BY Month
"""
df_q2 = pd.read_sql(q2, conn)
df_q2.to_csv("outputs/monthly_trend.csv", index=False)
print("\nMonthly Trend (first 5 rows):")
print(df_q2.head())

# Query 3: Region-wise performance
q3 = """
SELECT Region,
       ROUND(AVG(Sales), 2) AS Avg_Sales,
       ROUND(SUM(Profit), 2) AS Total_Profit,
       COUNT(*) AS Order_Count
FROM sales
GROUP BY Region
ORDER BY Total_Profit DESC
"""
df_q3 = pd.read_sql(q3, conn)
df_q3.to_csv("outputs/region_analysis.csv", index=False)
print("\nRegion Analysis:")
print(df_q3)

conn.close()
print("\n✓ All queries done. Results saved to outputs/")