import streamlit as st

from utils.charts import (
    bar_chart,
    line_chart,
    scatter_chart,
    histogram,
    pie_chart,
    box_plot,
    correlation_heatmap
)


def show():

    st.title("📊 Data Visualization")

    if st.session_state.df is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    df = st.session_state.df

    st.dataframe(df.head(), use_container_width=True)

    st.markdown("---")

    chart = st.selectbox(
        "Select Chart",
        [
            "Bar Chart",
            "Line Chart",
            "Scatter Plot",
            "Histogram",
            "Pie Chart",
            "Box Plot",
            "Correlation Heatmap"
        ]
    )

    numeric = df.select_dtypes(include="number").columns.tolist()
    columns = df.columns.tolist()

    fig = None

    if chart == "Bar Chart":

        x = st.selectbox("X Axis", columns)
        y = st.selectbox("Y Axis", numeric)

        fig = bar_chart(df, x, y)

    elif chart == "Line Chart":

        x = st.selectbox("X Axis", columns)
        y = st.selectbox("Y Axis", numeric)

        fig = line_chart(df, x, y)

    elif chart == "Scatter Plot":

        x = st.selectbox("X Axis", numeric)
        y = st.selectbox("Y Axis", numeric)

        fig = scatter_chart(df, x, y)

    elif chart == "Histogram":

        column = st.selectbox("Column", numeric)

        fig = histogram(df, column)

    elif chart == "Pie Chart":

        column = st.selectbox("Category", columns)

        fig = pie_chart(df, column)

    elif chart == "Box Plot":

        column = st.selectbox("Column", numeric)

        fig = box_plot(df, column)

    elif chart == "Correlation Heatmap":

        fig = correlation_heatmap(df)

    st.plotly_chart(fig, use_container_width=True)