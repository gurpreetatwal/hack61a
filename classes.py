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
	def __init__(self, name, class_size, lst): #lst = list of attributes of each class
		self.name = name
		self.class_size = class_size
		self.enrolledpercent = lst[0]
		self.enrolled = lst[1]
		self.day = lst[2]
		self.waitlist = lst[3]
		self.waitlist_percent = lst[5]

		

#################################
#Class defining list of classes you are taking
class CourseLoad(Course):
	def __init__(self, lst): #lst = list of Courses
		self.lst = lst
<<<<<<< HEAD
		total = 0
		for i in self.lst:
			total += i.units
		self.num_units = total

	def num_units(self):
		total = 0
=======
>>>>>>> 0ca1b8d5f915f57081ed24ff7925e6bb60d2de55
		for i in self.lst:
			total += i.units
		self.numunits = total

	def get(self, index):
		if index > len(self.lst):
			return "Error: exceeded length of list"
		else:
			return self.lst[index]

	def fullest_to_emptiest(self):
		self.lst = sorted(self.lst, key = lambda course: course.enrolledpercent)

	def most_units_to_least(self):
		self.lst = sorted(self.lst, key = lambda course: course.units)

<<<<<<< HEAD
	def unit_combos_phase1():
		units = 10.5

	    
	def can_phase_one():
		return [i for i in self.lst if i.enrolledpercent >= 100]


	def combo():
		def help_combo():
			return 0
		return help_combo()

=======
	def add_courseload(self, other): #adds two courseloads together
		return self.lst + other.lst
		
	def add_course(self,course): #adds a course to the courseload
		self.lst.append(course)
	
	def remove_course(self,course): #removes a course from the courseload
		self.lst.remove(course)
>>>>>>> 0ca1b8d5f915f57081ed24ff7925e6bb60d2de55



def count_courses(courses,unit_cap=10.5):
    """Return the number of ways to make change for unit_cap.

    >>> course1 = Course(['anthro',4,10,25,5,.4])
   	>>> course2 = Course(['german',4,13,25,5,.52])
   	>>> course3 = Course(['math',4,127,500,5,.254])
   	>>> course4 = Course(['spanish',5,9,20,5,.45])
    >>> courseloadA = CourseLoad([course1,course2,course3,course4])
    >>> count_courses(courseloadA,10.5)
    [[course4,course1],[course3,course1],[course2,course1],[course4,course2],[course3,course2],[course4,course3]]
    """
    def help_change(unit_cap, courseload):
        if unit_cap == 0:
            pass
        elif unit_cap == courseload.num_units:
            return courseload
        else: #unit_cap < courseload.num_units:
        	possible_course_loads = help_change(unit_cap-courseload.get(0).units,courseload.remove(0))
        	for i in possible_course_load:
        		possible_course_load.add(courseload.get(0))
        	possible_list.append(possible_course_load)
        	possible_list.append(help_change(unit_cap,courseload.remove(0)))
        	return possible_list
    return help_change(unit_cap,courses)

# certain classes wont fill up past phase 2, some will before phase 2 = phase 1 it

# if waitlist is 10% of class size, then waitlist at phase 2

# enrolled percentage, days since start of telebears, waitlisted, 
# enrolled number, max class size, title, 
# subtitle(e.g. "structure and interpretation of computer data")


phase_1_courses = []
phase_2_courses = []
adjustment_period_courses = []
do_not_attempt = []

def which_phase(course, enrollment1, enrollment2, limit, threshold):
	#if it does not work, replace three instances of global with nonlocal
	global phase_1_courses
	global phase_2_courses
	global do_not_attempt
	if enrollment2 > threshold:
		if enrollment1 >= limit:
			do_not_attempt.append(course)
		else:
			phase_1_courses.append(course)
	else:
		phase_2_courses.append(course)
