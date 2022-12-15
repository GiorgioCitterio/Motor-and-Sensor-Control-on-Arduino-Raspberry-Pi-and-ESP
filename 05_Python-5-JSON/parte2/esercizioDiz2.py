import json
lista = []

for i in range(7):
    dataOra = input("inserire la data e l'ora: ")
    val = int(input("inserire il valore: "))
    dizionario = {'DataOra': dataOra, 'Valore' : val}
    lista.append(dizionario)

print("\n")
data = json.dumps(lista)
file = open('05_Python-5-JSON/parte2/esDiz.json', 'a')
file.write(data)
file.close()
