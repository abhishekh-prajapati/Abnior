import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time
import os

class Vision:
    def __init__(self):
        # We need a model file for the hand landmarker
        # For simplicity, if the model isn't here, we'll try to download or skip
        model_path = os.path.join("p:\\Abnior", "assets", "hand_landmarker.task")
        
        # Download the model if it doesn't exist (this is just the path setup, 
        # actual download logic would be added if needed, or we'll assume it exists if we can't download)
        
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=1,
            min_hand_detection_confidence=0.7,
            min_hand_presence_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.detector = vision.HandLandmarker.create_from_options(options)
        self.cap = cv2.VideoCapture(0)

    def detect_gesture(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        
        frame = cv2.flip(frame, 1) # Mirror image
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # MediaPipe image format
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        
        # Detect landmarks
        # This will fail if the .task model file is missing
        try:
            results = self.detector.detect(mp_image)
            gesture = None
            
            if results.hand_landmarks:
                # Basic check for thumb up
                # Hand landmarks: wrist=0, thumb_tip=4, thumb_ip=3, index_mcp=5
                landmarks = results.hand_landmarks[0]
                thumb_tip_y = landmarks[4].y
                thumb_ip_y = landmarks[3].y
                index_mcp_y = landmarks[5].y
                
                if thumb_tip_y < thumb_ip_y < index_mcp_y:
                    gesture = "THUMB_UP"
            
            return gesture
        except Exception as e:
            # print(f"Vision detection error: {e}")
            return None

    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    v = Vision()
    try:
        while True:
            gesture = v.detect_gesture()
            if gesture:
                print(f"Gesture detected: {gesture}")
            time.sleep(0.1)
    except KeyboardInterrupt:
        v.close()
