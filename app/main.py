import os
from flask import Flask, request, render_template, url_for, redirect, flash #The main module that does a lot of hidden work
from flask.ext.sqlalchemy import SQLAlchemy #Our SQL helper
import cPickle as cp #A workaround to SQL for now
from mshc_lib import * #Our custom library
import bcrypt

DEBUG=True #CHANGE THIS TO FALSE ON MAJOR RELEASES
app = Flask(__name__)
app.secret_key=os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

pickle_path = os.path.join(os.getcwd(), 'requests/pickled_requests.txt')
feedback_path = os.path.join(os.getcwd(), 'feedback/feedback.txt')


##DECLARE DATABASE MODELS##
class Request(db.Model):
	request_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, unique=True)
	description = db.Column(db.String, unique=True)
	class_name = db.Column(db.String, unique=True)
	user = db.relationship('User', backref='request')

	def __init__(self, username, email, class_name):
		self.username = username
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.title

class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True)
	pw_hash = db.Column(db.String, unique=True)

	first_name = db.Column(db.String(50), unique=True)
	last_name = db.Column(db.String(50), unique=True)
	grade = db.Column(db.Integer, unique=True)
	email = db.Column(db.String(150), unique=True)

	##Classes the user is taking

	##Classes the user can Tutor

	##Requests I have made


	def __init__(self, username, email):
		self.username = username
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.username

##END DECLARE DB MODELS####

#DATABASE STUFF

#Run the app
if __name__ == '__main__':
  app.run(debug=DEBUG)