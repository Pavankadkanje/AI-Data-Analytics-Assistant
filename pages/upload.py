import streamlit as st
import pandas as pd


def show():

    st.title("📁 Upload Dataset")

    uploaded_file = st.file_uploader(
        "📂 Drag & Drop or Browse your CSV / Excel file",
        type=["csv", "xlsx"],
        help="Supported formats: CSV and Excel (.xlsx)"
    )

    # Read uploaded file
    if uploaded_file is not None:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Save dataset
        st.session_state.original_df = df.copy()
        st.session_state.df = df.copy()

        st.success("✅ Dataset Uploaded Successfully!")

        st.info(f"""
**File Name:** {uploaded_file.name}

**File Size:** {round(uploaded_file.size / 1024, 2)} KB
""")

    # Display dataset
    if st.session_state.df is not None:

        df = st.session_state.df

        st.markdown("## 📋 Dataset Preview")

        st.dataframe(
            df,
            use_container_width=True,
            height=400
        )

        st.markdown("---")
        st.markdown("## 📊 Dataset Summary")

        rows = df.shape[0]
        columns = df.shape[1]
        missing = df.isnull().sum().sum()
        duplicates = df.duplicated().sum()
        memory = round(df.memory_usage(deep=True).sum() / 1024, 2)

        c1, c2 = st.columns(2)
        c1.metric("Rows", rows)
        c2.metric("Columns", columns)

        c3, c4 = st.columns(2)
        c3.metric("Missing Values", missing)
        c4.metric("Duplicates", duplicates)

        st.metric("Memory Usage (KB)", memory)

        st.markdown("---")
        st.markdown("## 📋 Column Information")

        column_info = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Missing Values": df.isnull().sum().values,
            "Unique Values": df.nunique().values
        })

        st.dataframe(
            column_info,
            use_container_width=True,
            height=300
        )

        st.markdown("---")
        st.markdown("## 📈 Statistical Summary")

        st.dataframe(
            df.describe(include="all"),
            use_container_width=True,
            height=350
        )

    else:
        st.info("📂 Please upload a CSV or Excel file to begin.")

        