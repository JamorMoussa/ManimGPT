import streamlit as st

def main():
    st.set_page_config(page_title="AniThing", page_icon=":magic_wand", layout="wide")
    st.title("AniThing : GenAI Solution ")
    st.sidebar.image('./media/logo1.png', width=200)
    st.sidebar.title('Navigation')

    # Add links to different sections of the app
    page = st.sidebar.radio("Go to", ["Home", "Demo"])

    # Home Page Content
    if page == "Home":
        st.image('./media/logo2.png', width=300)
        st.header("Welcome to AniThing - Animate Anything")
        st.write("""
            AniThing is a Manim code generator tool that allows users to input prompts and automatically generate Manim animation. 
            Simply enter your prompt in the text area provided in the 'Demo' section and click the 'Generate Manim Code' button to see the code.
            Explore the different features and options available in the sidebar navigation.
        """)

    # Demo Page Content
    elif page == "Demo":
        st.write("""
            ## Demo Area
            Enter your prompt below to generate Manim animation code:
        """)
        # Input prompt text area
        prompt = st.text_area("Enter your prompt here:")
        # Button to generate Manim code
        if st.button("Generate Manim Code"):
            # Call function to generate Manim code (to be implemented)
            # manim_code = generate_manim_code(prompt)
            # Display the generated Manim code
            st.header("Sample Video")
            video_path = "./media/videos/AreaUnderCurveExample.mp4"
            st.video(video_path)

if __name__ == "__main__":
    main()
