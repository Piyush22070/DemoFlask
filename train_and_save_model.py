from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
import joblib

# Generate dummy binary classification data with 2 total features
X, y = make_classification(
    n_samples=100,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    random_state=42
)

# Train a simple model
model = LogisticRegression()
model.fit(X, y)

# Save the model to a .pkl file
joblib.dump(model, "models/model.pkl")

print("Model saved to models/model.pkl")
