import streamlit as st
from code.directory_picker import st_directory_picker

st.set_page_config(page_title='PixBuddy', page_icon='assets/icon.png')

st_directory_picker()

code1 = """import streamlit as st
from directorypicker import st_directory_picker
st_directory_picker()
st.markdown(st.session_state.path)"""

code2 = """my_selected_path = st_directory_picker()
st.markdown(my_selected_path)"""

st.markdown("---")
st.markdown("You can access the selected path from: ")
st.markdown("- The session state `st.session_state.path`:")
st.code(code1, language="python")
st.markdown("- return value of the function:")
st.code(code2, language="python")
st.markdown(st.session_state.path)
