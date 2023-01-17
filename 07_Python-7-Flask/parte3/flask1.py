from flask import Flask
import json

app = Flask(__name__)
@app.route('/')

def returnHtml():
        with open('05_Python-5-JSON/parte3/datiSensore.json', 'r') as fp:
                lista = json.load(fp)
        date = []
        valoriSensori = []
        stringa = "" 
        for i in range(len(lista)):
                date.append(lista[i]["DataOra"])
                valoriSensori.append(lista[i]["Valore"])
                stringa += "<tr><td>"+str(date[i])+"</td><td>"+str(valoriSensori[i])+"</td></tr>"
        stringaFinale= "<style>table, th, td{border: 1px solid black;}</style><body><table><tr><th>Data e ora</th><th>Valore</th></tr>"+stringa+"</table></body>"
        print(stringaFinale)
        return stringaFinale