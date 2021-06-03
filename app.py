from flask import Flask, render_template, redirect, url_for, request
import pickle
import numpy as np 

model = pickle.load(open('heart.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict', methods=['POST'])
def prediction():
	age = request.form.get('age')
	gender = request.form.get('gender')
	height = request.form.get('height')
	weight = request.form.get('weight')
	aphi = request.form.get('aphi')
	aplo = request.form.get('aplo')
	cho = request.form.get('cho')
	glu = request.form.get('glu')
	smoke = request.form.get('smoke')
	alco = request.form.get('alco')
	active = request.form.get('active')

	arr = [[age,gender,height,weight,aphi,aplo,cho,glu,smoke,alco,active]]

	pred = model.predict(arr)
	return render_template('result.html', prediction=pred)

@app.route('/tracker')
def tracker():
	return render_template('tracker.html')

@app.route('/helpline')
def helpline():
	return render_template('helpline.html')

@app.route('/aboutproject')
def aboutproject():
	return render_template('aboutproject.html')

@app.route('/aboutus')
def aboutus():
	return render_template('aboutus.html')

if __name__ == "__main__":
	app.run(debug=True)