from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user #current_user is a Flask-Login global, so we copy it into g.user so that all requests and HTML templates have access to it
    
@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template('index.html',
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
    return render_template('login.html', 
        title = 'Sign In',
        form = form)

def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# #Load pages
# @app.route('/')
# def main():
# 	return render_template('home.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or \
#                 request.form['password'] != 'secret':
#             error = 'Invalid credentials'
#         else:
#             flash('You were successfully logged in')
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)

# #Note that this URL rule keeps 
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
# 	if request.method == 'POST':
# 		return render_template('home.html', console=request.form)
# 	return render_template('signup.html')


# @app.route('/learn')
# def learn():
# 	return render_template('learn.html')

# @app.route('/teach')
# def teach():
# 	return render_template('teach.html')

# @app.route('/show_all_requests')
# def show_all_requests():
# 	read = open(pickle_path, 'rb')
# 	current_requests = cp.load(read)
# 	read.close()
# 	return render_template('show_all_requests.html', requests=current_requests)

# @app.route('/feedback')
# def feedback():
# 	return render_template('feedback.html')

# @app.route('/view_messages')
# def view_messages():
# 	read = open(feedback_path, 'rb')
# 	all_messages = cp.load(read)
# 	read.close()
# 	return render_template('view_messages.html', messages=all_messages)

# #Set URL rules for modals (?!)
# @app.route('/modal_overview')
# def modal_overview():
# 	return render_template('modal_overview.html')

# #Respond to form requests
# @app.route('/submitLearner', methods=['POST'])
# def submitLearner():
# 	info = request.form

# 	params={}
# 	#User information
# 	params['first_name'] = info['first_name']
# 	params['last_name'] = info['last_name']
# 	params['grade'] = int(info['grade'])
# 	params['email'] = info['email'] + "@menloschool.org"

# 	#Classes
# 	sci_classes = info.getlist('science')
# 	math_classes = info.getlist('math')
# 	other_classes = info.getlist('cs_as')
# 	all_classes = []
# 	all_classes.extend(sci_classes)
# 	all_classes.extend(math_classes)
# 	all_classes.extend(other_classes)
# 	params['all_classes'] = filter(lambda x: x in classesMap, all_classes) #Will only store values that are in our class list
	
	
# 	#Type of issue
# 	issue = info['issue']
# 	params['issue'] = issue
# 	if issue in issue_map:
# 		params['issue_str'] = issue_map[issue]
# 	elif issue == 'other':
# 		params['issue_str'] = info['elaboration'].lower()
# 	else:
# 		params['issue_str'] = 'Invalid option'

# 	#Mandatory info
# 	params['title'] = info['title']
# 	params['challenge'] = info['challenge']
	
# 	#Optional info
# 	params['requests'] = info['requests']
# 	params['availability'] = info['availability']
# 	params['additional'] = info['additional_comments']

# 	#THIS IS BAD AND SLOW. CHANGE IT LATER. 
# 	req = Request(params)
# 	read = open(pickle_path, 'rb')
# 	current_requests = cp.load(read)
# 	read.close()
# 	current_requests = [req] + current_requests #I do it in this order so the requests display chronologically
# 	write = open(pickle_path, 'wb')
# 	cp.dump(current_requests, write)
# 	write.close()

# 	return render_template('show_all_requests.html', requests=current_requests)

# @app.route('/submitTeacher', methods=['POST'])
# def submitTeacher():
# 	info = request.form

# 	params={}

# 	#User information
# 	params['first_name'] = info['first_name']
# 	params['last_name'] = info['last_name']
# 	params['grade'] = int(info['grade'])
# 	params['email'] = info['email'] + "@menloschool.org"

# 	#Classes
# 	sci_classes = info.getlist('science')
# 	math_classes = info.getlist('math')
# 	other_classes = info.getlist('cs_as')
# 	all_classes = []
# 	all_classes.extend(sci_classes)
# 	all_classes.extend(math_classes)
# 	all_classes.extend(other_classes)
# 	params['all_classes'] = filter(lambda x: x in classesMap, all_classes) #Will only store values that are in our class list

# 	t = Tutor(params)
# 	read = open(pickle_path, 'rb')
# 	current_requests = cp.load(read)
# 	read.close()

# 	filtered_requests = []
# 	for req in current_requests:
# 		if matches(req, all_classes):
# 			filtered_requests.append(req)

# 	return render_template('show_all_requests.html', requests=filtered_requests, tutor=t)

# @app.route('/submitMessage', methods=['POST'])
# def submitMessage():
# 	info = request.form
# 	params = {}

# 	params['title'] = info['title']
# 	params['feedback'] = info['feedback']
# 	params['type'] = info['feedback_type']
	
# 	message = Message(params)

# 	read = open(feedback_path, 'rb')
# 	all_messages = cp.load(read)
# 	read.close()
	
# 	all_messages = [message] + all_messages
	
# 	write = open(feedback_path, 'wb')
# 	cp.dump(all_messages, write)
# 	write.close()

# 	return render_template('home.html', console="Thanks for submitting feedback!")