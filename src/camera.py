import cv2
import streamlit as st
import mediapipe as mp
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer, WebRtcMode
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1)

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        # Convert the frame to RGB
        img = cv2.cvtColor(frame.to_ndarray(format="bgr24"), cv2.COLOR_BGR2RGB)

        # Find hands in the frame
        hands, img = detector.findHands(img)

        # Convert the image back to BGR
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        return img

def camera_recognition():

    webrtc_streamer(
        key="WYH",
        mode=WebRtcMode.SENDRECV,
        video_transformer_factory=VideoTransformer,
        async_transform=False,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
    )