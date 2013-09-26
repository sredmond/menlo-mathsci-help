#Stay away! No! Bad hacker.
'''This python script deletes all the current requests stored on the server.
It is purely for convenience (I'm generating a lot of requests while debugging)
PLEASE PLEASE PLEASE make me remove this script before pushing it to production
(although I'm not sure how a hacker could run arbitrary scripts on the server)'''
import os
import cPickle as cp
def clear_requests():
	path = os.path.join(os.getcwd(), 'requests/pickled_requests.txt')
	f = open(path, 'wb')
	cp.dump([], f)
	f.close()

def clear_messages():
	path = os.path.join(os.getcwd(), 'feedback/feedback.txt')
	f = open(path, 'wb')
	cp.dump([], f)
	f.close()