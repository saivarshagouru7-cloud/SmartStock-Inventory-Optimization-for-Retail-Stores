import numpy as np
import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "smart-stock.csv")
data = pd.read_csv(DATA_PATH, on_bad_lines='skip')
print("data :\n")
print(data.head(2))
print(data.isnull().sum())
print(data.describe())
 
data.columns=data.columns.str.strip().str.lower().str.replace(" ","_")

col_to_clean=['sales']

data['sales']=(

    data['sales'].replace([""," ","NA","N/A"],np.nan)

)


data['sales']=pd.to_numeric(data['sales'],errors='coerce')
 
data['sales']=data['sales'].fillna(0).astype(int)
 
print(data.columns)

print(data['sales'].head(5))
 
print(data.count())
 