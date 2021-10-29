import csv

def adminmenu(courses,programs,semesters,students,passwords):
##import Student
##import Program
##import Course
##import Semester
## login Peter

    
## Add/Remove/Amendastudent(Youwillalsoneedtoconsidertheeffectonotherclassinstancese.g., program, semester offerings.)
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
    

    def amendStudent(student):
        pass

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

    def amendCourse(course):
        pass

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

    def amendProgram(program):
        pass

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

    def amendSemester(semester):
        pass

    def studyPlan(student):
        pass

## Query student information including academic history and current enrolment Quinn


## Allow manual amendment of the study plan for a student Sai


## Validate a students study plan Sai


## generate a student plan for a student of minimum length Sai


## for a particular course offering display a sorted list of students Sai

## Exit Peter
 ######################33 need to change to admin passwords when pasword section is added
    def login(passwords):
        print('Please sign in')
        username = input('Enter your student number\n')
        pword = input('Enter your password\n')
        for i in passwords:
            if i.admin == '1' and i.username == username:
                ### we need a pasword for each student!!!!!!!!!!!
                if pword == i.password:
                    return True
        return False
    ## 3 seperate things for add remove ammend ... 
    def helpadmin():
        print('If you would like to\n\nAdd/Remove/Amendastudent - enter arast (the student)\nAdd/Remove/Amendacourse - enter arac (the course)\nAdd/Remove/Amendaprogram - enter arap (the program)\nAdd/Remove/Amendasemester - enter arase (the semester)\nQuery student information including academic history and current enrolment - enter query (the student)\nAllow manual amendment of the study plan for a student - enter ama(the student)\nValidate a students study plan - validate (the student)\nGenerate a student plan for a student of minimum length - enter generate study (the student)\nFor a particular course offering display a sorted list of students - enter display students (specific course offering)\nReturn to the main menu - enter exit')

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
        if inp.lower() == 'help': helpadmin()
        if inp.lower() == 'exit': break
        ## these need to be changed to the function calls for the admin menu
        if inp.lower() == 'academic history':
            pass #acc hsit function 
        if inp.lower() == 'course or program information':
            pass #course or program information function
        if inp.lower() == 'enrol':
            pass #Enrol function
        if inp.lower() == 'un enrol':
            pass #Un enrol function
        if inp.lower() == 'un enrol':
            pass #Un enrol function
        else: print('Imput error try again\nTry entering help to see the comands')
    print ('returning to main meu') 