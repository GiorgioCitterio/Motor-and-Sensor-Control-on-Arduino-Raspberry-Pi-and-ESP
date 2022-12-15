import json
lista = []
lista2 = []

for i in range(7):
    #dataOra = input("inserire la data e l'ora: ")
    #val = int(input("inserire il valore: "))
    #dizionario = {'DataOra': dataOra, 'Valore' : val}
    dizionario = {'DataOra': i+1, 'Valore' : i+1}
    lista.append(dizionario)

print("\n")
data = json.dumps(lista)
file = open('05_Python-5-JSON/parte2/esDiz1.json', 'w')
file.write(data)
file.close()

with open('05_Python-5-JSON/parte2/esDiz1.json', 'r') as fp:
    lista2 = json.load(fp)

print(lista2[-5:])
