##The main library for the Menlo Math-Sci Help Center Web Application
##The two high level classes are Requests and People

#A request
class Request:
	def __init__(self, params):
		#User info
		self.first_name = params['first_name']
		self.last_name = params['last_name']
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