import os
from flask import Flask, request, render_template

DEBUG=True
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

#Run the app
if __name__ == '__main__':
  app.run(debug=DEBUG)