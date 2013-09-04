##The main library for the Menlo Math-Sci Help Center Web Application
##The two high level classes are Requests and People
import time
#A request
class Request:
	def __init__(self, params):
		#User info
		self.first_name = params['first_name'].capitalize()
		self.last_name = params['last_name'].capitalize()
		self.grade = params['grade']
		self.email = params['email']

		#Classes
		self.classes=params['all_classes']
		
		#Type of issue
		self.issue = params['issue']

		#Other info
		self.challenge = params['challenge']
		self.requests = params['requests']
		self.availability = params['availability']
		self.additional = params['additional']

		#Time the server received the request (technically, these won't be the same value (the second one calls time.localtime() as it is interpreted)
			#but I don't see that as a problem. It will be a back-compatability problem though...
		self.time = time.time()
		self.pretty_time = time.strftime("%a, %b. %d, %Y at %I:%M:%S %p")