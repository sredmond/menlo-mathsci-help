import os

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SECRET_KEY = os.urandom(24)

#Email
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'mathsciencehelpcenter@gmail.com'
MAIL_PASSWORD = '1uattw3ba1b'

MAIL_DEFAULT_SENDER = ('Math & Science Help Center', 'mathsciencehelpcenter@gmail.com')
REPLY_RECEIVER = ('Sam Redmond', 'sam.redmond+mshc@menloschool.org')

# administrator list
ADMINS = ['sam.redmond@menloschool.org']