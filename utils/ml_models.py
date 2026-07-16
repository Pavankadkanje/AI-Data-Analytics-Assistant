from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


def train_model(df, target):

    X = df.drop(columns=[target])
    y = df[target]

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

    score = r2_score(y_test, prediction)

    return model, score