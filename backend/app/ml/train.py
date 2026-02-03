import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import os

# Create dummy data (3 features)
X = np.random.rand(100, 3)
y = np.random.randint(0, 2, 100)

model = RandomForestClassifier()
model.fit(X, y)

# Ensure directory exists
os.makedirs("app/ml", exist_ok=True)

# Save model
output_path = "app/ml/model.pkl"
joblib.dump(model, output_path)
print(f"Model saved to {output_path}")
