import streamlit as st
from openai import OpenAI
from pathlib import Path
import os

client = OpenAI()

st.title("🎙️ Assistant Vocal Interactif")

st.header("1. Transcription Audio")
audio_input = st.audio_input("📥 Enregistrez votre message vocal")

if audio_input:
    os.makedirs("temp", exist_ok=True)
    input_path = "temp/input.mp3"
    
    with open(input_path, "wb") as file:
        file.write(audio_input.getbuffer())
    
    with open(input_path, "rb") as audio_file:
        transcription = client.audio.translations.create(
            model="whisper-1", 
            file=audio_file
        )
    
    st.write("📝 Transcription :", transcription.text)

    st.header("2. Réponse de l'Assistant")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu es un assistant vocal intelligent et bienveillant."},
            {"role": "user", "content": transcription.text}
        ]
    )
    
    assistant_text = response.choices[0].message.content
    st.write("🤖 Réponse :", assistant_text)

    st.header("3. Conversion Texte → Audio")
    
    speech_response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",  # autres voix (alloy, echo, fable, onyx, nova, shimmer)
        input=assistant_text
    )
    
    output_path = "temp/output.mp3"
    speech_response.stream_to_file(output_path)
    
    st.audio(output_path, autoplay=True)

