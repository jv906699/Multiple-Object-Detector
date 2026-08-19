Execution Procedure (How to Run the Model)

1. Install Required Libraries

Before running the GUI application, install the following Python libraries:
pip install ultralytics
pip install opencv-python
pip install pillow
pip install pandas
pip install tk

2. Python Environment Note

This project can be run from:
# Command Prompt
# Windows PowerShell
# VS Code Terminal
# Anaconda Prompt (optional)
# As long as Python + required libraries are installed, the GUI will run on any machine.

3. How to Run the GUI Application

Step 1: Open Terminal

Open Command Prompt / PowerShell / VS Code Terminal / Anaconda Prompt.

Step 2: Navigate to the Folder

Copy the path of the folder in which detector_gui.py is stored and run:

cd <your-project-folder-path>

Example:
cd C:\Users\Jatin\Desktop\MultipleObjectDetector\

Step 3: Run the GUI Script :-

python detector_gui.py

Step 4: Load the YOLO Model

Inside the GUI:

Click “Load Model”
Navigate to:
best.pt (the best.pt is what you need to load )
Select best.pt
Wait for a success message

Step 5: Start Detection

After the model is loaded successfully, you can perform:

Webcam Live Detection
Video File Detection
Image Detection
Real-time predictions with bounding boxes will appear in the GUI window.