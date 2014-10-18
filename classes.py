# dct = data.py
# lst = #list of names of classes to take
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

	def num_units(self):
		total = 0
		for i in self.lst:
			total += i.units
		return total

	def fullest_to_emptiest(self):
		self.lst = sorted(self.lst, key = lambda course: course.enrolledpercent)

	def most_units_to_least(self):
		self.lst = sorted(self.lst, key = lambda course: course.units)

	def count_courses(courses,amount=10.5):
	
	    temp_lst = []
	    def help_count(amount,part):
	    	if amount <= 0: #hit max units
	    	    return []
	    	elif amount > 0: #still can add units to phase 1
	    	    
	    		
	    for i in courses:
	    	temp_lst.append(help_count(amount,part))
	    return temp_lst
	    
	    def help_change(amount, part):
	        if amount == 0:
	            return 1
	        if amount == part:
	            return 1
	        elif amount < part:
	            return 0
	        else:
	            return help_change(amount-part.lst[1].units,part)+help_change(amount,part*2)
	    return help_change(amount,courses.lst)
	    possible_courses = course_load
	    
	    possible_courses.print()

	def can_phase_one(self):
		return [i for i in self.lst if i.enrolledpercent >= 100]


# certain classes wont fill up past phase 2, some will before phase 2 = phase 1 it

# if waitlist is 10% of class size, then waitlist at phase 2

# enrolled percentage, days since start of telebears, waitlisted, 
# enrolled number, max class size, title, 
# subtitle(e.g. "structure and interpretation of computer data")


