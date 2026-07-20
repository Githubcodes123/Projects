import cv2
import time
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

model_path = "C:/Users/Yonchic/Desktop/Projects/handgame/models/hand_landmarker.task"
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

mp_hands = mp.tasks.vision.HandLandmarksConnections
mp_drawing = mp.tasks.vision.drawing_utils
mp_drawing_styles = mp.tasks.vision.drawing_styles

# Create a hand landmarker instance with the live stream mode:
def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    # print("{}".format(result))
    toret = [result.handedness,result.hand_landmarks]
    return toret
options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)
with HandLandmarker.create_from_options(options) as landmarker:
    while True:
        attempt = 0
        success, img = cap.read()
        while not success and attempt < 5:
            time.sleep(0.2)
            success, img = cap.read()
            attempt += 1
        if not success:
            print("failed to read frame")
            break
        img = cv2.flip(img,1)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        landmarker.detect_async(mp_image, round((cap.get(cv2.CAP_PROP_POS_MSEC))))
        results = HandLandmarkerOptions.result_callback
        
        print(results)
        cv2.imshow("Image",img)
        # print_result(HandLandmarkerOptions.result_callback,mp_image,round((cap.get(cv2.CAP_PROP_POS_MSEC))))
        if cv2.waitKey(1) & 0xFF == ord('x') or cv2.getWindowProperty('Image',cv2.WND_PROP_VISIBLE) < 1:
            break
    cap.release()
    cv2.destroyAllWindows()
    pass
