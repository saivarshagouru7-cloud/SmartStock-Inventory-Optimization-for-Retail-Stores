import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    "Age": [5, 10, 12, 15, 18, 20, 25, 30, 40, 50, 60, 70, 80, 90],
    "Height": [11.0, 13.5, 14.8, 16.5, 17.2, 17.5, 17.6, 17.7, 17.7, 17.7, 17.6, 17.5, 17.4, 17.3]
})
x = data[["Age"]]
y = data[["Height"]]
x_train, x_test, y_train, y_test =train_test_split(x,y,test_size=0.3)
model = LinearRegression()
model.fit(x_train, y_train)
pred = model.predict(x_test)
print("Predicted Heights:", pred)
print("Actual Heights:", y_test.values)
new_age = [[47]]
predicted_height = model.predict(new_age)
print("Prediction for Age 33:", predicted_height)

