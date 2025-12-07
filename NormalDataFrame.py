import pandas as pd
import numpy as np
df = pd.DataFrame({'Item':['soap','book','pen','bag'],
                   'Quantity':[12,np.nan,54,65],
                   'price':[10,15,5,100],
                   'sales':[10,29,np.nan,233]})
print("After fill the null with forward mean for quantity:\n",df['Quantity'].fillna(18))
df['sales'].fillna(method='ffill',inplace=True)
print("After fill the null with forward mean for sales:\n",df['sales'])
print(df.query('sales > 20'))
print(df['sales'].agg(['min','max','sum','mean','sort']))
sorted_df = df.sort_values(by= 'price',ascending=False)
print("sorted data of price in dataframe:\n",sorted_df)


