from data_new import berkeley_classes
from bs4 import BeautifulSoup
import urllib.request

print("Welcome to Tele-Bears Advisor!")
print("Tele-Bears Advisors looks at last semester's enrollment data and determines")
print("which classes you should Phase 1 and which ones you should Phase 2")
user_classes = input("Please enter all the classes you plan to take this semester, seperated by a spaces.\n")

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