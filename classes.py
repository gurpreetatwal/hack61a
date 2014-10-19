#Class defining "class"
#test
class Course(object):
	def __init__(self, lst): #lst = list of attributes of each class
		self.name = lst[0]
		self.units = lst[1]
		self.enrolled = lst[2]
		self.class_size = lst[3]
		self.days_past = lst[4]
		self.enrolledpercent = lst[5]

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
		return total

	def fullest_to_emptiest():
		self.lst = sorted(self.lst, key = lambda course: course.enrolledpercent)

	def most_units_to_least():
		self.lst = sorted(self.lst, key = lambda course: course.units)

	def unit_combos_phase1():
		units = 10.5

	    
	def can_phase_one():
		return [i for i in self.lst if i.enrolledpercent >= 100]


	def combo():
		def help_combo():
			return 0
		return help_combo()


	def unit_combos_phase2():
		phase1_lst = unit_combos_phase1


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


