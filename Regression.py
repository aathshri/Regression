
# Regression Project
# A simple Linear Regression model

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data
X = [[1], [2], [3], [4], [5]]
y = [10, 20, 30, 40, 50]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make a prediction
value = 6
prediction = model.predict([[value]])

print("LINEAR REGRESSION PROJECT")
print("-------------------------")
print("Input value:", value)
print("Predicted value:", round(prediction[0], 2))
print("Model coefficient:", round(model.coef_[0], 2))
print("Model intercept:", round(model.intercept_, 2))

# Plot the data and regression line
plt.scatter(X, y, label="Actual data")
plt.plot(X, model.predict(X), label="Regression line")
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Linear Regression")
plt.legend()
plt.show()
