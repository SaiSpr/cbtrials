import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import streamlit as st
import streamlit.components.v1 as components

def run():
    iframe_src = "https://saiprakashtut-galileo.hf.space"
    components.iframe(iframe_src)
   # You can add height and width to the component of course.

if __name__ == "__main__":
    run()
