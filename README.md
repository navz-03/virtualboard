# Virtual Board
The Virtual Board is an interactive application that leverages computer vision techniques to create a virtual drawing board. Users can control the board using hand gestures, thanks to the integration of OpenCV, MediaPipe, and NumPy.

# Features:
**Hand Tracking:** The application uses MediaPipe to track the coordinates of the user’s hands in real time. By detecting hand landmarks, it identifies the position and movement of each hand.
<br>

**Grid Interaction:** The virtual board is divided into a grid. When a user’s hand enters a specific grid cell, that area is highlighted. This allows users to draw or interact with the board by moving their hands within the grid.
<br>

**Drawing Mode**: Users can switch to drawing mode, where their hand movements translate into lines or shapes on the virtual board. Imagine creating digital art by simply waving your hand!
<br>

**Color Selection:** You can incorporate color selection by associating hand gestures with different colors. For example, forming a fist could switch to red, while an open palm could select blue.
<br>

# Requirements:
Python 3.x<br>
OpenCV<br>
MediaPipe<br>
NumPy<br>

# Usage:
Install the required libraries using pip install opencv-python mediapipe numpy.<br>
Run the virtual_board.py script.<br>
Calibrate the system by placing your hands within the camera view. The application will detect your hand landmarks.<br>
Start drawing or interacting with the grid!<br>

# Future Enhancements:
Add more gestures for features like erasing, changing brush size, or undoing actions.<br>
Explore multi-user support for collaborative drawing sessions.<br>
Optimize performance for smoother hand tracking.<br>
