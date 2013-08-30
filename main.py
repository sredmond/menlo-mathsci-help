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

#Run the app
if __name__ == '__main__':
  app.run(debug=DEBUG)