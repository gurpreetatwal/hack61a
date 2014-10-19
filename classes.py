# dct = data.py
# input day of phase1, phase2
# lst = #input names of classes to take
# #reenter classes if class name was inputted wrong or not found
# lst2 = [dct.get(i) for i in lst]
# lst3 = []
# count = 0
# for i in lst2:
#     lst3.append(Course(lst[count],lst2[1],lst2[2]))
# c = CourseLoad(lst3)

#Class defining "class"
#test
class Course(object):
	def __init__(self, name, day, enrolled, wait, wait_percent, enrolled_percent, units, max_enroll):
		self.name = name
		self.class_size = max_enroll
		self.day = day
		self.enrolled = enrolled
		self.wait = wait
		self.wait_percent = wait_percent
		self.enrolled_percent = enrolled_percent
		self.units = units


		

#################################
#Class defining list of classes you are taking
class CourseLoad(Course):
	def __init__(self, lst): #lst = list of Courses
		self.lst = lst
		total = 0
		for i in self.lst:
			total += i.units
		self.num_units = total

	def is_empty(self):
		return len(self.lst)<=0

	def get(self, index):
		if index > len(self.lst) or not self.is_empty():
			return "Error: exceeded length of list"
		else:
			return self.lst[index]

	def fullest_to_emptiest(self):
		self.lst = sorted(self.lst, key = lambda course: course.enrolledpercent)

	def most_units_to_least(self):
		self.lst = sorted(self.lst, key = lambda course: course.units)

	def add_courseload(self, other): #adds two courseloads together
		return self.lst + other.lst
		
	def add_course(self,course): #adds a course to the courseload
		self.lst.append(course)
	
	def remove_course(self,course): #removes a course from the courseload
		self.lst.remove(course)



def count_courses(courseload,unit_cap=21):
	"""Return the number of ways to make change for unit_cap.

	>>> course1 = Course('anthro',25,[.4,10,5,0,0,4])
	>>> course2 = Course('german',25,[.52,24,5,0,0,4])
	>>> course3 = Course('math',500,[.254,127,5,0,0,4])
	>>> course4 = Course('spanish',20,[.45,9,5,0,0,5])
	>>> courseloadA = CourseLoad([course1,course2,course3,course4])
	>>> count_courses(courseloadA,10.5)
	[[course4,course1],[course3,course1],[course2,course1],[course4,course2],[course3,course2],[course4,course3]]
	"""
	if unit_cap == 0:
		print('unit_cap is 0')
		return []
	elif unit_cap >= courseload.num_units:
		print('cap is large enuf')
		return [courseload]
	elif courseload.is_empty():
		print('courseload is_empty')
		return []
	elif courseload.get(0).units>unit_cap:
		return []
	else: #unit_cap < courseload.num_units:
		possible_course_loads = []
		print('before append')
		course0 = courseload.get(0)
		courseload.remove_course(0)
		possible_course_loads.append(count_courses(courseload, unit_cap -course0.units))
		for i in possible_course_loads:
			possible_course_loads[i].add_course(course0)
		possible_course_loads.append(count_courses(courseload,unit_cap))
		return possible_course_loads

#schedule = {'cs61a': ['cs61a', 100, 100, 100], 'physics7a': ['physics7a', 80, 100, 100], 'math54': ['math54', 80, 80, 100]}

schedule = []

phase_1_courses = []
phase_2_courses = []
do_not_attempt = []

def name(course):
	#return course[0]
	return course.name

def enrollment1(course):
	#return course[1]/course[3]
	return course.enrolled1/course.class_size

def enrollment2(course):
	#return course[2]/course[3]
	return course.enrolled2/course.class_size

def limit(course):
	#return course[3]
	return course.class_size

def list_annex(course):
	#if it does not work, replace three instances of global with nonlocal
	threshold = .9
	global phase_1_courses
	global phase_2_courses
	global do_not_attempt
	if enrollment2(course) > threshold:
		if enrollment1(course) >= threshold:
			do_not_attempt.append(name(course))
		else:
			phase_1_courses.append(name(course))
	else:
		phase_2_courses.append(name(course))

def which_phase(schedule):
	for key in schedule:
		list_annex(schedule[key])

#dictionary = {}

#def make_dictionary(course_list):
	#for i in course_list:
