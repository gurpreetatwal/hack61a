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

	def add_courseload(self, other): #adds two courseloads together
		return self.lst + other.lst
		
	def add_course(self,course): #adds a course to the courseload
		self.lst.append(course)
	
	def remove_course(self,course): #removes a course from the courseload
		self.lst.remove(course)


# certain classes wont fill up past phase 2, some will before phase 2 = phase 1 it

# if waitlist is 10% of class size, then waitlist at phase 2

# enrolled percentage, days since start of telebears, waitlisted, 
# enrolled number, max class size, title, 
# subtitle(e.g. "structure and interpretation of computer data")


