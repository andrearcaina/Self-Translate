import av
import streamlit as st
from streamlit_webrtc import webrtc_streamer

def camera_recognition():
    webrtc_streamer(
        key="WYH",
        video_processor_factory=None,
        async_transform=False,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=False,
    )