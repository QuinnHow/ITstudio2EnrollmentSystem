import csv

from Course import Course
from Program import Program
from Semester import Semester
from Student import Student

courses = []
programs = []
semesters = []
students = []



courseFile = open('course.csv')
courseReader = csv.reader(courseFile, delimiter=' ')
for row in courseReader:
    print(row)
    course = Course(row[0], row[1], row[2], row[3], row[4])
    
    courses.append(course)
    print(course)

 

programFile = open('program.csv')
programReader = csv.reader(programFile, delimiter=' ')
for row in programReader:
    print(row)
    program = Program(row[0], row[1], row[2], row[3])
    
    programs.append(program)
    print(program)



semesterFile = open('semester.csv')
semesterReader = csv.reader(semesterFile, delimiter=' ')
for row in semesterReader:
    print(row)
    semester = Semester(row[0], row[1], row[2])
    
    semesters.append(semester)
    print(semester)


studentFile = open('student.csv')
studentReader = csv.reader(studentFile, delimiter=' ')
for row in studentReader:
    print(row)
    student = Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6] )
    
    students.append(student)
    print(student)



finish = True
while finish:
    inp = input('What would you like to do?\n')
    # a way to exit the program
    if inp.lower() == 'quit': break
    #put the different calls here e.g navigating through the menu...
    #if inp.lower() == 'student':
        #studentMenu(courses,programs,semesters,students)
## save all files or save files when finished editing them?
print ('exiting program') 