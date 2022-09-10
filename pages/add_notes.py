import streamlit as st
from PIL import Image
from pages.browse_images import get_images
from tinydb import TinyDB, Query
import imagehash


def load_db(PATH):
    db = TinyDB(str(PATH)+'/PixBuddy.db')
    return db


if 'db' not in st.session_state:
    st.session_state.db = load_db(st.session_state.folder)

if 'images' not in st.session_state:
    st.session_state.images = get_images()

if 'index' not in st.session_state:
    st.session_state.index = 0

image = Image.open(st.session_state.images[st.session_state.index % len(st.session_state.images)])

st.markdown(f"Image {st.session_state.index % len(st.session_state.images) + 1} of {len(st.session_state.images)}")

st.image(image, use_column_width=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col3:
    next = st.button('Next')
    if next:
        st.session_state.index += 1
        st.experimental_rerun()

with col1:
    prev = st.button('Prev')
    if prev:
        st.session_state.index -= 1
        st.experimental_rerun()

text = st.text_area("Image Description")

save = st.button("Save")

if save:
    obj = Query()

    if not st.session_state.db.search(obj.pth == st.session_state.images[st.session_state.index % len(st.session_state.images)]):
        st.session_state.db.insert(
            {
                'pth': st.session_state.images[st.session_state.index % len(st.session_state.images)],
                'text': text,
                'hash': {
                    'average_hash': str(imagehash.average_hash(image)),
                    'perceptual_hash': str(imagehash.colorhash(image)),
                    'crop_resistant_hash': str(imagehash.crop_resistant_hash(image)),
                    'dhash': str(imagehash.dhash(image)),
                    'dhash_vert': str(imagehash.dhash_vertical(image))
                },
                'im_size': image.size
            }
        )

    else:
        st.session_state.db.update(
            {'text': text},
            obj.pth == st.session_state.images[st.session_state.index % len(st.session_state.images)]
        )
