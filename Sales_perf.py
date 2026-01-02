import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sales_data_100k.csv')

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nInfo:")
df.info()

print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

### PHASE 1 COMPLETED ###

df['profit'] = df['sales'] - df['cost']

print("\nProfit stats:")
print(df['profit'].describe())

print("\nLoss :")
print(df[df['profit'] < 0].head())

print("\nZero-profit :")
print(df[df['profit'] == 0].head())

## PHASE 2 COMPLETED ##

Top_profit = df.groupby('product')[['sales', 'profit']].sum()

Top_profit['Profit_margin%'] = (
    Top_profit['profit'] / Top_profit['sales']
    ) * 100
print(Top_profit)

Top_profit = Top_profit.sort_values(
    by='profit', ascending=False
    )

print(Top_profit)

## PHASE 3 COMPLETED    

region_summary = (
    df.groupby("region")
      .agg(
          total_sales=("sales", "sum"),
          total_profit=("profit", "sum")
      )
)

region_summary['avg_profit_region'] = (
    region_summary['total_profit'] / region_summary['total_sales'] 
) * 100

region_summary = region_summary.sort_values(
    by='total_profit', ascending=False
)

print(region_summary)

#Phase 4 completed