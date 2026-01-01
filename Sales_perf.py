import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sales_data_100k.csv')


print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nData Info:")
df.info()

print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nProfit summary:")
df['profit'] = df['sales'] - df['cost']
print(df['profit'].describe())

print("\nSample losses:")
print(df[df['profit'] < 0].head())

print("\nZero profit rows:")
print(df[df['profit'] == 0].head())

