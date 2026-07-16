import streamlit as st

from utils.chatbot import answer_question


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

        answer = answer_question(df, question)

        if hasattr(answer, "shape"):
            st.dataframe(answer)
        else:
            st.success(answer)