import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize PyAutoGUI for media playback control
media_player = pyautogui

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands() 

# Initialize MediaPipe eye detection model
mp_eye_detection = mp.solutions.face_detection
eye_detection = mp_eye_detection.FaceDetection()

# Function to count fingers   count the number of extended fingers based on the detected hand landmarks. 
def count_fingers(lst):
    cnt = 0  #lst=contain hand landmarks detected by the MediaPipe library.

    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2  #vertical distance b/w 1st and 9th landmark.  determine whether a finger is extended or not.

    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
        cnt += 1     #it indicates that the index finger is extended, so cnt is incremented by 1.

    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        cnt += 1  #it indicates that the middle finger is extended, so cnt is incremented by 1.

    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        cnt += 1  #indicates ring finger

    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        cnt += 1  #liitle finger
    return cnt 

# Function to detect eyes
def detect_eyes(frame):
    # Convert the frame to RGB format
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #MediaPipe library processes frames in RGB format.
    #using OpenCV's cvtColor function
    # Process the RGB frame using the eye detection model
    results = eye_detection.process(rgb_frame)
    eyes_detected = False
    #previously initialized eye_detection model to process the RGB frame and detect eyes

    if results.detections:
        for detection in results.detections:
            left_eye = [pt for pt in detection.location_data.relative_keypoints if 0.4 < pt.x < 0.5]
            #Extracts the keypoints corresponding to the left eye by filtering the keypoints based on
            # their relative x-coordinates. 
            #Only keypoints with x-coordinates between 0.4 and 0.5 are considered as part of the left eye.
            right_eye = [pt for pt in detection.location_data.relative_keypoints if 0.5 < pt.x < 0.6]
            
            if left_eye and right_eye:
                eyes_detected = True
                break
    return eyes_detected

# Main loop for capturing video and detecting eyes and hand gestures
cap = cv2.VideoCapture(0)
eyes_status = False  # Variable to track eyes status
prev = -1
start_init = False

while True:
    end_time = time.time()
    _, frm = cap.read()
    frm = cv2.flip(frm, 1) # flips the captured frame horizontally (around the y-axis) using OpenCV's flip function. It's often done to correct the orientation of the frame.

    # Detect hands in the frame
    res = hands.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))#The easiest way to convert is to use openCV cvtColor

    # Detect eyes in the frame
    eyes_detected = detect_eyes(frm)  #detect eyes in the flipped frame

    # If eyes status changes, play/pause media playback
    if eyes_detected != eyes_status:  #eye status has changed compared to the previous iteration and updating
        eyes_status = eyes_detected
        if eyes_detected:                  #control media playback using PyAutoGUI.
            media_player.press('space')  # Press spacebar to play
        else:
            media_player.press ('space')  # Press spacebar to pause

    if res.multi_hand_landmarks:
        hand_keyPoints = res.multi_hand_landmarks[0]  # checks any hand landmarks detection and retriving its value

        cnt = count_fingers(hand_keyPoints)  #count the number of extended fingers based on the detected hand landmarks. 

        if not(prev==cnt): 
            if not(start_init)    :   # checks if the gesture recognition process has not yet started. If start_init is False, it means this is the first time a change in finger count is detected.
                start_time = time.time()  #start a timer if the finger count changes for gesture recognition.
                start_init = True       # gesture recognition process has started.
            elif (end_time-start_time) > 0.2:
                if (cnt == 1):
                    pyautogui.press("right")
                elif (cnt == 2):
                    pyautogui.press("left")
                elif (cnt == 3):
                    pyautogui.press("up")
                elif (cnt == 4):
                    pyautogui.press("down")

                prev = cnt
                start_init = False    # resets to 0 and indicates that it is completed


    # Display the frame
    cv2.imshow("window", frm)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()   #(escape)discard all frames and breaking the loop
        cap.release()   #freeing up the camera resource. 
        break 