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
    
    course = Course(row[0], row[1], row[2], row[3], row[4])
    
    courses.append(course)
    





programFile = open('program.csv')
programReader = csv.reader(programFile, delimiter=' ')
for row in programReader:
    
    program = Program(row[0], row[1], row[2], row[3])
    
    programs.append(program)
    



semesterFile = open('semester.csv')
semesterReader = csv.reader(semesterFile, delimiter=' ')
for row in semesterReader:
    
    semester = Semester(row[0], row[1])
    
    semesters.append(semester)
    


studentFile = open('student.csv')
studentReader = csv.reader(studentFile, delimiter=' ')
for row in studentReader:
    
    student = Student(row[0],row[1],row[2],row[3],row[4].split(),row[5].split(),row[6].split())
    
    students.append(student)



        
            
         
        

    
    














passwordFile = open('passwords.csv')
passwordReader = csv.reader(passwordFile, delimiter=' ')
for row in passwordReader:
    
    password = Password(row[0], row[1], row[2])
    
    passwords.append(password)
    

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




def helpmain():
    print('If you would like to\nAccess the student menu - enter student\nAccess the admin menu - enter admin\nExit the program - enter quit')

print('Welcome')
helpmain()

finish = True
while finish:
    inp = input('What would you like to do?\n')
    # a way to exit the program
    if inp.lower() == 'quit': break
    #put the different calls here e.g navigating through the menu...
    elif inp.lower() == 'student':
        studentMenu(courses,programs,semesters,students,passwords)
    elif inp.lower() == 'admin':
        adminmenu(courses,programs,semesters,students,passwords)
    elif inp.lower() == 'help': helpmain()

    else: print('Imput error try again\nTry entering help to see the comands')
## save all files or save files when finished editing them?
print ('exiting program') 