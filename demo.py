import streamlit as st
import time as t 

def demo_page(): 
    st.write("""
        ## Demo Area
        Enter your prompt below to generate Manim animation code:
    """)

    prompt = st.text_area("Enter your prompt here:")

    if st.button("Generate Manim Code"):
        t.sleep(10)
        st.header("Sample Video")
        video_path = "./media/videos/test/480p15/HeightExample.mp4"
        st.video(video_path)