import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("data/retail_inventory_sales.csv", parse_dates=["date"])
df["dayofweek"] = df["date"].dt.dayofweek
df["month"] = df["date"].dt.month
X = pd.get_dummies(df[["store_id","category","unit_price","promotion_flag","on_hand_units","lead_time_days","dayofweek","month"]], drop_first=True)
y = df["units_sold"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)
model = RandomForestRegressor(n_estimators=80, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, pred):.2f} units")
