import streamlit as st
import requests
from PIL import Image

def main():

    #LAYOUT / CONFIG
    #set page configuration to wide
    st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
    st.title("Bunbetsu Buddy")

    st.camera_input("Show me your trash and I'll tell you how to dispose of it!")


if __name__ == "__main__":
    main()
