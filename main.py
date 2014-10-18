print("Welcome to Tele-Bears Advisor!")
print("Tele-Bears Advisors looks at last semester's enrollment data and determines")
print("which classes you should Phase 1 and which ones you should Phase 2")
user_classes = input("Please enter all the classes you plan to take this semester, seperated by a spaces.\n")

user_classes = list(user_classes.upper().split())

berkeley_classes = ['CS61A', 'CS61B', 'CS61C']

i = 0
while i < len(user_classes):
	if user_classes[i].upper() in berkeley_classes:
		i += 1
	else:
		user_classes[i] = input('Sorry, but ' + user_classes[i] + ' is not a valid course, please try again\n')

# for option in berkeley_classes:

