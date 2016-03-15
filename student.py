
class Student:
 	__num_students = 0
 	def __init__(self, name, gpa):
 		self.name = name
 		self.gpa = gpa
 		Student.__num_students += 1
 	def __str__(self):
		return self.name + ": " + str(self.gpa)


joey = Student('Joey Coder', 4.0)
# joey = Student()

print joey
print Student.__num_students
