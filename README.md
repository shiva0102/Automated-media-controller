# Automated Media Controller System

This project enables media playback control using hand gestures and eye detection through a webcam. It uses [MediaPipe](https://google.github.io/mediapipe/) for hand and eye detection and [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) to simulate keyboard inputs, allowing for hands-free media control.

## Features

- **Play/Pause Control**: Automatically plays or pauses media playback based on eye detection (open or closed).
- **Gesture Control**: Uses hand gestures to control media playback:
  - **1 Finger**: Next track (right arrow key)
  - **2 Fingers**: Previous track (left arrow key)
  - **3 Fingers**: Volume up (up arrow key)
  - **4 Fingers**: Volume down (down arrow key)

## Requirements

- **Python 3.x**
- **Required Libraries**:
  - `opencv-python`: for video capture and frame manipulation
  - `mediapipe`: for hand and eye detection
  - `pyautogui`: for simulating media control keypresses
  - `time`: for handling gesture timing

### Installation

To install the required libraries, run:

```bash
pip install opencv-python mediapipe pyautogui
```

## Code Overview

1. **Initialize Libraries and Models**  
   - Imports OpenCV, MediaPipe, and PyAutoGUI.
   - Sets up MediaPipe’s hand and face detection models.

2. **Functions**
   - `count_fingers(lst)`: Counts extended fingers based on hand landmark positions.
   - `detect_eyes(frame)`: Detects if eyes are open by checking for eye landmarks.

3. **Main Loop**  
   The program:
   - Continuously captures video frames and processes them for hand and eye detection.
   - Controls media playback with a simulated spacebar key press based on eye detection (open to play, closed to pause).
   - Recognizes hand gestures and sends corresponding media commands.

4. **Control Actions**  
   Based on the number of extended fingers:
   - **1 Finger** → Next track
   - **2 Fingers** → Previous track
   - **3 Fingers** → Volume up
   - **4 Fingers** → Volume down

5. **Exit Condition**  
   Press the **Escape key (Esc)** to end the program, release the camera, and close the video window.

## How to Run

1. Connect your webcam.
2. Run the script with:

   ```bash
   python gesture_media_control.py
   ```

3. The program will open a video window and start detecting gestures and eye status.

## Troubleshooting

- Ensure you have the latest version of each library.
- Check your webcam permissions if the video window doesn’t open.
- Adjust lighting for optimal hand and eye detection.

## Notes

- Gesture recognition relies on clear hand visibility. Ensure your hand is within the webcam's view.
- For eye detection, position yourself directly facing the camera.

##  Future Scope
-  This system can be adapted for broader applications, such as:

-  Smart TVs: Gesture-based control for navigating channels or adjusting volume without remotes.
-  Home Automation: Integrating with smart home systems to control lighting, appliances, or media devices.
-  Virtual Meetings: Controlling video calls hands-free to mute/unmute or switch views based on gestures and eye presence.

