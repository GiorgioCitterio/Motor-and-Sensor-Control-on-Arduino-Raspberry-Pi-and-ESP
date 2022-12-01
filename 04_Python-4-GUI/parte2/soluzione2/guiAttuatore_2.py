import tkinter as tk
import serial
direzione = b"A"
velocita = 0

arduino = serial.Serial('COM3', 9600)
window = tk.Tk() 
window.geometry("250x100")
window.title("Controllo motore")
window.resizable(False, False)

def DirezioneAvanti():
    global direzione
    direzione = b"A"
    arduino.write(direzione)

def DirezioneIndietro():
    global direzione
    direzione = b"I"
    arduino.write(direzione)

avantiDir_button = tk.Button(text="Avanti", command=DirezioneAvanti)
avantiDir_button.grid(row=0, column=0, sticky="W")

indietroDir_button = tk.Button(text="Indietro", command=DirezioneIndietro)
indietroDir_button.grid(row=0, column=2, sticky="E")

if __name__ == "__main__":
    window.mainloop()