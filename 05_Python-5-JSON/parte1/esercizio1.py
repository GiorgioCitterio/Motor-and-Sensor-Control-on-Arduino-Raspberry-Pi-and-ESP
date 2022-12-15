lista = []

for i in range(7):
    dataOra = input("inserire la data e l'ora: ")
    val = int(input("inserire il valore: "))
    dizionario = {'DataOra': dataOra, 'Valore' : val}
    lista.append(dizionario)

print("\n")
print(lista[-5:])