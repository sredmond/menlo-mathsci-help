from flask import Flask, render_template, request, url_for

DEBUG = True
app = Flask(__name__)

@app.route('/')
def main():
  return "Hello World!"

#Run the app
if __name__ == '__main__':
  app.run(debug=DEBUG)