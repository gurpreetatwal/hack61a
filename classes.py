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
	def __init__(self, name, class_size, day, enrolled, wait, wait_percent, enrolled_percent, units):
		self.name = name
		self.class_size = class_size
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

	def num_units(self):
		total = 0
		for i in self.lst:
			total += i.units
		self.numunits = total

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

	def unit_combos_phase1():
		units = 10.5

	    
	def can_phase_one():
		return [i for i in self.lst if i.enrolledpercent >= 100]


	def combo():
		def help_combo():
			return 0
		return help_combo()

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
        return []
    elif unit_cap >= courseload.num_units:
        return [courseload]
    elif courseload.is_empty:
    	print('courseload is_empty')
    	return []
    else: #unit_cap < courseload.num_units:
    	possible_course_loads = []
    	print('before append')
    	possible_course_loads.append(count_courses(unit_cap-courseload.get(0).units,courseload.remove_course(0)))
    	for i in possible_course_loads:
    		possible_course_loads[i].add_course(courseload.get(0))
    	possible_course_loads.append(count_courses(unit_cap,courseload.remove_course(0)))
    	return possible_course_loads

# certain classes wont fill up past phase 2, some will before phase 2 = phase 1 it

# if waitlist is 10% of class size, then waitlist at phase 2

# enrolled percentage, days since start of telebears, waitlisted, 
# enrolled number, max class size, title, 
# subtitle(e.g. "structure and interpretation of computer data")


schedule = {'cs61a': ['cs61a', 70, 70, 100, 70], 'physics7a': ['physics7a', 80, 80, 100, 70], 'math54': ['math54', 60, 60, 100, 70]}

phase_1_courses = []
phase_2_courses = []
adjustment_period_courses = []
do_not_attempt = []

def name(data):
	return data[0]

def enrollment1(data):
	return data[1]

def enrollment2(data):
	return data[2]

def limit(data):
	return data[3]

def threshold(data):
	return data[4]

def which_phase(data):
	#if it does not work, replace three instances of global with nonlocal
	global phase_1_courses
	global phase_2_courses
	global do_not_attempt
	if enrollment2(data) > threshold(data):
		if enrollment1(data) >= limit(data):
			do_not_attempt.append(name(data))
		else:
			phase_1_courses.append(name(data))
	else:
		phase_2_courses.append(name(data))

def final_soln(schedule):
	for key in schedule:
		which_phase(schedule[key])
