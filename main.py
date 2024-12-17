from openai import OpenAI
import streamlit as st

client = OpenAI()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Chatbot")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Entrez votre message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Génération de la réponse...")
        
        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            response = completion.choices[0].message.content
            
            message_placeholder.markdown(response)
            
            st.session_state.messages.append({"role": "assistant", "content": response})
        
        except Exception as e:
            message_placeholder.markdown(f"Erreur : {str(e)}")