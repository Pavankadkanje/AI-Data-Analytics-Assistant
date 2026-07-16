import streamlit as st

from utils.gemini_chat import ask_gemini


def show():

    st.title("🤖 AI Chat")

    if st.session_state.df is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    df = st.session_state.df

    question = st.text_input(
        "Ask anything about your dataset..."
    )

    if st.button("Ask AI"):

     with st.spinner("🤖 Gemini is thinking..."):

        try:
            answer = ask_gemini(question, df)
            st.success(answer)

        except Exception as e:
            st.error(f"Error: {e}")