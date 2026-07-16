import streamlit as st

from pages import (
    home,
    profile,
    upload,
    cleaning,
    visualization,
    ai_chat,
    prediction,
    reports
)
from utils import profiler
# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="AI Data Analytics Assistant",
    page_icon="📊",
    layout="wide"
)

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
        "📄 Reports"
    ]
)

# ----------------------------
# Navigation
# ----------------------------

if menu == "🏠 Home":
    home.show()

elif menu == "📁 Upload Dataset":
    upload.show()

elif menu == "🧹 Data Cleaning":
    cleaning.show()

elif menu == "📊 Visualization":
    visualization.show()

elif menu == "🤖 AI Chat":
    ai_chat.show()

elif menu == "📈 Data Profile":
    profile.show()

elif menu == "📉 Prediction":
    prediction.show()

elif menu == "📄 Reports":
    reports.show()
    

elif menu == "📊 Visualization":
    visualization.show()    

elif menu == "🤖 AI Chat":
    ai_chat.show()    