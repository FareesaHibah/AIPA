import streamlit as st
from gtts import gTTS
import os

# Streamlit UI
st.title("Text to Speech Converter")
st.write("Enter text below and convert it into speech.")

# Text input
text = st.text_area("Enter text:")

# Language selection
language = st.selectbox("Select Language:", ["en", "es", "fr", "de"])
# Convert button
if st.button("Convert to Speech"):
    if text.strip():
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save("output.mp3")
        st.audio("output.mp3", format="audio/mp3", start_time=0)
    else:
        st.warning("Please enter some text.")
