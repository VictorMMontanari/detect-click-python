import cv2
from pynput import mouse, keyboard
import os

# Caminho da pasta onde as imagens serão salvas
pasta = "Datasets/imgs"

# Verifica se o caminho da pasta existe, caso contrário, cria a pasta
if not os.path.exists(pasta):
    os.makedirs(pasta)

camera = cv2.VideoCapture(0)

def capturar_imagem():
    capturar_imagem.valor += 1 
    ret, imagem = camera.read()
    img = os.path.join(pasta, f"foto_capturada{capturar_imagem.valor}.png")
    cv2.imwrite(img, imagem)
    print("Imagem capturada e salva em:", img)

capturar_imagem.valor = 0

def on_click(x, y, button, pressed):
    if pressed:
        capturar_imagem()

def on_press(key):
    if key == keyboard.Key.space:
        capturar_imagem()

mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

key_listener = keyboard.Listener(on_press=on_press)
key_listener.start()

key_listener.join()
