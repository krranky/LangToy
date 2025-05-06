import cv2
import numpy as np
import os
import pygame
from gtts import gTTS
import simpleaudio as sa
from pydub import AudioSegment  

pygame.mixer.init()
score = 0 

net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255)

classes = []
with open("dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        classes.append(class_name.strip())

print("Objects List Loaded")
print(classes)

cam = cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to capture frame")
        continue
    
   
    (class_ids, scores, bboxes) = model.detect(frame)

    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        if score > 0.5: 
            class_name = classes[class_id]
            print(f"Detected: {class_name} ({score:.2f})")
            
           
            mp3_file = f"{class_name}.mp3"
            wav_file = f"{class_name}.wav"

            if not os.path.isfile(wav_file): 
                tts = gTTS(text=class_name, lang='en', slow=False)
                tts.save(mp3_file)
                
                
                sound = AudioSegment.from_mp3(mp3_file)
                sound.export(wav_file, format="wav")
            
            
            wave_obj = sa.WaveObject.from_wave_file(wav_file)
            wave_obj.play()
