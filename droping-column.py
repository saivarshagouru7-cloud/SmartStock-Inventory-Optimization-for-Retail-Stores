import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "smart-stock.csv")
df = pd.read_csv(DATA_PATH, on_bad_lines='skip')
df = df.drop("Product Name",axis=1)
print(df)
sorted_df = df.sort_values(by= df.columns[2])
print(sorted_df)