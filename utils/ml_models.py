from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from xgboost import XGBRegressor

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

import pandas as pd


def train_model(df, target, model_name, test_size):

    X = df.drop(columns=[target])
    y = df[target]

    # Keep only numeric columns
    X = X.select_dtypes(include="number")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=42
    )

    # Model Selection
    if model_name == "Linear Regression":
        model = LinearRegression()

    elif model_name == "Decision Tree":
        model = DecisionTreeRegressor(random_state=42)

    elif model_name == "Random Forest":
        model = RandomForestRegressor(random_state=42)

    elif model_name == "XGBoost":
        model = XGBRegressor(random_state=42)

    else:
        raise ValueError("Invalid model selected")

    # Train
    model.fit(X_train, y_train)

    # Predict
    prediction = model.predict(X_test)

    # Metrics
    r2 = r2_score(y_test, prediction)
    mae = mean_absolute_error(y_test, prediction)
    mse = mean_squared_error(y_test, prediction)
    rmse = mse ** 0.5

    # Feature Importance
    importance = None

    if hasattr(model, "feature_importances_"):
        importance = pd.DataFrame({
            "Feature": X.columns,
            "Importance": model.feature_importances_
        })

        importance = importance.sort_values(
            by="Importance",
            ascending=False
        )

    return model, r2, mae, mse, rmse, importance