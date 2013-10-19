from app import db
import bcrypt
ROLE_USER = 0
ROLE_ADMIN = 1

#Relationship between users and subjects
tutorsForSubjects = db.Table('tutorsForSubjects',
    db.Column('tutor_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'))
)

learnersForSubjects = db.Table('learnersForSubjects',
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
    
    #Administrative
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    
    #Requests Made
    requests = db.relationship('Request', backref = 'author', lazy = 'dynamic')

    subjectsITutor = db.relationship('Subject', 
        secondary = tutorsForSubjects, 
        backref = db.backref('tutors', lazy = 'dynamic'), 
        lazy = 'dynamic')

    #Add classes
    def teachSubject(self, subject):
        if not self.is_teaching(subject):
            self.subjectsITutor.append(subject)
            return self

    def unteach(self, subject):
        if self.is_teaching(subject):
            self.subjectsITutor.remove(subject)
            return self

    def is_teaching(self, subject):
        return self.subjectsITutor.filter(tutorsForSubjects.c.subject_id == subject.id).count() > 0

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
    name = db.Column(db.String(100))

    #List of requests about this subject
    requests = db.relationship('Request', backref = 'subject', lazy = 'dynamic')

    def __repr__(self):
        return '<Subject %r>' % (self.name)

