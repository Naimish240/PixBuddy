import streamlit as st
from PIL import Image
from os import listdir


def get_images():
    folder = str(st.session_state.folder)
    images = []

    for item in listdir(folder):
        if (item.endswith(".png") or item.endswith(".jpg") or item.endswith(".jpeg")):
            images.append(folder + '/' + item)

    return images


if 'images' not in st.session_state:
    st.session_state.images = get_images()

if 'index' not in st.session_state:
    st.session_state.index = 0

image = Image.open(st.session_state.images[st.session_state.index % len(st.session_state.images)])

st.markdown(f"Loading image from path {st.session_state.images[st.session_state.index % len(st.session_state.images)]}")

st.image(image, use_column_width=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col3:
    if st.button('Next'):
        st.session_state.index += 1

with col1:
    if st.button('Prev'):
        st.session_state.index -= 1
