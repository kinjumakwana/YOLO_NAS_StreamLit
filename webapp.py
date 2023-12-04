# import module
import streamlit as st

# Title
st.title("Yolo-NAS Project")

# import Image from pillow to open images
from PIL import Image
img = Image.open("streamlit.png")
st.image(img)

# Video adding
vid_file = open(r"D:\New folder\Videos\demo1.mp4", "rb")
vid_bytes = vid_file.read()
st.video(vid_bytes) # 10m

# Audio
sudio_file = open("pop.mp3", "rb").read()
st.audio(sudio_file)

