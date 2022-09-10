import streamlit as st
from code.directory_picker import st_directory_picker

st.set_page_config(page_title='PixBuddy', page_icon='assets/icon.png')

st_directory_picker()

st.markdown(f"Path Selected: {st.session_state.path}")

if 'folder' not in st.session_state:
    st.session_state.folder = st.session_state.path

save = st.button("Use Selected Path")
if save:
    st.session_state.folder = st.session_state.path
