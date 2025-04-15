import cv2
import time
import numpy as np
import math

def estimate_distance(y, h, H_img=720, FOV_vert=20, tilt_angle_deg=10, cam_height_m=5):
    # Step 1: Pixel to image-relative ratio
    y_bottom = y + h
    alpha = ((y_bottom / H_img) - 0.5) * FOV_vert  # angle from center to car bottom

    # Step 2: Add camera tilt
    theta_total = tilt_angle_deg + alpha

    # Step 3: Convert to radians and calculate distance
    theta_rad = math.radians(theta_total)
    distance = cam_height_m /math.tan(theta_rad)

    return distance
  
haar_cascade = 'haarcascades/haarcascade_car.xml'
# video name can be changed according to  your preference
video='video/clear_road.mp4'
      
cap = cv2.VideoCapture(video)
car_cascade = cv2.CascadeClassifier(haar_cascade)

# Display frames in a window
ret, frames = cap.read()
frames= cv2.resize(frames, (1280,720))
cv2.imshow('video', frames)

# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
    if not ret:
        print("End of video reached or failed to read frame.")
        break
    frames= cv2.resize(frames, (1280,720))
        
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    #blur = cv2.GaussianBlur(gray,(5,5),0)
    #dilated = cv2.dilate(blur,np.ones((3,3)))
    #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    #closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel) 
    
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        
    # To draw a rectangle in each cars and put distance text on it
    for (x,y,w,h) in cars:
      if y>0 and w>70:
        distance=int(estimate_distance(y,h,H_img=720))
        cv2.rectangle(frames,(x,y),(x+w,y+h),(255,255,255),10)
        cv2.rectangle(frames, (x-5, y-50), (x+w+5 , y), (0,100,100), -1)
        cv2.putText(frames,str(int(distance))+' M', (x+int(w/2)-10,(y-10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
    
    # Display frames in a window 
    cv2.imshow('video', frames)        
    # Wait for Esc key to stop
    if cv2.waitKey(1000) == 27:
        break
    
# Destroy tabs
cv2.destroyAllWindows()
