from flask import Flask, render_template

app = Flask('honorarios', template_folder='./static')

@app.route("/", methods=['GET','POST'])
def index():
	return render_template('main.html')

@app.route("/honorarios")
def hon():
	return render_template('hon.html')
app.run(debug=True)