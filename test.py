from bs4 import BeautifulSoup
import urllib.request

page = urllib.request.urlopen("http://www.berkeleytime.com/enrollment/").read()
soup = BeautifulSoup(page)

options = soup.find_all('option',value=True)

classes = {}
text_file = open('list_classes.py', 'w')

for option in options:
	if option['value']:
		text_file.write('"' + option['data-title'] + '" : ' + str(option['value']) + ', ')
		classes[option['data-title']] = option['value']


# for option in options:

# 	# Build request
# 	sections = urllib.request.urlopen("http://www.berkeleytime.com/enrollment/sections/" + option['value'] + "/").read()
# 	data = eval(BeautifulSoup(sections).text)
# 	if data:
# 		year, semester = data[-1]['year'], data[-1]['semester']

# 		final_data = urllib.request.urlopen("http://www.berkeleytime.com/enrollment/aggregate/" + option['value'] + "/" + semester + "/" + year + "/").read()
# 		data = eval(BeautifulSoup(final_data).text)

# 	if data:
# 		title = data["title"]
# 		subtitle = data["subtitle"]
# 		max_enrollment = data['enrolled_max']
# 		data = data['data']
# 		text_file.write('\t \'')
# 		text_file.write(title)
# 		text_file.write('\' : ')
# 		text_file.write('[')
# 		text_file.write("'"+subtitle+"'")
# 		text_file.write(',')
# 		text_file.write(str(max_enrollment))
# 		text_file.write(',')
# 		text_file.write(str(data))
# 		text_file.write(']\n')

text_file.close()