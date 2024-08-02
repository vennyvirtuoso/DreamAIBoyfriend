import streamlit as st
from chatbot import DatingCoachChatbot

def main():
    st.markdown("<h1 style='text-align: center; color: #FF69B4;'>Miracle: Dream AI Boyfriend for Swifties</h1>", unsafe_allow_html=True)
    
    ai_boyfriend_name = st.text_input("Enter the name you would like to give your AI Boyfriend:")
    
    if not ai_boyfriend_name:
        st.warning("Please enter his to proceed.")
        return
    
    st.write(f"Enter your reply:")
    chatbot = DatingCoachChatbot(ai_boyfriend_name)

    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []
    
    with st.form(key='chat_form'):
        user_input = st.text_input("Start Conversation:")
        submit_button = st.form_submit_button(label='Submit')
    
    if submit_button and user_input:
        response = chatbot.get_reply(user_input)
        st.session_state.conversation_history.append((ai_boyfriend_name, user_input))
        st.session_state.conversation_history.append(("You", response))
    
    for speaker, message in st.session_state.conversation_history:
        st.write(f"**{speaker}:** {message}")

if __name__ == "__main__":
    main()





