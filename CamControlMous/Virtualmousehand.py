from pickle import TRUE
from turtle import left
import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

screen_w,screen_h=pyautogui.size()
index_y=0
while True:
    _, frame = cam.read()
    frame=cv2.flip(frame,1) 
    rgb_frame= cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    output= hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    
    print(hands)
    frame_h,frame_w,_=frame.shape

    if hands:        
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):                
                x=int(landmark.x * frame_w)
                y=int(landmark.y * frame_h)
                print(x,y)
                if id==8:
                    index_x= screen_w/frame_w*x
                    index_y = screen_h/frame_h*y
                    cv2.circle(img=frame,center= (x, y), radius=10,color= (0, 255, 0))
                    pyautogui.moveTo(index_x,index_y)
                if id==4:
                    cv2.circle(img=frame,center= (x, y), radius=10,color= (0, 255, 0))
                    thumb_x= screen_w/frame_w*x
                    thumb_y = screen_h/frame_h*y
                    if abs(index_y - thumb_y) <20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    
                    
            
        #     if id ==1:
        #         
        #                    
        # left = [landmarks[145], landmarks[159]]
        # for landmark in left:
        #     x=int(landmark.x * frame_w)
        #     y=int(landmark.y * frame_h)
        #     cv2.circle(frame, (x, y), 3, (0, 255, 255))
        # if(left[0].y- left[1].y) < 0.004:
        #     print("click")
        #     pyautogui.click()
        #    # pyautogui.sleep(1)

    #print(landmark_points)
    cv2.imshow(' Virtual Mouse',frame)
    cv2.waitKey(1)
    