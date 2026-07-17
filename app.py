import streamlit as st

from pages import (
    home,
    profile,
    upload,
    cleaning,
    visualization,
    ai_chat,
    prediction,
    reports,
    login
)
# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="AI Data Analytics Assistant",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ----------------------------
# Custom CSS
# ----------------------------

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
    padding-left:1rem;
    padding-right:1rem;
}

.stButton>button{
    width:100%;
    border-radius:10px;
}

.stDownloadButton>button{
    width:100%;
    border-radius:10px;
}

.stTextInput input{
    font-size:18px;
}

.stTextArea textarea{
    font-size:18px;
}

@media (max-width:768px){

    .block-container{
        padding-left:0.5rem;
        padding-right:0.5rem;
    }

    h1{
        font-size:28px;
    }

}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Session State
# ----------------------------

if "df" not in st.session_state:
    st.session_state.df = None

if "original_df" not in st.session_state:
    st.session_state.original_df = None

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.title("📊 Navigation")

menu = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Home",
        "📁 Upload Dataset",
        "📈 Data Profile",
        "🧹 Data Cleaning",
        "📊 Visualization",
        "🤖 AI Chat",
        "📉 Prediction",
        "📄 Reports",
        "👤 Account"
    ]
)

# ----------------------------
# Navigation
# ----------------------------

if menu == "🏠 Home":
    home.show()

elif menu == "📁 Upload Dataset":
    upload.show()

elif menu == "📈 Data Profile":
    profile.show()

elif menu == "🧹 Data Cleaning":
    cleaning.show()

elif menu == "📊 Visualization":
    visualization.show()

elif menu == "🤖 AI Chat":
    ai_chat.show()

elif menu == "📉 Prediction":
    prediction.show()

elif menu == "📄 Reports":
    reports.show()

elif menu == "👤 Account":
    login.show()
