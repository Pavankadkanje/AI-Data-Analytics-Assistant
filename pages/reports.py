import streamlit as st
import pandas as pd
import io
import os

from utils.report_generator import generate_pdf


def show():

    st.title("📄 Reports")

    if st.session_state.df is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    df = st.session_state.df

    # ==================================
    # Dataset Preview
    # ==================================

    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    st.markdown("---")

    # ==================================
    # Dataset Summary
    # ==================================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing", df.isnull().sum().sum())
    col4.metric("Duplicates", df.duplicated().sum())

    st.markdown("---")

    # ==================================
    # Download CSV
    # ==================================

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )

    # ==================================
    # Download Excel
    # ==================================

    excel = io.BytesIO()

    with pd.ExcelWriter(excel, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    st.download_button(
        label="⬇ Download Excel",
        data=excel.getvalue(),
        file_name="cleaned_dataset.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    st.markdown("---")

    # ==================================
    # PDF Report
    # ==================================

    os.makedirs("generated_reports", exist_ok=True)

    if st.button("📄 Generate PDF Report"):

        filename = "/AI_Data_Report.pdf"

        generate_pdf(df, filename)

        with open(filename, "rb") as pdf_file:

            st.download_button(
                label="⬇ Download PDF Report",
                data=pdf_file,
                file_name="AI_Data_Report.pdf",
                mime="application/pdf"
            )

        st.success("✅ PDF Report Generated Successfully!")