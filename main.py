# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request
from db import dbSQL
import json
import os


app = Flask('honorarios', template_folder='./static', static_folder='./static')

@app.route("/", methods=['GET','POST'])
def index():
	return render_template('main.html')

@app.route("/honorarios")
def hon():
        empID = dbSQL().selectSQL()
        jsn = json.dumps(empID)
        return render_template('hon.html',ids = json.loads(jsn))

@app.route("/cadastro_empresas", methods=['GET','POST'])
def cadastro():
        if request.method == "POST":
            print(request.form['valor'].replace(',','.'))
            dbSQL().updateTblValor(round(float(request.form['valor'].replace(",","."),2), request.form['id']))
        empID = dbSQL().selectSQL()
        return render_template('empresas.html' , empresas=empID)

@app.route("/empresa/<id>", methods=['GET',' POST'])
def empresa(id):
	emp = dbSQL().selectId(id)
	return render_template('empresa.html', emp=emp)

@app.route("/teste")
def teste():
    return render_template('barbudo.html')

@app.route("/paty")
def paty():
    return 'te amo muito'

app.run(port=5000, host='0.0.0.0',debug=True)
