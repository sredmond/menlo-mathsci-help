from app import models
from app import db

u = models.User(first_name="Sam", last_name="Redmond")
s = models.Subject(name="math")
db.session.add(u)
db.session.commit()
db.session.add(u.teachSubject(s))
db.session.commit()
print "Got here"
for t in s.tutors:
	print t
for sub in u.subjectsITutor:
	print sub