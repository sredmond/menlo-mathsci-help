import os
from flask import Flask

DEBUG=True
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

#Run the app
if __name__ == '__main__':
  app.run(debug=DEBUG)