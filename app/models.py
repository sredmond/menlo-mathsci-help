from app import db
import bcrypt
ROLE_USER = 0
ROLE_ADMIN = 1
ROLE_SUPER = 2

#Tutors are in the 'left' column, subjects are in the 'right'
tutorsSubjects = db.Table('tutorsSubjects',
    db.Column('tutor_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'))
)

#Learners are in the 'left' column, subjects are in the 'right'
learnersSubjects = db.Table('learnerSubjects',
    db.Column('learner_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    #Information for logging in 
    email = db.Column(db.String(120), unique = True)
    hashed_password = db.Column(db.String(60));

    #Personal Information
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    grade = db.Column(db.SmallInteger)
    
    #Timing
    created = db.Column(db.DateTime)
    last_logged_in = db.Column(db.DateTime)

    #Administrative
    role = db.Column(db.SmallInteger, default = ROLE_SUPER)
    
    #Requests Made
    requests = db.relationship('Request', backref = 'author')

    #I can ask for <user>.tutoring and <subject>.tutors
    tutoring = db.relationship('Subject', 
        secondary = tutorsSubjects, 
        backref = db.backref('tutors'))

    #I can ask for <user>.learning and <subject>.learners
    learning = db.relationship('Subject', 
        secondary = learnersSubjects, 
        backref = db.backref('learners'))

    #Make a request
    def make_request(self, request):
        self.requests.append(request)

    #Add classes to tutor
    def tutor_subject(self, subject):
        if not self.is_tutoring(subject):
            self.tutoring.append(subject)
            return self

    def untutor_subject(self, subject):
        if self.is_tutoring(subject):
            self.tutoring.remove(subject)
            return self

    def is_tutoring(self, subject):
        return subject in self.tutoring

    #Add classes to learn
    def learn_subject(self, subject):
        if not self.is_learning(subject):
            self.learning.append(subject)
            return self

    def unlearn_subject(self, subject):
        if self.is_learning(subject):
            self.learning.remove(subject)
            return self

    def is_learning(self, subject):
        return subject in self.learning
    
    #Necessary methods for Flask-Login
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def verify_password(self, password):
    	return bcrypt.hashpw(password, self.hashed_password) == self.hashed_password

    def __repr__(self):
        return '<User %r>' % (self.email)

class Request(db.Model):
    id = db.Column(db.Integer, primary_key = True)


    #A form of meta data
    title = db.Column(db.String(100))
    issue = db.Column(db.String(64)) #Again, arbitrary - this field holds "homework" or "project" or "test" or something else
    
    #Content
    body = db.Column(db.String(1023))
    extra_requests = db.Column(db.String(255))
    availability = db.Column(db.String(255))
    additional = db.Column(db.String(255))

    #Other
    timestamp = db.Column(db.DateTime)

    #References
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))

    def __repr__(self):
        return '<Request %r>' % (self.body)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    title = db.Column(db.String(64))


    #List of requests about this subject
    requests = db.relationship('Request', backref = 'subject')

    def add_request(self, request):
        self.requests.append(request)


    def __repr__(self):
        return '<Subject %r>' % (self.title)

