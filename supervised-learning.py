# Step 1: Install Required Libraries
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required_packages = ["ucimlrepo", "pandas", "scikit-learn", "numpy"]

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)

from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# load dataset
student_performance = fetch_ucirepo(id=320)
X = student_performance.data.features
# students final grades
y = student_performance.data.targets['G3']

# Preprocess the dataset: encode categorical features and scale numerical features
X = pd.get_dummies(X, drop_first=True)
scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train and Evaluate Gradient Boosting Regressor
gb_model = GradientBoostingRegressor(random_state=42)
gb_model.fit(X_train, y_train)
y_pred_gb = gb_model.predict(X_test)

# Evaluate the model
#the average of the squared differences between the predicted values and the actual values
mse_gb = mean_squared_error(y_test, y_pred_gb)
#how much of the variation in the target variable is explained by the model
r2_gb = r2_score(y_test, y_pred_gb)
#the average of the absolute differences between predicted values and actual values.
mae_gb = mean_absolute_error(y_test, y_pred_gb)

print("Gradient Boosting Results:")
print(f"Mean Squared Error: {mse_gb:.2f}, R-squared: {r2_gb:.2f}, MAE: {mae_gb:.2f}")

# Step 6: Example Predictions
example_features = X_test.iloc[:10]
actual_grades = y_test.iloc[:10]
predicted_grades = gb_model.predict(example_features)

print("\n--- Example Predictions ---")
for i in range(len(example_features)):
    print(f"Student {i+1}: Predicted Final Grade = {predicted_grades[i]:.1f}, Actual Final Grade = {actual_grades.iloc[i]}")
