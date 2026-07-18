import streamlit as st
from chains.support_chains import support_chain

st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🎧",
    layout="wide"
)

# ---------------- Session ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("🎧 Customer Support")

    st.markdown("---")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- Main ---------------- #

st.title("AI Customer Support Assistant")

st.write(
    "Welcome! Ask any customer support related question."
)

# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input

user_input = st.chat_input("Type your question here...")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = support_chain.invoke(
                    {
                        "question": user_input
                    }
                )

                st.markdown(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as e:

                st.error(str(e))