import cPickle as pic

def open (fileName):
	# file = open("fileName", "rb")
	file = open("fileName")
	languages = pic.load(file);
	print "File: " + languages


def save (fileName, data):
	# file = open("fileName", "wb")
	file = open("fileName")
	pic.dump(data, file)
	print "save complete"


data = ['Java', 'C++', 'Python']
print data

save("test.txt", data)
open("test.txt")