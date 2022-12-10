import tkinter as tk
import serial
import struct
IDCORRETTO = "BE"
DESTINATARIOCORRETTO = "D031"

arduino = serial.Serial('COM3', 9600)
window = tk.Tk() 
window.geometry("225x60")
window.title("Controllo sensore")
window.resizable(False, False)

def StampaValori(val):
    valoreText_Label = tk.Label(window, text = "Valore sensore = " + str(val), font=('Courier New', 10)).grid(row=1, column=0, pady=13)

def funz(window): 
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
        print("id e destinatario corretti")
        print(valoreSensore)
        s=int(valoreSensore)
        StampaValori(valoreSensore)
    else:
        print("pacchetto scartato")   
    window.after(1000, funz, window)

window.after(1000, funz, window)
 
if __name__ == "__main__":
    window.mainloop()