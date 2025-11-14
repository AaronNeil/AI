import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
import joblib


# Load data
df = pd.read_csv('data/training_data.csv')

# Features and target
features = ['attack', 'defense', 'hp', 'sp_attack', 'sp_defense', 'speed']  # adjust as needed
target = 'type1'

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Initialize base Random Forest model
rf = RandomForestClassifier(random_state=42)

# Define hyperparameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

# Setup GridSearchCV with 5-fold cross-validation
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid,
                           cv=5, n_jobs=-1, verbose=2, scoring='accuracy')

# Run grid search
grid_search.fit(X_train, y_train)

# Best parameters from tuning
print("Best parameters found:", grid_search.best_params_)

# Evaluate best estimator on test set
model = grid_search.best_estimator_
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, 'model/pokemon_type_predictor.joblib')
print("Model and reference data saved in 'model/' folder")
