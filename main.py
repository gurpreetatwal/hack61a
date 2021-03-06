from data_new import berkeley_classes
from bs4 import BeautifulSoup
from classes import Course,CourseLoad
from datetime import datetime
import urllib.request

print("Welcome to Tele-Bears Advisor!")
print("Tele-Bears Advisors looks at last semester's enrollment data and determines")
print("which classes you should Phase 1 and which ones you should Phase 2")

user_day1 = input("Please enter your Phase1 Tele-Bears day, for example Nov 4 2014: ")
user_day2 = input("Please enter your Phase2 Tele-Bears day: ")
user_classes = input("Please enter all the classes you plan to take this semester, seperated by a spaces.\n")

tele_bears = datetime.strptime('Oct 20 2014', '%b %d %Y')
user_day1 = datetime.strptime(user_day1, '%b %d %Y') - tele_bears
user_day2 = datetime.strptime(user_day2, '%b %d %Y') - tele_bears

user_day1 = int(user_day1.days)
user_day2 = int(user_day2.days)

user_day1 = 19
user_day2 = 20

user_classes = user_classes.upper().split()
class_data = {}

i = 0
while i < len(user_classes):
	user_classes[i] = user_classes[i].upper()   
	current_class = user_classes[i]

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

		# Get units
		unit_page = urllib.request.urlopen("http://www.berkeleytime.com/catalog/course_box/?course_id=" + str(class_value))
		unit_page = BeautifulSoup(unit_page)
		units = unit_page.find('div', class_="generic-text-box", text='Units').previous_element

		# Manage data
		class_data[current_class] = {}
		max_enroll = data['enrolled_max']
		data = data['data']

		for day in data:
			day_key = day['day']
			enrolled = day['enrolled']
			waitlisted = day['waitlisted']
			wait_percent = day['waitlisted_percent']
			enro_percent = day['enrolled_percent']

			class_data[current_class][day_key] = [float(enrolled), float(waitlisted), float(enro_percent), float(wait_percent), int(units), float(max_enroll)]
		i += 1
	else:
		user_classes[i] = input('Sorry, but ' + user_classes[i] + ' is not a valid course, please try again\n')

keys, values = class_data.keys(), []
for i in class_data:
	values.append(class_data.get(i))

phase1, phase2 = [], []
for i in values:
	phase1.append(i.get(user_day1))
	phase2.append(i.get(user_day2))

course_lst1, course_lst2 = [], []
count = 0
for key in keys:
	p1, p2 = phase1[count], phase2[count]
	print(p1, p2)
	course_lst1.append(Course(key,user_day1, p1[0], p1[1], p1[3], p1[2], p1[4], p1[5]))
	course_lst2.append(Course(key,user_day2, p2[0], p2[1], p2[3], p2[2], p2[4], p2[5]))
	count += 1

cl1 = CourseLoad(course_lst1)
cl2 = CourseLoad(course_lst2)


def phase_or_not(courseyay):

	if courseyay.wait_percent + (courseyay.enrolled / courseyay.class_size) > .3:
		return False
	return True



phase_two_classes = CourseLoad([])
phase_one_courses = CourseLoad([])


for i in range(cl2.len()):
	if True == phase_or_not(cl2.get(i)):
		phase_two_classes.add_course(cl2.get(i))
	else:

		phase_one_courses.add_course(cl1.get(i))


phase_one_courses1 = CourseLoad([])
impossible_classes = CourseLoad([])


for i in range(phase_one_courses.len()):
	if True == phase_or_not(phase_one_courses.get(i)):
		phase_one_courses1.add_course(phase_one_courses.get(i))

	else:
		impossible_classes.add_course(phase_one_courses.get(i))

print('You can phase 2 these and probably get in: ', [i.name for i in phase_two_classes.lst])
print('You need to phase 1 these for sure; if you cant you probably wont get into them: ', [i.name for i in phase_one_courses1.lst])
print('Sorry, you cant get into these classes even with phase 1: ', [i.name for i in impossible_classes.lst])



