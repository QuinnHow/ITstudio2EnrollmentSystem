import csv

from Course import Course
from Program import Program
from Semester import Semester
from Student import Student

courses = []

courseFile = open('course.csv')
courseReader = csv.reader(courseFile, delimiter=' ')
for row in courseReader:
    print(row)
    course = Course(row[0], row[1], row[2], row[3], row[4])
    
    courses.append(course)
    print(course)

 

programFile = open('program.csv')
programReader = csv.reader(programFile, delimiter=' ')

semesterFile = open('semester.csv')
semesterReader = csv.reader(semesterFile, delimiter=' ')

studentFile = open('student.csv')
studentReader = csv.reader(studentFile, delimiter=' ')

finish = True
while finish:
    inp = input('What would you like to do?\n')
    # a way to exit the program
    if inp.lower() == 'quit': break
    #put the different calls here e.g navigating through the menu... 
## save all files or save files when finished editing them?
print ('exiting program') 