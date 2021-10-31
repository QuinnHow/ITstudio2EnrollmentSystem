import csv
import Student

def adminmenu(courses,programs,semesters,students,passwords):

##import Program
##import Course
##import Semester
## login Peter
    
## Add/Remove/Amendastudent(Youwillalsoneedtoconsidertheeffectonotherclassinstancese.g., program, semester offerings.)James
    def addStudent(student):
        with open('student.csv', 'w') as writeFile:
            writeFile.write(student)
            

    def removeStudent(student):
        ## remove student from row, remove student from program, drop student in course offering,
        ## remove student from student.csv
        lines = []
        with open('student.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == student:
                        lines.remove(row)

        with open('student.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines) 
    

    def amendStudent(student, newStudent):
        lines = []
        with open('student.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == student:
                        lines.remove(row)

        with open('student.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines) 
            writeFile.write(newStudent)

## Add/Remove/Amendacourse(Youwillalsoneedtoconsidertheeffectonotherclassinstancese.g.,semester offerings.)James
    def addCourse(course):
        with open('course.csv', 'w') as writeFile:
            writeFile.write(course)

    def removeCourse(course):
        ## remove course from course.csv
        lines = []
        with open('course.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == course:
                        lines.remove(row)

        with open('course.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    def amendCourse(course, newCourse):
        lines = []
        with open('course.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == course:
                        lines.remove(row)

        with open('course.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines) 
            writeFile.write(newCourse)

## Add/Remove/Amendaprogram(Youwillalsoneedtoconsidertheeffectonotherclassinstancese.g., students.)James
    def addProgram(program):
        with open('program.csv', 'w') as writeFile:
            writeFile.write(program)

    def removeProgram(program):
        ## remove program from program.csv
        lines = []
        with open('program.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == program:
                        lines.remove(row)

        with open('program.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    def amendProgram(program, newProgram):
        lines = []
        with open('program.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == program:
                        lines.remove(row)

        with open('program.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
            writeFile.write(newProgram)

## Add/Remove/Amendasemester(Youwillalsoneedtoconsidertheeffectonotherclassinstancese.g., students)James
    def addSemester(semester):
        with open('semester.csv', 'w') as writeFile:
            writeFile.write(semester)

    def removeSemester(semester):
        ## remove program from semester.csv
        lines = []
        with open('semester.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == semester:
                        lines.remove(row)

        with open('semester.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
            
    def amendSemester(semester, newSemester):
        lines = []
        with open('semester.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == semester:
                        lines.remove(row)

        with open('semester.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
            writeFile.write(newSemester)

## Query student information including academic history and current enrolment Quinn
    def stuQuery(students,search):
            stu = None
            search = search.lower()
            for i in students:
                if search == i.studentID:
                    stu = i
            if stu == None:
                print('No matching student')
                exit()
            i = 0
            print('Student Name:',stu.name)
            print('Student ID:',stu.studentID)
            print('Student Academic History:')        
            while i < len(stu.accedemicHist):
                
                x = eval(stu.accedemicHist[i])
                            
                print('In {0} a grade of {1} was acheived'.format(x[0], x[1]))
                i+=1
            print('Student current enrollment:')
            i = 0
            while i < len(stu.curEnoll):
                
                x = eval(stu.curEnoll[i])
                            
                print('The course {0} is being taken in {1}'.format(x[0], x[1]))
                i+=1














# Allow manual amendment of the study plan for a student Sai
    def addStudyPlan(studentID):
        for i in students:
            if i.studentID == studentID:
                courseCode = input('Enter course code: ')
                semester = input('Enter Semester: ')
                year = input('Enter year: ')
                lines = []
                # with open('semester.csv', 'r') as readFile:
                #     reader = csv.reader(readFile)
                # for row in reader:
                #     lines.append(row)
                # for field in row:
                #     if field == studentID:
                #         lines.remove(row)
                # i.studyPlan.append(courseCode,semester,year)
                with open('semester.csv', 'w') as writeFile:
                    writeFile.write(courseCode,semester,year)
                return print(i.studyPlan)
           
    ## still looking into this
    


## Validate a students study plan Sai



## generate a student plan for a student of minimum length Sai
    def studyPlan(studentID):

        for i in students:
            if i.studentID == studentID:
            
                return print(i.studyPlan)
    

## for a particular course offering display a sorted list of students Sai

## in the assignment document it says the input should be course id and semester, 
## we need to add a input column to academic history under the student csv.
## also need to fix the academic spelling

    def achivementList(courseID,sem):
        for i in students:
            if i.accedemicHist == courseID and i.accemicHist == sem:
                return print(i.accedemicHist)


## Exit Peter
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
            
 ######################33 need to change to admin passwords when pasword section is added
    def login(passwords):
        print('Please sign in')
        username = input('Enter your username\n')
        pword = input('Enter your password\n')
        for i in passwords:
            if i.admin == '1' and i.username == username:
                ### we need a pasword for each student!!!!!!!!!!!
                if pword == i.password:
                    return True
        return False
    ## 3 seperate things for add remove ammend ... 
    def helpadmin():
        # print('If you would like to\n\n 1. Add student\n 2. RemoveAdd/Remove/Amendacourse - enter 2 \nAdd/Remove/Amendaprogram - enter 3 \nAdd/Remove/Amendasemester - enter 4 \nQuery student information including academic history and current enrolment - enter 5 \nAllow manual amendment of the study plan for a student - enter 6\nValidate a students study plan - enter 7 \nGenerate a student plan for a student of minimum length - enter 8 \nFor a particular course offering display a sorted list of students - enter 9 \nReturn to the main menu - enter exit')
        print(' 1.Add student \n 2.Remove student\n 3.Amend student\n 4.Add course\n 5.Remove course\n 6.Amend course\n 7.Add program\n 8.Remove Program\n 9.Amend Program\n 10.Add Semester\n 11.Remove Semester\n 12.Amend Semester\n 13.Query student information/Academic history\n 14.Genrate Study plan for a student\n 15.Amend study plan for a student\n 16.Validate a study pln for a student\n 17.Display a sorted list of students achievements in a course\n Enter search to search for a course\n Enter quit to exit\n\n Enter the number: ')

    success = login(passwords)
    if success:
        finish = True
        print('\nwelcome to the admin menu\n')
        helpadmin()  
    else:
        ## change back to false when passwords are implimented as this True is just so we can test the other functions
        finish = False
        ## remove the print and help call when passwords have been implemented as they are there for testingstud
        
        
        #################
        print('incorrect details')
    
    while finish:
        inp = input()
        ## returning to the base menu 
        if inp.lower() == 'help':
            helpadmin
        elif inp.lower() == 'quit':
            break
        elif inp == '1':
            addStudent()
        elif inp == '2':
            removeStudent()
        elif inp == '3':
            amendStudent()
        elif inp == '4':
            addCourse()
        elif inp == '5':
            removeCourse()
        elif inp == '6':
            amendCourse()
        elif inp == '7':
            addProgram
        elif inp == '8':
            removeProgram()
        elif inp == '9':
            amendProgram()
        elif inp == '10':
            addSemester()
        elif inp == '11':
            removeSemester()
        elif inp == '12':
            amendSemester()
        elif inp == '13':
            pass
        elif inp == '14':
            studentID = input('Enter studentID: ')
            studyPlan(studentID)
        elif inp == '15':
            studentID = input('Enter studentID: ')
            addStudyPlan(studentID)
        elif inp == '16':
            pass
        elif inp == '17':
            courseID = input('Enter courseID: ')
            sem = input('enter semester: ')
            achivementList(courseID,sem)
        elif inp.lower() == 'search': printclassessearch(courses,input('To use the search function you need two imputs title and code if you dont want to search by title or code just press enter for the prompts\nIf you would like to display all courses press enter twice\nenter the title you would like to search for or else press enter to not search with title\n'),input('Enter the course code you would like to search for or else press enter to not search with code\n'))
        else: print('Imput error try again\nTry entering help to see the comands')
    print ('returning to main meu') 