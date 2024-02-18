import streamlit as st

def home_page(): 

    st.image('./media/logo2.png', width=300)
    
    st.header("Welcome to AniThing - Animate Anything")
    st.image("./media/ContinuousMotion.gif", caption='Your GIF Caption', use_column_width=True)
    st.write("""
        AniThing is a Manim code generator tool that allows users to input prompts and automatically generate Manim animation. 
        Simply enter your prompt in the text area provided in the 'Demo' section and click the 'Generate Manim Code' button to see the code.
        Explore the different features and options available in the sidebar navigation.
    """)