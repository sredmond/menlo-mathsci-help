import os
from flask import Flask, request, render_template, url_for
import cPickle as cp
from mshc_lib import *

DEBUG=True
app = Flask(__name__)

#Load pages
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
@app.route('/submitLearner', methods=['POST'])
def submitLearner():
	info = request.form

	params={}
	#User information
	params['first_name'] = info['first_name']
	params['last_name'] = info['last_name']
	params['grade'] = int(info['grade'])
	params['email'] = info['email'] + "@menloschool.org"

	#Classes
	sci_classes = info.getlist('science')
	math_classes = info.getlist('math')
	other_classes = info.getlist('cs_as')
	all_classes = []
	all_classes.extend(sci_classes)
	all_classes.extend(math_classes)
	all_classes.extend(other_classes)
	params['all_classes'] = all_classes
	
	#Type of issue
	issue = info['issue']
	params['issue'] = issue

	#Other info
	params['challenge'] = info['challenge']
	params['requests'] = info['requests']
	params['availability'] = info['availability']
	params['additional'] = info['additional_comments']

	#THIS IS BAD AND SLOW. CHANGE IT LATER. 
	req = Request(params)
	path = os.path.join(os.getcwd(), 'requests/pickled_requests.txt')
	read = open(path, 'rb')
	current_requests = cp.load(read)
	read.close()
	current_requests = [req] + current_requests #I do it in this order so the requests display chronologically
	write = open(path, 'wb')
	cp.dump(current_requests, write)
	write.close()

	return render_template('show_all_requests.html', requests=current_requests)

@app.route('/submitTeacher', methods=['POST'])
def submitTeacher():
	info = request.form
	return render_template('home.html', console=str(info))

#Run the app
if __name__ == '__main__':
  app.run(debug=DEBUG)