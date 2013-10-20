#!venv/bin/python
from app.models import *

#A list of (server_name, formal_name), tuples
classes = (('fresh_phys','Freshman Physics'),
	('ap_phys_b','AP Physics B'),
	('ap_phys_c','AP Physics C'),
	('conc_chem','Conceptual Chemistry'),
	('accel_chem','Accelerated Chemistry'),
	('ap_chem','AP Chemistry'),
	('o_chem','Organic Chemistry'),
	('bio','Biology'),
	('at_bio','AT Biology'),
	('anat_and_phys','Anatomy and Physiology'),
	('apes','AP Environmental Science'),
	('inter_alg','Intermediate Algebra'),
	('geo','Analytic Geometry'),
	('geoh','Analytic Geometry (H)'),
	('a2','Algebra 2'),
	('a2h','Algebra 2 (H)'),
	('fst','Functions, Statistics, and Trigonometry'),
	('pop','Principles of Precalculus'),
	('apc','Analytical Precalculus'),
	('pch','Precalculus (H)'),
	('calc','Intro to Calculus'),
	('calc_ab','AP Calculus AB'),
	('calc_bc','AP Calculus BC'),
	('stats','Statistics'),
	('ap_stats','AP Statistics'),
	('at_math','AT Math'),
	('intro_cs','Intro to Programming'),
	('ap_cs','AP Computer Science'),
	('at_cs','AT Computer Science'),
	('asr','ASR (H)'),
	('biotech','Biotechnology/Science Research'),
	('robo','Electronics/Robotics'),
	('eng1','Fundamentals of Engineering'),
	('eng2','Entrepreneurship Engineering'),
	('tool_safety','Design Thinking and Tool Safety (IS)'))

for cl in classes:
	sub = Subject(name=cl[0], title=cl[1])
	db.session.add(sub)

db.session.commit()