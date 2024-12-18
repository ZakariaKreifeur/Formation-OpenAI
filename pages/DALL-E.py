from openai import OpenAI
import streamlit as st

class ApplicationDALLE:
    def __init__(self):
        self.client = OpenAI()
        st.title("🎨 Générateur d'Images DALL-E")

    def generer_image(self, prompt):
        try:
            reponse = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                n=1
            )
            return reponse.data[0].url
        except Exception as e:
            st.error(f"Erreur : {e}")
            return None

    def executer(self):
        prompt = st.text_input("Décrivez l'image que vous souhaitez créer")
        
        if st.button("Générer l'image"):
            if prompt:
                with st.spinner("Génération de l'image..."):
                    url_image = self.generer_image(prompt)
                    if url_image:
                        st.image(url_image, caption=prompt)
            else:
                st.warning("Veuillez saisir une description")

if __name__ == "__main__":
    app = ApplicationDALLE()
    app.executer()