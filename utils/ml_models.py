from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)


def train_model(df, target):

    X = df.drop(columns=[target])
    y = df[target]

    # Keep only numeric features
    X = X.select_dtypes(include="number")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(random_state=42)

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    # Evaluation Metrics
    r2 = r2_score(y_test, prediction)
    mae = mean_absolute_error(y_test, prediction)
    rmse = mean_squared_error(y_test, prediction) ** 0.5

    return model, r2, mae, rmse