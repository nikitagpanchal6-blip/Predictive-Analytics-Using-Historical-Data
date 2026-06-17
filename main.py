import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load Dataset
data = pd.read_csv("historical_data.csv")

# Features and Target
X = data[['Month']]
y = data['Sales']

# Train Model
model = LinearRegression()
model.fit(X, y)

# Predict Future Sales (Month 13)
future_month = [[13]]
prediction = model.predict(future_month)

print("Predicted Sales for Month 13:", prediction[0])

# Plot Graph
plt.scatter(X, y, label="Actual Sales")
plt.plot(X, model.predict(X), color='red', label="Regression Line")

plt.title("Predictive Analytics Using Historical Data")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

# Save Graph
plt.savefig("prediction_graph.png")

plt.show()
plt.figure(figsize=(8,5))
plt.bar(data['Month'], data['Sales'])
plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("monthly_sales.png")
plt.show()