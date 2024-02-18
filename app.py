import streamlit as st

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

if __name__ == "__main__":
    main()
