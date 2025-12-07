import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.DataFrame({
    "Land_area" :["1000","1500","2000","2500","3000"],
    "price":[10,15,18,22,27]
})
x = data[["Land_area"]]
y = data[["price"]]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
model= LinearRegression()
model.fit(x_train,y_train)
pred = model.predict(x_test)
print("Predictiom Prices:",pred)
print("Actual Prices:",y_test.values)
new_land_area = [[2800]]
new_price = model.predict(new_land_area)