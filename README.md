# LangToy
This project is a prototype of a toy that speaks the name of the object a baby holds in their hand.
It runs on a Raspberry Pi 4 Model B, using a USB camera and an AUX-connected speaker.

The object detection is powered by YOLOv4-tiny using OpenCV's DNN module.
Speech output is generated using offline text-to-speech libraries.

Make sure you're using Python 3.9.2 for compatibility.
Create a virtual environment with this Python version before installing dependencies.

Install all required libraries listed in the "requirements.txt" file.
Note: Ensure that the versions of OpenCV and NumPy are compatible.
The version of OpenCV that worked well with YOLOv4-tiny in this project is: opencv-python==4.5.5.64

The model is trained to recognize 80 common object classes, listed in the "classes.txt" file.
You can customize the class names or reduce the list based on your application.

After installing the dependencies, run the script "LangToy.py".
The toy will detect objects through the camera and speak their names through the speaker.
