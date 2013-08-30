import os
from flask import Flask, request, render_template, url_for

DEBUG=True
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/learn')
def learn():
	return render_template('learn.html')

@app.route('/teach')
def teach():
	return render_template('teach.html')

#Respond to form requests
@app.route('/submitLearner')
def submitLearner():
	info = request.form
	return render_template('home.html', console=str(info))

@app.route('/submitTeacher')
def submitTeacher():
	info = request.form
	return render_template('home.html', console=str(info))

#Run the app
if __name__ == '__main__':
  app.run(debug=DEBUG)