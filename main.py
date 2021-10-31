#start 8/10/21
#last updated: 31/10/21
#Members: James Hijazin:s3895829 , Peter Fulton:s3896790, Quinn How:s3899122, Saicharan Kannan:s3814854. 
#The program is intended to allow students to enrol and observe their  programs and courses as well as allow administative staff to alter courses and student information.
import csv
from AdminMenu import adminmenu

from Course import Course
from Program import Program
from Semester import Semester
from Student import Student
from password import Password
from StudentMenu import studentMenu
#creating the lists to store the data retrieved from the csv
courses = []
programs = []
semesters = []
students = []
passwords =[]


courseFile = open('course.csv')
courseReader = csv.reader(courseFile, delimiter=' ')
# for each row in the csv it is creating a course class from the data within that row and storing the cours created into the list courses
for row in courseReader:
    # print(row)
    course = Course(row[0], row[1], row[2], row[3], row[4])
    
    courses.append(course)
    # print(course)

# the process above is completed for all the classes course, program, semester, studemt, and passwords 



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
    student = Student(row[0],row[1],row[2],row[3],row[4].split(),row[5].split(),row[6].split())
    
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
        for i in courses:
            if i.title == title and i.code == code:
                print(i)

    else: print('something went wrong with your search ')
# a help function to display the actions a user can take
def helpmain():
    print('If you would like to\n1.Access the menu\n2.Access the admin menu\nquit.Exit the program')

print('Welcome')
helpmain()# shows an initial list of actions that can be taken

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

    elif inp.lower() == 'search': printclassessearch(courses,input('To use the search function you need two imputs title and code if you dont want to search by title or code just press enter for the prompts\nIf you would like to display all courses press enter twice\nenter the title you would like to search for or else press enter to not search with title\n'),input('Enter the course code you would like to search for or else press enter to not search with code\n'))

    else: print('Imput error try again\nTry entering help to see the comands')
# ends the program nolonger loops printing this message and then finishes running
print ('exiting program') 
