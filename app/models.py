from app import db
ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    #Information for logging in 
    email = db.Column(db.String(120), unique = True)
    hashed_password = db.Column(db.String(60));

    #Personal Information
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    grade = db.Column(db.SmallInteger)

    #Classes
    #classes_taking = db.Column(db.PickleType(mutable=True))
    #classes_can_help = db.Column(db.PickleType(mutable=True))
    
    #Administrative
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    
    #Requests Made
    requests = db.relationship('Request', backref = 'author', lazy = 'dynamic')

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
    class_for = db.Column(db.String(64)) #64 is arbitrary
    issue = db.Column(db.String(64)) #Again, arbitrary - this field holds "homework" or "project" or "test" or something else
    
    #Content
    body = db.Column(db.String(255)) #Max length for VARCHARs in older versions of SQL 
    extra_requests = db.Column(db.String(255))
    availability = db.Column(db.String(255))
    additional = db.Column(db.String(255))

    #Other
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)