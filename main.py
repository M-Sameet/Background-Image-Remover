import streamlit as st
from rembg import remove
from io import BytesIO
from PIL import Image

# st.title("Hello upload!")
st.set_page_config(layout="wide", page_title="image Background remover")

st.write("Remove Background from Image")
st.write("Try Uploading an Image to watch the Background")
st.sidebar.write("Upload and Download :gear:")

col1, col2 = st.columns([0.5, 0.5])


# image_upload = st.file_uploader("upload an image", type=["png", "jpg", "jpeg"])


def convert_image(img):
    buf = BytesIO()
    img.save(buf, format='PNG')
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("ORIGINAL IMAGE :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("FIXED IMAGE :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\\n")
    st.sidebar.download_button("DOWNLOAD", convert_image(fixed), "fixed.png", "image/png")


my_upload = st.sidebar.file_uploader("UPLOAD AN IMAGE", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("./wallaby.png")
