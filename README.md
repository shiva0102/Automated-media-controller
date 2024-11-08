# Automated Media Control System Using Hand Gestures and Eye Detection

## Project Overview
The **Automated Media Control System** is a hands-free, interactive media controller that leverages computer vision for media playback control using hand gestures and eye presence detection. This system is designed to make multimedia interaction more intuitive and accessible, especially in scenarios where physical interaction with devices may be inconvenient or impossible, such as during workouts, cooking, or presentations.

## Features
- **Eye Detection for Play/Pause**: The system detects user eye engagement to play or pause media automatically.
- **Gesture-Based Control**: Specific hand gestures control media functions such as skipping tracks and adjusting volume.
- **Real-Time Processing**: The system operates with minimal latency, providing a seamless and responsive experience.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [System Architecture](#system-architecture)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Methodology](#methodology)
8. [Results](#results)
9. [Future Scope](#future-scope)

## Technologies Used
- **OpenCV**: For capturing video streams and processing frames in real-time.
- **MediaPipe**: To detect eye presence and hand gestures, using machine learning models for hand and face tracking.
- **PyAutoGUI**: To simulate GUI interactions for media control actions, like keypresses.

## System Architecture
The system is structured as follows:
1. **Video Input Module**: Captures video feed from a webcam.
2. **Hand and Eye Detection Modules**: MediaPipe models detect hand gestures and eye presence.
3. **Media Control Logic**: Maps hand gestures and eye detection results to specific media control actions.
4. **Output Control**: Uses PyAutoGUI to send commands to the media player (e.g., play/pause, skip, volume up/down).

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/automated-media-control-system.git
# Automated Media Control System

## Install Required Packages
Make sure you have Python 3 installed, then run:

```bash
pip install opencv-python mediapipe pyautogui
