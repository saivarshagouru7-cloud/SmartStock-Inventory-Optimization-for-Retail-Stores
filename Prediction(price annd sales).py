import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

DATA_PATH = os.path.join(os.path.dirname(__file__), "smart-stock.csv")
df = pd.read_csv(DATA_PATH, on_bad_lines='skip')

# Features and target
X = df[["Price"]]      
y = df[["sales"]]      

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions on test set 
y_pred = model.predict(X_test)

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape, "\n")

print("Test Data Shapes:")
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape, "\n")

print("Model Results:")
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("\nPredicted Sales for Test Data:")
print(y_pred)
price_value = float(input("\nEnter Price to predict sales: "))
new_X = pd.DataFrame({"Price": [price_value]})
predicted_sales = model.predict(new_X)
print(f"Predicted sales for Price {price_value}: {predicted_sales[0][0]}")


