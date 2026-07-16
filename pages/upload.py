import streamlit as st
import pandas as pd

def show():

    st.title("📁 Upload Dataset")

    uploaded_file = st.file_uploader(
        "Choose CSV or Excel File",
        type=["csv", "xlsx"]
    )

    # Read uploaded file and save to session state
    if uploaded_file is not None:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Save original dataset
        st.session_state.original_df = df.copy()

        # Save working dataset
        st.session_state.df = df.copy()

        st.success("✅ Dataset Uploaded Successfully!")

    # Display dataset if available
    if st.session_state.df is not None:

        df = st.session_state.df

        st.markdown("## 📋 Dataset Preview")
        st.dataframe(df, use_container_width=True)

        st.markdown("---")
        st.markdown("## 📊 Dataset Summary")

        rows = df.shape[0]
        columns = df.shape[1]
        missing = df.isnull().sum().sum()
        duplicates = df.duplicated().sum()
        memory = round(df.memory_usage(deep=True).sum()/1024, 2)

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("Rows", rows)
        col2.metric("Columns", columns)
        col3.metric("Missing", missing)
        col4.metric("Duplicates", duplicates)
        col5.metric("Memory (KB)", memory)

        st.markdown("---")
        st.markdown("## 📋 Column Information")

        column_info = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Missing Values": df.isnull().sum().values,
            "Unique Values": df.nunique().values
        })

        st.dataframe(column_info, use_container_width=True)

        st.markdown("---")
        st.markdown("## 📈 Statistical Summary")

        st.dataframe(df.describe(include="all"), use_container_width=True)

    else:
        st.info("📂 Please upload a CSV or Excel file to begin.")