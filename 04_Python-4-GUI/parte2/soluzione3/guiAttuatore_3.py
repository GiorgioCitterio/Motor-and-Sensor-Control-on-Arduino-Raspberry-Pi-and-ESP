import tkinter as tk
import serial

arduino = serial.Serial('COM3', 9600)
window = tk.Tk() 
window.geometry("570x100")
window.title("Controllo motore")
window.resizable(False, False)

def update_lbl(val):
    if int(val)<0:
        direzione = "I"
        v = ~int(val)+1
        stringaDaInviare = "{0};{1}".format(direzione,str(v)).encode()
        print(stringaDaInviare)
        arduino.write(stringaDaInviare)
    else:
        direzione = "A"
        stringaDaInviare = "{0};{1}".format(direzione,val).encode()
        print(stringaDaInviare)
        arduino.write(stringaDaInviare)

velocitaText_Label = tk.Label(window, text = "Velocità:")
velocitaText_Label.grid(row=1, column=0, pady=10)

scale = tk.Scale(window, orient="horizontal", length=510, from_=-255.0, to=255.0, command=update_lbl)
scale.grid(column=1, row=1)
scale.set(0)


if __name__ == "__main__":
    window.mainloop()