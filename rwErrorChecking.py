import cPickle as pic

# Function to load list from file
def load (fileName):	
	try:
		file = open(fileName)	
		languages = pic.load(file)
		file.close()
		print "Loaded Data"
		print languages
	except IOError, e:
		if e.errno == 2:
			print "The file you want to read to does not exist"
		if e.errno == 13:
			print "You do not have read access to that directory"		
	except NameError:
		print "File not created successfully"	

	# Test for success, add parameter to allow open to create file if missing
	finally:
		file = open(fileName, "r")
		languages = pic.load(file)
		file.close()
		print "Loaded Data"
		print languages

# Function to save list
def save (fileName, data):
	try:
		file = open(fileName)		
		pic.dump(data, file)
		file.close()
		print "Save complete"
	except IOError, e:
		if e.errno == 2:
			print "The file you want to write to does not exist"
		if e.errno == 13:
			print "You do not have write access to that directory"		
	except NameError:
		print "File not created successfully"

	# Test for success, add parameter to allow open to create file if missing
	finally:
		file = open(fileName, "w")
		pic.dump(data, file)
		file.close()
		print "Save complete"

# List of test file names and directories
tests = ["test.txt", "null.txt", "/home/roeje/Documents/343/pythonProjects/test2.txt", "/home/woodriir/test2.txt"]
data = ['Java', 'C++', 'Python']

# Loop through test directories
for test in tests:	
	save(test, data)	
	load(test)