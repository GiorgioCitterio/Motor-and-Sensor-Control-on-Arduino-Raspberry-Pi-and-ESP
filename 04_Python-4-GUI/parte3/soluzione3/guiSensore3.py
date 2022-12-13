import tkinter as tk
import serial
import struct
import matplotlib.pyplot as plt
import numpy as np 
IDCORRETTO = "BE"
DESTINATARIOCORRETTO = "D031"

arduino = serial.Serial('COM3', 9600)
window = tk.Tk()
listaDati = []

for i in range(30):
    val = arduino.read(32)
    pack = struct.unpack("2s 4s 4s 2s 4s 16s", val)
    print(pack)
    id=pack[0].decode()
    mittente=pack[1].decode()
    destinatario=pack[2].decode()
    tipo=pack[3].decode()
    valoreSensore=pack[4].decode()
    vuoto=pack[5].decode()
    if (id==IDCORRETTO)and(destinatario==DESTINATARIOCORRETTO):
        print("id e destinatario corretti, valore del sensore = "+valoreSensore)
        listaDati.append(valoreSensore)
    else:
        print("pacchetto scartato")    

def funz(window):
    
        x = np.linspace(-(2*np.pi), 2*np.pi, 100)
        y = np.sin(x)
        plt.plot(x, y, marker = "o", color = 'red')
        plt.title("Il grafico dei valori del sensore")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()
    

    



if __name__ == "__main__":
    window.mainloop()