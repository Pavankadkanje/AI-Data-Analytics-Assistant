import streamlit as st
import pandas as pd

from utils.ml_models import train_model


def show():

    st.title("📉 Prediction")

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

    if st.button("Train Model"):

        model, r2, mae, rmse = train_model(numeric, target)

        st.success("✅ Model Trained Successfully!")

        col1, col2, col3 = st.columns(3)

        col1.metric("R² Score", round(r2, 3))
        col2.metric("MAE", round(mae, 3))
        col3.metric("RMSE", round(rmse, 3))