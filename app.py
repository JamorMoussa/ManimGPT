import streamlit as st

<<<<<<< HEAD
from home import home_page
from demo import demo_page 

def main():
    st.set_page_config(page_title="AniThing", page_icon=":magic_wand", layout="wide")
    st.title("AniThing : GenAI Solution ")
    st.sidebar.image('./media/logo1.png', width=200)
    st.sidebar.title('Navigation')

    # Add links to different sections of the app
    page = st.sidebar.radio("Go to", ["Home", "Demo"])

    # Home Page Content
    if page == "Home":
        home_page()

    # Demo Page Content
    elif page == "Demo":
        demo_page()
=======
def main():
    st.set_page_config(page_title="AniThing", page_icon=":magic_wand", layout="wide")
    st.title("Manim Code Generator")
    st.sidebar.image('./media/logo1.png', width=200)
    # Add a title to the sidebar and set its width
    st.sidebar.title('Navigation')
    

    # Add links to different sections of the app
    home = st.sidebar.button("Home")
    about = st.sidebar.button("Demo")

    # User Input Prompt Section
    st.write(
        """
        ## Demo
        Enter your prompt below to generate Manim animation code:
        """
    )

    # Input prompt text area
    prompt = st.text_area("Enter your prompt here:")

    # Button to generate Manim code
    if st.button("Generate Manim Code"):
        # Call function to generate Manim code (to be implemented)
        # manim_code = generate_manim_code(prompt)
        # Display the generated Manim code
            # Displaying a sample video from a local file
        st.header("Sample Video")
        video_path = "./media/videos/AreaUnderCurveExample.mp4"
        st.video(video_path)
>>>>>>> b070ab4 (Adding the streamlit app)

if __name__ == "__main__":
    main()
