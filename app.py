import streamlit as st

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st
import streamlit.components.v1 as components

# def run():
#     iframe_src = "https://saiprakashtut-galileo.hf.space"
#     components.iframe(iframe_src)
#    # You can add height and width to the component of course.

# if __name__ == "__main__":
#     run()


# Streamlit Title
st.title("🧬 Galileo - Biomarker Based Clinical Trial Matching!")

# Embed the Gradio app using an iframe
gradio_url = "https://saiprakashtut-galileo.hf.space"  # Replace with your Gradio app URL

iframe_code = f"""
<iframe src="{gradio_url}" width="100%" height="600" frameborder="0"></iframe>
"""

# Display iframe using Streamlit's HTML component
st.components.v1.html(iframe_code, height=600)
