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

	def num_units():
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

# certain classes wont fill up past phase 2, some will before phase 2 = phase 1 it

# if waitlist is 10% of class size, then waitlist at phase 2

# enrolled percentage, days since start of telebears, waitlisted, 
# enrolled number, max class size, title, 
# subtitle(e.g. "structure and interpretation of computer data")


