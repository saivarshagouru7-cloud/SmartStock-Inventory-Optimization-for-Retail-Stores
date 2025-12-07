import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "smart-stock.csv")
df = pd.read_csv(DATA_PATH, on_bad_lines='skip')
print( df)

print(df.sort_values(by=df.columns[0]))

print( "sorting values in decending order:\n",df.sort_values(by='sales', ascending=False))

print("Quanty of having more than 30:\n" ,df[df['Quantity in Stock'] < 30])

print( df[(df['Price'] >= 100) & (df['Price'] <= 1000)])

