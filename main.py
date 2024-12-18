import streamlit as st

path = "root/pages/"

pg = st.navigation([
    st.Page("pages/Home.py", icon=":material/home:"), 
    # st.Page("pages/NLP.py", title="1. Traitement du Langage Naturel"),
    st.Page("pages/OpenAI.py", title="1. Chat OpenAI"), 
    st.Page("pages/DALL-E.py", title="2. Génération d'Images DALL-E"),
    st.Page("pages/Article_Generator.py", title="3. Générateur d'articles"),
    st.Page("pages/Whisper.py", title="4. Transcription Audio"),
    # st.Page("pages/Fine_Tuning.py", title="5. Ajustement du Modèle"),
    # st.Page("pages/Final_Exercise.py", title="6. Exercice Final"),

]) 

# Exécution de la navigation
pg.run()