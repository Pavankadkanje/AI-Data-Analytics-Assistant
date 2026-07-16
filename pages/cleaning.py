import streamlit as st
import pandas as pd

def show():

    st.title("🧹 Data Cleaning")

    if st.session_state.df is None:
        st.warning("⚠ Please upload a dataset first.")

    else:

        df = st.session_state.df.copy()

        # -----------------------------
        # Dataset Preview
        # -----------------------------
        st.markdown("## 📋 Current Dataset")
        st.dataframe(df.head(), use_container_width=True)

        # -----------------------------
        # Dataset Quality
        # -----------------------------
        st.markdown("---")
        st.markdown("## 📊 Dataset Quality")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", len(df))
        col2.metric("Duplicates", df.duplicated().sum())
        col3.metric("Missing Values", df.isnull().sum().sum())

        st.markdown("---")
        st.markdown("## 🛠 Cleaning Tools")

        # =============================
        # Remove Duplicates
        # =============================
        if st.button("🗑 Remove Duplicates"):

            before = len(df)

            df = df.drop_duplicates()

            st.session_state.df = df

            after = len(df)

            st.success(f"✅ Removed {before-after} duplicate rows.")

            st.dataframe(df, use_container_width=True)

        # =============================
        # Missing Value Handling
        # =============================
        st.markdown("### Missing Value Handling")

        option = st.selectbox(
            "Choose Method",
            [
                "Mean (Numeric)",
                "Median (Numeric)",
                "Mode (All Columns)"
            ]
        )

        if st.button("Fill Missing Values"):

            if option == "Mean (Numeric)":

                numeric = df.select_dtypes(include="number").columns

                df[numeric] = df[numeric].fillna(df[numeric].mean())

            elif option == "Median (Numeric)":

                numeric = df.select_dtypes(include="number").columns

                df[numeric] = df[numeric].fillna(df[numeric].median())

            else:

                for col in df.columns:
                    if df[col].isnull().sum() > 0:
                        df[col] = df[col].fillna(df[col].mode()[0])

            st.session_state.df = df

            st.success("✅ Missing values handled successfully!")

            st.dataframe(df, use_container_width=True)

        # =============================
        # Remove Empty Rows
        # =============================
        if st.button("🗑 Remove Empty Rows"):

            before = len(df)

            df = df.dropna(how="all")

            after = len(df)

            st.session_state.df = df

            st.success(f"✅ Removed {before-after} empty rows.")

            st.dataframe(df, use_container_width=True)
