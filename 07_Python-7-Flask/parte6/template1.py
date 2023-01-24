from flask import render_template
from flask import Flask
import json
import os

pathJ = os.getcwd()+'/datiSensore.json'
pathH = os.getcwd()+'/index.html'
app = Flask(__name__)
@app.route('/')

def returnHtml():
        with open(pathJ, 'r') as fp:
                lista = json.load(fp)
        return render_template(pathH, dizValori=lista)