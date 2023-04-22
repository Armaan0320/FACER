#**FACER**
#**Face Attendance system**

This is a Python project that uses OpenCV, face_recognition, tkinter, csv, numpy, datetime, os and customtkinter libraries to implement face-recognition based attendance system. The system detects faces in real-time from your system's camera, matches them with known faces in a database, and maintains an attendance record with date and time stamp of the recognized faces.

##**Prerequisities**
The following Python libraries must be installed to run this project:
- OpenCV
- face_recognition
- tkinter
- datetime
- customtkinter
- numpy

##**Installation**
1. Clone or download this repository.
2. Install the required libraries using pip:
  pip install opencv
  pip install face-recognition
  pip install numpy
  pip install tkinter
  pip install customtkinter
 
##**Usage**

When the program is launched, a GUI window will appear and then after clicking on the 'Start' button. It will start the camera stream and display a live feed on the screen. The system will recognize any known face that appears in the camera frame and add its name and timestamp to the attendance record.

To add a new person to the system, click on the "New Face Profile" button and a camera stream will pop up. You can use 'space' your image. After that a text box will appear, type your name in it and the system will capture new face profile and save it in the database.
