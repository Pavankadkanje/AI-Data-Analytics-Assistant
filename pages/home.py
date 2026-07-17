import streamlit as st


def show():

    # ==============================
    # HERO SECTION
    # ==============================

    st.markdown("""
    # 📊 AI Data Analytics Assistant

    ### Transform your raw data into meaningful insights with AI.

    Upload your dataset and instantly **clean, analyze, visualize, predict,
    chat with your data, and generate reports** — all from one platform.
    """)

    st.markdown("---")

    # ==============================
    # FEATURE CARDS
    # ==============================

    st.markdown("## 🚀 Features")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        ### 📁 Upload Dataset
        Upload CSV and Excel datasets for instant analysis.
        """)

        st.info("""
        ### 🧹 Automatic Data Cleaning
        Handle missing values, duplicates, and data quality issues.
        """)

        st.info("""
        ### 📊 Interactive Visualization
        Generate charts and explore patterns in your data.
        """)

        st.info("""
        ### 🤖 AI Data Chat
        Ask questions about your dataset using AI.
        """)

    with col2:
        st.info("""
        ### 📈 Machine Learning Prediction
        Train Linear Regression, Decision Tree, Random Forest,
        and XGBoost models.
        """)

        st.info("""
        ### 📄 AI Report Generation
        Generate downloadable data analysis reports.
        """)

        st.info("""
        ### 💾 Download ML Models
        Train and download machine learning models as `.pkl` files.
        """)

        st.info("""
        ### 📱 Mobile Friendly
        Access the application from desktop, tablet, or mobile.
        """)

    st.markdown("---")

    # ==============================
    # APP PREVIEW
    # ==============================

    st.markdown("## 🖥️ Application Preview")

    tab1, tab2, tab3, tab4 = st.tabs([
        "📁 Upload",
        "📊 Visualization",
        "🤖 AI Chat",
        "📈 Prediction"
    ])

    with tab1:
        st.image(
            "assets/images/upload.png",
            caption="Upload Dataset"
        )

    with tab2:
        st.image(
            "assets/images/visualization.png",
            caption="Interactive Data Visualization"
        )

    with tab3:
        st.image(
            "assets/images/ai_chat.png",
            caption="AI-powered Data Chat"
        )

    with tab4:
        st.image(
            "assets/images/prediction.png",
            caption="Machine Learning Prediction"
        )

    st.markdown("---")

    # ==============================
    # PROJECT LINKS
    # ==============================

    st.markdown("## 🔗 Project Links")

    col1, col2 = st.columns(2)

    with col1:
        st.link_button(
            "⭐ View Project on GitHub",
            "https://github.com/Pavankadkanje",
            use_container_width=True
        )

    with col2:
        st.link_button(
            "💼 Connect on LinkedIn",
            "https://www.linkedin.com/in/pavan-kadkanje-307155327",
            use_container_width=True
        )

    st.markdown("---")

    # ==============================
    # BUILT WITH
    # ==============================

    st.markdown("## 🛠️ Built With")

    st.markdown("""
    **Frontend & Application**
    - Python
    - Streamlit

    **Data Analytics**
    - Pandas
    - NumPy
    - Matplotlib

    **Machine Learning**
    - Scikit-learn
    - XGBoost

    **Artificial Intelligence**
    - Gemini API

    **Database**
    - MySQL

    **Deployment & Version Control**
    - Streamlit Community Cloud
    - Git & GitHub
    """)

    st.markdown("---")

    st.caption(
        "AI Data Analytics Assistant | Built as an end-to-end Data Analytics & AI project"
    )