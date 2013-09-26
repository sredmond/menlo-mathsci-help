##The main library for the Menlo Math-Sci Help Center Web Application
##The two high level classes are Requests and People
import time

classesMap = {"fresh_phys":"Freshman Physics", 
	"ap_phys_b":"AP Physics B", 
	"ap_phys_c":"AP Physics C", 
	"conc_chem":"Conceptual Chemistry", 
	"accel_chem":"Accelerated Chemistry", 
	"ap_chem":"AP Chemistry", 
	"o_chem":"Organic Chemistry", 
	"bio":"Biology", 
	"at_bio":"AT Biology", 
	"anat_and_phys":"Anatomy and Physiology", 
	"apes":"AP Environmental Science", 
	"inter_alg":"Intermediate Algebra", 
	"geo":"Analytic Geometry", 
	"geoh":"Analytic Geometry (H)", 
	"a2":"Algebra 2", 
	"a2h":"Algebra 2 (H)", 
	"fst":"Functions, Statistics, and Trigonometry", 
	"pop":"Principles of Precalculus", 
	"apc":"Analytical Precalculus", 
	"pch":"Precalculus (H)", 
	"calc":"Intro to Calculus", 
	"calc_ab":"AP Calculus AB", 
	"calc_bc":"AP Calculus BC", 
	"stats":"Statistics", 
	"ap_stats":"AP Statistics", 
	"at_math":"AT Math", 
	"intro_cs":"Intro to Programming", 
	"ap_cs":"AP Computer Science", 
	"at_cs":"AT Computer Science", 
	"asr":"ASR (H)", 
	"biotech":"Biotechnology/Science Research", 
	"robo":"Electronics/Robotics", 
	"eng1":"Fundamentals of Engineering", 
	"eng2":"Entrepreneurship Engineering", 
	"tool_safety":"Design Thinking and Tool Safety (IS)"}

issue_map = {"hw": "homework",
	"test": "a test",
	"proj": "a project"}

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
		self.pretty_classes=[classesMap[cl] for cl in self.classes]
		
		#Type of issue
		self.issue = params['issue']
		self.issue_str = params['issue_str']

		#Mandatory info
		self.title = params['title']
		self.challenge = params['challenge']
		
		#Optional info
		self.requests = params['requests']
		self.availability = params['availability']
		self.additional = params['additional']

		#Time
		current_time = time.localtime()
		self.time = time.mktime(current_time) #Could be used as an ID perhaps?
		self.pretty_time = time.strftime("%a, %b. %d, %Y at %I:%M:%S %p", current_time)

class Tutor:
	def __init__(self, params):
		#User info
		self.first_name = params['first_name'].capitalize()
		self.last_name = params['last_name'].capitalize()
		self.grade = params['grade']
		self.email = params['email']

		#Classes
		self.classes=params['all_classes']
		self.pretty_classes=[classesMap[cl] for cl in self.classes]

		#Time
		current_time = time.localtime()
		self.time = time.mktime(current_time) #Could be used as an ID perhaps?
		self.pretty_time = time.strftime("%a, %b. %d, %Y at %I:%M:%S %p", current_time)


def matches(req, classes):
	for cl in req.classes:
		if cl in classes:
			return True
	return False

#Right now, a message is just two strings - a title and content... in the future it might be more.
class Message:
	#Initialize the message
	def __init__(self, params):
		self.title = params['title']
		self.content = params['feedback']
		self.type = params['type']

	def __str__(self):
		return "message[title={0}, content={1}]".format(self.title, self.content)