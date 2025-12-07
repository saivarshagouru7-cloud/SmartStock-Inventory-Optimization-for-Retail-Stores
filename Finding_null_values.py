import pandas as pd
import numpy as np
import os

def check_null_values(df):
    if df.isnull().any().any():
        print("Null values found.")
        print(df.isnull().sum())
    else:
        print("No null values found.")
DATA_PATH = os.path.join(os.path.dirname(__file__), "smart-stock.csv")
df = pd.read_csv(DATA_PATH, on_bad_lines='skip')
print(df)
check_null_values(df)