import plotly.express as px
import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "smart-stock.csv")
df = pd.read_csv(DATA_PATH, on_bad_lines='skip')
print(df)
#line chart
fig = px.line(
    df,
    x="Product ID",
    y="Price",
    title="Plotly Representation of Line Plot"
)
fig.show()

#pie chart
fig = px.pie(df,names="Product ID",values="Price",title="plotly representaion of pie chart")
fig.show()
#dounut
fig = px.pie(df,names="Product ID",values="Price",title="plotly representaion of dounut chart",hole=0.5)
fig.show()
#bar chart
fig = px.bar(
    df,
    x="Product ID",
    y="Price",
    title="Plotly Representation of Bar chart"
)
fig.show()



