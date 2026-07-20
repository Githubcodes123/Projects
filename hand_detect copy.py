import cv2
import time
import numpy as np
import random as r
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

goal_size = 50
offset_frames = 0
goalx = r.randint(0,500)
goaly = r.randint(0,500)
def hand_detect():
    cap = cv2.VideoCapture(0)
    model_path = "C:/Users/Yonchic/Desktop/Projects/handgame/models/hand_landmarker.task"
    base_options = python.BaseOptions(model_asset_path=model_path)
    options = vision.HandLandmarkerOptions(base_options=base_options,num_hands = 2,running_mode = vision.RunningMode.VIDEO)
    hand_landmarker = vision.HandLandmarker.create_from_options(options)
    frame_timestamp = 0
    while True:    
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame,1)
        rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        mp_img = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        # detect hands
        result = hand_landmarker.detect_for_video(mp_img,frame_timestamp)
        frame_timestamp += 1
        # draw landmarks
        h,w,c = frame.shape
        cv2.putText(frame,str(frame_timestamp),(w-150,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),5)
        if result.hand_landmarks:
            for hand_landmarks,handedness in zip(result.hand_landmarks, result.handedness):
                hand_name = handedness[0].category_name # 'Left' or 'Right'
                if hand_name == "Left":
                    hand_name == "Right"
                else:
                    hand_name = "Left"
                for landmark in hand_landmarks:
                    x = int(landmark.x*w)
                    y = int(landmark.y*h)
                    cv2.circle(frame,(x,y),6,(0,0,255),-1)
        game(frame,result,frame_timestamp)
        cv2.imshow("image",frame)
        if cv2.waitKey(1) & 0xFF == ord('x') or cv2.getWindowProperty('image',cv2.WND_PROP_VISIBLE) < 1:
            break
    cap.release()
    cv2.destroyAllWindows()
def collision(frame,result,object):
    h,w,c = frame.shape
    for hand_landmarks,handedness in zip(result.hand_landmarks, result.handedness):
        hand_name = handedness[0].category_name # 'Left' or 'Right'
        if hand_name == "Left":
            hand_name == "Right"
        else:
            hand_name = "Left"
        
        for landmark in hand_landmarks:
            x = int(landmark.x*w)
            y = int(landmark.y*h)
            # rectangle collision
            if object[0][0] < x < object[1][0] and object[0][1] < y < object[1][1]+object[2]:
                return True
def game(frame,result,framenumber):
    global offset_frames
    global goalx
    global goaly
    h,w,c = frame.shape
    #line_coords = [start,end,thickness]
    if round(h/5)+framenumber-offset_frames >= h:
        offset_frames = framenumber
        line_coords = [(0,round(h/5)),(w,round(h/5)),40]     
    # elif round(h/5)+framenumber-offset_frames <= 0:
    #     offset_frames = framenumber
    #     line_coords = [(0,round(h/5)+framenumber - offset_frames),(w,round(h/5)+framenumber - offset_frames),40]
    else:
        line_coords = [(0,round(h/5)+framenumber - offset_frames),(w,round(h/5)+framenumber - offset_frames),40]
    goal_coords = [(goalx,goaly),(goalx+goal_size,goaly+goal_size),0]
    cv2.rectangle(frame,goal_coords[0],goal_coords[1],(255,255,0),-1)
    cv2.line(frame,line_coords[0],line_coords[1],(0,0,0),line_coords[2])
    if result.hand_landmarks:
        if collision(frame,result,line_coords):
            cv2.line(frame,line_coords[0],line_coords[1],(255,0,0),line_coords[2])
        if collision(frame,result,goal_coords):
            goalx = r.randint(0,w-goal_size)
            goaly = r.randint(0,h-goal_size)
            goal_coords = [(goalx,goaly),(goalx+goal_size,goaly+goal_size),0]
        
    
hand_detect()
