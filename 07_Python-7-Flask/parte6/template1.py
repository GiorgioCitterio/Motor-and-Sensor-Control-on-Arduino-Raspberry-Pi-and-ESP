from flask import render_template
from flask import Flask
import json
import os

path = os.getcwd()+'/datiSensore.json'
app = Flask(__name__)
@app.route('/')

def returnHtml():
        with open(path, 'r') as fp:
                lista = json.load(fp)
        return render_template('index.html', dizValori=lista)