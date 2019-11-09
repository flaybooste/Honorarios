from flask import Flask, render_template, jsonify, request
from db import dbSQL
import json

app = Flask('honorarios', template_folder='./static')

@app.route("/", methods=['GET','POST'])
def index():
	return render_template('main.html')

@app.route("/honorarios")
def hon():
	empID = dbSQL().selectSQL()
	jsn = json.dumps(empID)
	return render_template('hon.html', ids = json.loads(jsn))

@app.route("/cadastro_empresas", methods=['GET','POST'])
def cadastro():
	if request.method == "POST":
		dbSQL().updateTblValor(round(float(request.form['valor']),2), request.form['id'])
	empID = dbSQL().selectSQL()
	return render_template('empresas.html' , empresas=empID)

@app.route("/empresa/<id>", methods=['GET',' POST'])
def empresa(id):
	emp = dbSQL().selectId(id)
	return render_template('empresa.html', emp=emp)

app.run(debug=True)
