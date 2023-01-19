from flask import render_template
from flask import Flask
import json
import os

path = os.getcwd()+'/datiSensore.json'
app = Flask(__name__)
@app.route('/template/')
@app.route('/template/<name>')

def returnHtml(name = None):
        with open(path, 'r') as fp:
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
        return render_template('index.html')