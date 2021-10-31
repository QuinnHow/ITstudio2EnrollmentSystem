import csv
from AdminMenu import adminmenu

from Course import Course
from Program import Program
from Semester import Semester
from Student import Student
from password import Password
from StudentMenu import studentMenu

courses = []
programs = []
semesters = []
students = []
passwords =[]


courseFile = open('course.csv')
courseReader = csv.reader(courseFile, delimiter=' ')
for row in courseReader:
    # print(row)
    course = Course(row[0], row[1], row[2], row[3], row[4])
    
    courses.append(course)
    # print(course)





programFile = open('program.csv')
programReader = csv.reader(programFile, delimiter=' ')
for row in programReader:
    # print('---------------------------------------',row)
    program = Program(row[0], row[1], row[2], row[3])
    
    programs.append(program)
    # print(program)



semesterFile = open('semester.csv')
semesterReader = csv.reader(semesterFile, delimiter=' ')
for row in semesterReader:
    # print(row)
    semester = Semester(row[0], row[1])
    
    semesters.append(semester)
    # print(semester)


studentFile = open('student.csv')
studentReader = csv.reader(studentFile, delimiter=' ')
for row in studentReader:
    # print(row)
    student = Student(row[0],row[1],row[2],row[3],row[4].split(),row[5],row[6])
    
    students.append(student)
    # print(student)


passwordFile = open('passwords.csv')
passwordReader = csv.reader(passwordFile, delimiter=' ')
for row in passwordReader:
    # print('---------------------------------------',row)
    password = Password(row[0], row[1], row[2])
    
    passwords.append(password)
    # print(password)

for i in courses:
    if i.getCourse('cosc2411') is True:
        print(i.code)


def stuSearch(ID):
    for i in students:
        if i.studentID == ID:
            return i
        else:
            return None
#Student.getStudent('s3653411')
def printclasses(courses):
    for i in courses: print(i)
def printclassessearch(courses, title = None, code= None):
    if (title == '' )and (code == ''):
        printclasses(courses)
    elif  title == '':
        for i in courses:
            if i.code == code : print(i)
    elif code == '': 
        for i in courses:
            if i.title == title : print(i)
    elif code != '' and title != '':
        for i in course:
            if i.title == title and i.code == code:
                print(i)

    else: print('something went wrong with your search ')
def helpmain():
    print('If you would like to\nAccess the student menu - enter 1\nAccess the admin menu - enter 2\nExit the program - enter quit')

print('Welcome')
helpmain()

finish = True
while finish:
    inp = input('What would you like to do?\n')
    # a way to exit the program
    if inp.lower() == 'quit': break
    #put the different calls here e.g navigating through the menu...
    elif inp.lower() == '1':
        studentMenu(courses,programs,semesters,students,passwords)
    elif inp.lower() == '2':
        adminmenu(courses,programs,semesters,students,passwords)
    elif inp.lower() == 'help': helpmain()
    elif inp.lower() == 'classes': printclasses(courses)
    elif inp.lower() == 'class search': printclassessearch(courses,input('enter the tiqtle you would like to search for or else press enter'),input('enter the course code you would like to search for or else press enter'))

    else: print('Imput error try again\nTry entering help to see the comands')
## save all files or save files when finished editing them?
print ('exiting program') 
