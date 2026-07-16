import streamlit as st

def show():

    st.title("📊 AI Data Analytics Assistant")

    st.markdown(
        """
        Welcome to your AI-powered data analytics platform.

        Upload a dataset and use AI to clean, analyze, visualize,
        predict, and generate reports in one place.
        """
    )

    st.divider()

    st.subheader("🚀 Features")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📁 Upload CSV & Excel Files")
        st.info("🧹 Automatic Data Cleaning")
        st.info("📊 Interactive Visualizations")
        st.info("🤖 AI Chat with Gemini")

    with col2:
        st.info("📈 Machine Learning Prediction")
        st.info("📄 AI Report Generation")
        st.info("📥 Download Trained Models")
        st.info("📱 Mobile Friendly")

    st.divider()

    st.subheader("⚡ Quick Start")

    st.success("""
1. Upload your dataset.
2. Explore Data Profile.
3. Clean missing values.
4. Create visualizations.
5. Ask AI questions.
6. Train ML models.
7. Download reports and models.
""")

    st.divider()

    st.subheader("📌 Current Status")

    if st.session_state.df is None:

        st.warning("No dataset uploaded.")

    else:

        rows, cols = st.session_state.df.shape

        c1, c2 = st.columns(2)

        c1.metric("Rows", rows)
        c2.metric("Columns", cols)