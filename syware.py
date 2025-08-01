# Librerias #

import pyautogui
import os
from time import time
from datetime import datetime
import cv2 as cv
import numpy as np

# Video n screenshots #

class screenshot:
    
    def __init__(self):
        self.imagepath = os.path.join(os.getcwd(), "takensend", "image")
        self.image = None
        self.rawdatetime = datetime.now()
        self.datetime = self.rawdatetime.strftime("%d_%m_%Y_%H_%M_%S")
        
    
    def takensave(self):
        self.image = f"takensend/image/Imagen {self.datetime}.jpg"
        
        print("Tomando captura")
        pyautogui.screenshot(self.image)
    
    def checkpath(self):
        if not os.path.exists(self.imagepath):
            print(f"[{self.imagepath}] No econtrado, creando...")
            os.makedirs(self.imagepath)

class videotake:
    
    def __init__(self):
        self.videopath = os.path.join(os.getcwd(), "takensend", "video")
        self.rawdatetime = datetime.now()
        self.datetime = self.rawdatetime.strftime("%d_%m_%Y_%H_%M_%S")
    
    
    def takensavev(self):
        self.start_time = time()
        self.fourcc = cv.VideoWriter_fourcc(*'XVID')
        self.fps = 20
        self.screenshot = pyautogui.screenshot()
        self.frame = np.array(self.screenshot)
        self.frame = cv.cvtColor(self.frame, cv.COLOR_RGB2BGR)
        self.altura, self.ancho, _ = self.frame.shape
        self.framesize = (self.ancho, self.altura)

        
        self.out = cv.VideoWriter(os.path.join(self.videopath, f"Video {self.datetime}.avi"), self.fourcc, self.fps, self.framesize)
        
        while True:
            self.current_time = time()
            if self.current_time - self.start_time > 30:
                break
            
            self.screenshot = pyautogui.screenshot()
            self.frame = np.array(self.screenshot)
            self.frame = cv.cvtColor(self.frame, cv.COLOR_RGB2BGR)
            self.out.write(self.frame)

        
        self.out.release()
    
    def checkpath(self):
        if not os.path.exists(self.videopath):
            print(f"[{self.videopath}] No econtrado, creando")
            os.makedirs(self.videopath)

class camtake:
    
    def __init__(self):
        self.campath = os.path.join(os.getcwd(), "takensend", "image")
        self.rawdatetime = datetime.now()
        self.datetime = self.rawdatetime.strftime("%d_%m_%Y_%H_%M_%S")
        self.cam = cv.VideoCapture(0)
        pass
    
    def takecamphoto(self):
        if self.cam.isOpened(): 
            ret, frame = self.cam.read()
            cv.imwrite((os.path.join(self.campath, f"Camara {self.datetime}.jpg")), frame)
        else:
            print("Camara no encontrada")
            return

    def checkpath(self):
        if not os.path.exists(self.campath):
            print(f"[{self.campath}] No econtrado, creando...")
            os.makedirs(self.campath)


def main():
    
    camara = camtake()
    camara.checkpath()
    camara.takecamphoto()
    
    screen = screenshot()
    screen.checkpath()
    screen.takensave()

    video = videotake()
    video.checkpath()
    video.takensavev()

if __name__ == "__main__":
    
    main()