from data_new import berkeley_classes
from bs4 import BeautifulSoup
from classes import Course,CourseLoad
import urllib.request

print("Welcome to Tele-Bears Advisor!")
print("Tele-Bears Advisors looks at last semester's enrollment data and determines")
print("which classes you should Phase 1 and which ones you should Phase 2")
user_classes = input("Please enter all the classes you plan to take this semester, seperated by a spaces.\n")
user_day1 = input("Please enter your Phase1 Tele-Bears day:  ")
user_day2 = input("Please enter your Phase2 Tele-Bears day:  ")

user_classes = list(user_classes.upper().split())
class_data = {}

i = 0
while i < len(user_classes):
	current_class = user_classes[i].upper()
	if current_class in berkeley_classes:

		# Get all sections
		class_value = berkeley_classes[current_class]
		sections = urllib.request.urlopen("http://www.berkeleytime.com/enrollment/sections/" + str(class_value) + "/").read()
		data = eval(BeautifulSoup(sections).text)

		# Get enrollment info
		year, semester = data[-1]['year'], data[-1]['semester']
		print(current_class ,semester, year)
		bt_data = urllib.request.urlopen("http://www.berkeleytime.com/enrollment/aggregate/" + str(class_value) + "/" + semester + "/" + year + "/").read()
		data = eval(BeautifulSoup(bt_data).text)

		# Manage data
		class_data[current_class] ={}
		data = data['data']
		
		for day in data:
			day_key = day['day']
			enrolled = day['enrolled']
			waitlisted = day['waitlisted']
			wait_percent = day['waitlisted_percent']
			enro_percent = day['enrolled_percent']
			class_data[current_class][day_key] = [enrolled, waitlisted, enro_percent, wait_percent]

		i += 1
	else:
		user_classes[i] = input('Sorry, but ' + user_classes[i] + ' is not a valid course, please try again\n')

# print(class_data)

user_day1, user_day2 = int(user_day1), int(user_day2)
keys, values = class_data.keys(), []
for i in class_data:
	values.append(class_data.get(i))
print(class_data.keys())

phase1, phase2 = [], []
for i in values:
	phase1.append(i.get(user_day1))
	phase2.append(i.get(user_day2))

course_lst = []
count = 0


# print(keys[count])

# for i in phase1:
# 	course_lst.append(Course())
# courseload_1 = CourseLoad()
# courseload_2 = CourseLoad()





