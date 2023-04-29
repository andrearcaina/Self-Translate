import cv2
import streamlit as st
import mediapipe as mp
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer, WebRtcMode
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=2)

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = cv2.cvtColor(frame.to_ndarray(format="bgr24"), cv2.COLOR_BGR2RGB)
        hands, img = detector.findHands(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        return img

def camera_recognition():
    webrtc_streamer(
        key="Hand Detection",
        mode=WebRtcMode.SENDRECV,
        video_transformer_factory=VideoTransformer,
        async_transform=False,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
    )