import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "smart-stock.csv")
df = pd.read_csv(DATA_PATH, on_bad_lines='skip')
print(df['sales'].agg(['mean','min','max','count','sum']))
 
 