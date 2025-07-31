# Librerias #

import pynput
import os
import sys
import logging as logg
from pynput import keyboard, mouse

# Keylogger class #

class keylog:
    
    def __init__(self):
        "Inicializador de la clase"
        self.loggerpath = os.path.join(os.getcwd(), "log.txt")
    def keylogger(self):
        "Funcion que captura las teclas presionadas"
        pass
    def mouselogger(self):
        "Funcion que captura el mouse y sus botones"
        pass