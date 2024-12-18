from openai import OpenAI
import streamlit as st
import os
from utils.openai_processor import OpenAIProcessor

processor = OpenAIProcessor()

# Initialiser l'état de session si nécessaire
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.last_prompt = None

st.title("🖋️ Générateur d'Articles")

if prompt := st.chat_input("Donnez moi un sujet.", key=f"user_input"):
    if prompt != st.session_state.last_prompt:
        # Affiche les messages de chat de l'historique quand on change le prompt
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        st.session_state.last_prompt = prompt

    # Afficher le message de l'utilisateur dans le conteneur de message de chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Ajouter le message de l'utilisateur à l'historique des messages
    st.session_state.messages.append({"role": "user", "content": prompt, "type": "text", "prompt": prompt})

    # Affiche les réponses de l'assistant
    with st.chat_message("assistant"):
        with st.status("Requête en cours...", expanded=False) as status:
            result = processor.article_generator(prompt)
            parts = result.split('¤')

            value = 1
            for part in parts: 
                # Écriture du texte du paragraphe
                st.write(part)
                
                # Ajout du texte dans les messages de session
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": part, 
                    "type": "text", 
                    "prompt": prompt
                })
            
                # Mise à jour du statut
                status.update(label=f"Paragraphe {value}/4 généré...")
                
                if part != "Bien tenté mais non.":
                    # Génération de l'image
                    image_url = processor.openai_create_image(prompt)
                    
                    # Affichage de l'image dans l'interface utilisateur
                    st.image(image_url, caption=f"Image {value}")

                    # Ajout de l'URL de l'image dans l'historique
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": image_url,
                        "type": "image", 
                        "prompt": prompt
                    })

                value += 1
            
            status.update(label="Réponse générée!", state="complete", expanded=True)