##The main library for the Menlo Math-Sci Help Center Web Application
##The two high level classes are Requests and People
import time

classes = {"fresh_phys":"Freshman Physics", 
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

#Right now, a message is just two strings - a title and content... in the future it might be more.
class Message:
	#Initialize the message
	def __init__(self, params):
		self.title = params['title']
		self.content = params['feedback']

	def __str__(self):
		return "message[title={0}, content={1}]".format(self.title, self.content)