import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load cleaned data
df = pd.read_csv("data/clean/superstore_clean.csv")

# Create target variable: 1 if profitable, 0 if not
df["Is_Profitable"] = (df["Profit"] > 0).astype(int)

# Features and target
features = ["Sales", "Quantity", "Discount"]
X = df[features]
y = df["Is_Profitable"]

# Split into training and testing sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

print("\nFeature Importances:")
for f, imp in zip(features, model.feature_importances_):
    print(f"  {f}: {round(imp*100, 1)}%")