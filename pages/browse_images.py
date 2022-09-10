import streamlit as st
from PIL import Image
from os import listdir
from tinydb import TinyDB, Query


def get_images():
    folder = str(st.session_state.folder)
    images = []

    for item in listdir(folder):
        foo = item.lower()
        if foo[-4:] in ['.png', '.jpg'] or foo[-5:] in [".jpeg"]:
            images.append(folder + '/' + item)

    return images


def load_db(PATH):
    db = TinyDB(str(PATH)+'/PixBuddy.json')
    return db


if 'db' not in st.session_state:
    st.session_state.db = load_db(st.session_state.folder)

if 'images' not in st.session_state:
    st.session_state.images = get_images()

if 'index' not in st.session_state:
    st.session_state.index = 0

image = Image.open(st.session_state.images[st.session_state.index % len(st.session_state.images)])

st.markdown(f"Image {st.session_state.index % len(st.session_state.images) + 1} of {len(st.session_state.images)}")
st.markdown(f"Loading image from path {st.session_state.images[st.session_state.index % len(st.session_state.images)]}")

st.image(image, use_column_width=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col3:
    if st.button('Next'):
        st.session_state.index += 1
        st.experimental_rerun()

with col1:
    if st.button('Prev'):
        st.session_state.index -= 1
        st.experimental_rerun()


obj = Query()
if st.session_state.db.search(obj.pth == st.session_state.images[st.session_state.index % len(st.session_state.images)]):
    data = st.session_state.db.search(obj.pth == st.session_state.images[st.session_state.index % len(st.session_state.images)])
    text = data[0]['text']
    st.markdown(text)
