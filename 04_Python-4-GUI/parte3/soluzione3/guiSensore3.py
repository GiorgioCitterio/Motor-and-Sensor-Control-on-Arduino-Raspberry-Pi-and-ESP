import serial
import struct
import matplotlib.pyplot as plt
import matplotlib.animation as animation
IDCORRETTO = "BE"
DESTINATARIOCORRETTO = "D031"

arduino = serial.Serial('COM3', 9600)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def GrafFunz(i, xs, ys):
    xs.append(i)
    ys.append(valoreSensore)
    xs = xs[-20:]
    ys = ys[-20:]
    ax.clear()
    ax.plot(xs, ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title("Il grafico dei valori del sensore")
    plt.xlabel("X - Secondi")
    plt.ylabel("Y - Valori sensore")
    plt.axes([0, i, 0, 1023])
    return 0

for i in range(20):
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
        ani = animation.FuncAnimation(fig, GrafFunz, fargs=(xs, ys), interval=1000)
        plt.show()
        ani.save()
    else:
        print("pacchetto scartato")

