import streamlit as st


from utils.profiler import (
    dataset_summary,
    column_information,
    statistical_summary,
    missing_report
)
def show():

    st.title("📊 Data Profile")

    if st.session_state.df is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    df = st.session_state.df

    # ===============================
    # Dataset Summary
    # ===============================

    summary = dataset_summary(df)

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Rows", summary["Rows"])
    col2.metric("Columns", summary["Columns"])
    col3.metric("Missing", summary["Missing Values"])
    col4.metric("Duplicates", summary["Duplicate Rows"])
    col5.metric("Memory (KB)", summary["Memory (KB)"])

    st.markdown("---")

    # ===============================
    # Column Information
    # ===============================

    st.subheader("📋 Column Information")
    st.dataframe(column_information(df), use_container_width=True)

    st.markdown("---")

    # ===============================
    # Statistical Summary
    # ===============================

    st.subheader("📈 Statistical Summary")
    st.dataframe(statistical_summary(df), use_container_width=True)

    st.markdown("---")

    # ===============================
    # Missing Value Report
    # ===============================

    st.subheader("📉 Missing Value Report")
    st.dataframe(missing_report(df), use_container_width=True)