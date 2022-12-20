import serial
import struct
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
IDCORRETTO = "BE"
DESTINATARIOCORRETTO = "D031"

arduino = serial.Serial('COM3', 9600)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def animate(i, xs, ys):
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
        xs.append(i)
        ys.append(int(valoreSensore))
        xs = xs[-20:]
        ys = ys[-20:]
        ax.clear()
        ax.plot(xs, ys, marker="o")
        plt.title("Il grafico dei valori del sensore")
        plt.xlabel("X - Secondi")
        plt.ylabel("Y - Valori sensore")
        plt.axes([0, i, 0, 1023])
    else:
        print("pacchetto scartato")

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()


