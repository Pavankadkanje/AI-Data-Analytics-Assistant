import streamlit as st
import pandas as pd
import joblib

from utils.ml_models import train_model


def show():

    st.title("📈 Prediction")

    if st.session_state.df is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    df = st.session_state.df.copy()

    numeric = df.select_dtypes(include="number")

    if numeric.shape[1] < 2:
        st.warning("Need at least 2 numeric columns.")
        return

    target = st.selectbox(
        "Select Target Column",
        numeric.columns
    )

    model_name = st.selectbox(
        "Choose Model",
        [
            "Linear Regression",
            "Decision Tree",
            "Random Forest",
            "XGBoost"
        ]
    )

    test_size = st.slider(
        "Test Size",
        0.1,
        0.4,
        0.2
    )

    if st.button("Train Model"):

        model, r2, mae, mse, rmse, importance = train_model(
            numeric,
            target,
            model_name,
            test_size
        )

        st.success("✅ Model Trained Successfully!")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("R²", round(r2,3))
        c2.metric("MAE", round(mae,3))
        c3.metric("MSE", round(mse,3))
        c4.metric("RMSE", round(rmse,3))

        if importance is not None:
            st.subheader("Feature Importance")

            st.bar_chart(
                importance.set_index("Feature")
            )

        joblib.dump(model, "trained_model.pkl")

        with open("trained_model.pkl","rb") as f:

            st.download_button(
                "⬇ Download Model",
                f,
                file_name="trained_model.pkl"
            )