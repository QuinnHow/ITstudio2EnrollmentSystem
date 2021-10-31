#start 8/10/21
#last updated: 31/10/21
#Members: James Hijazin:s3895829 , Peter Fulton:s3896790, Quinn How:s3899122, Saicharan Kannan:s3814854. 
#The program is intended to allow students to enrol and observe their  programs and courses as well as allow administative staff to alter courses and student information.
import csv
import Student

def adminmenu(courses,programs,semesters,students,passwords):

##import Program
##import Course
##import Semester
## login Peter
    
## Add/Remove/Amendastudent(Youwillalsoneedtoconsidertheeffectonotherclassinstancese.g., program, semester offerings.)James
    def addStudent(studentID):
        sID = studentID ## assign studentID to sID
        name = input('Enter name: ') ## ask for name
        dob = input('Enter date of birth: ') ## ask for dob
        programCode = input('Enter program code: ' ) ## ask for program code
        academicHist = input('Enter academic history: ') ## ask for academic history
        studyPlan = input('Enter study plan: ') ## ask for study plan
        curEnoll = input('Enter current enrollment: ') ## ask for current enrollment
        student = name + ' ' + sID + ' ' + dob + ' ' + programCode + ' ' + academicHist + ' ' + studyPlan + ' ' + curEnoll ## create student string
        with open('student.csv', 'a') as writeFile: ## open file for writing
            writeFile.write("\n") ## create new line for new row
            writeFile.write(student) ## write student to csv file

    def removeStudent(studentID):
        lines = []
        with open('student.csv', 'r') as readFile: ## open file for reading
            reader = csv.reader(readFile, delimiter=' ') ## read file
            for row in reader:
                if row[1] != studentID: ## if row doesn't contain studentID we don't want
                    lines.append(row) ## add to list

        with open('student.csv', 'w') as writeFile: ## open file for writing
            writer = csv.writer(writeFile)
            writer.writerows(lines) ## write data from list back to csv
    

    def amendStudent(studentID, newStudentID):
        lines = []
        with open('student.csv', 'r') as readFile: ## open file for reading
            reader = csv.reader(readFile, delimiter=' ') ## read file
            for row in reader:
                if row[1] != studentID: ## if row doesn't contain studentID we don't want
                    lines.append(row) ## add to list
        sID = newStudentID ## assign studentID to sID
        name = input('Enter name: ') ## ask for name
        dob = input('Enter date of birth: ') ## ask for dob
        programCode = input('Enter program code: ' ) ## ask for program code
        academicHist = input('Enter academic history: ') ## ask for academic history
        studyPlan = input('Enter study plan: ') ## ask for study plan
        curEnoll = input('Enter current enrollment: ') ## ask for current enrollment
        newStudent = name + ' ' + sID + ' ' + dob + ' ' + programCode + ' ' + academicHist + ' ' + studyPlan + ' ' + curEnoll ## create new student string
        with open('student.csv', 'w') as writeFile: ## open file for writing
            writer = csv.writer(writeFile)
            writer.writerows(lines) ## write data from list back to csv
            writeFile.write(newStudent) ## write new student to csv

## Add/Remove/Amendacourse(Youwillalsoneedtoconsidertheeffectonotherclassinstancese.g.,semester offerings.)James
    def addCourse(courseCode):
        cCode = courseCode ## assign courseCode to cCode
        title = input('Enter title: ') ## ask for title
        credit = input('Enter credit score: ') ## ask for credit score
        preReq = input('Enter prerequisites: ' ) ## ask for prerequisites
        avalSem = input('Enter available semester: ') ## ask for semester
        course = cCode + ' ' + title + ' ' + credit + ' ' + preReq + ' ' + avalSem ## create course string
        with open('course.csv', 'a') as writeFile: ## open file for writing
            writeFile.write("\n") ## create new line for new row
            writeFile.write(course) ## write course to csv file

    def removeCourse(courseCode):
        lines = []
        with open('course.csv', 'r') as readFile: ## open file for reading
            reader = csv.reader(readFile, delimiter=' ') ## read file
            for row in reader:
                if row[0] != courseCode: ## if row doesn't contain courseCode we don't want
                    lines.append(row) ## add to list

        with open('course.csv', 'w') as writeFile: ## open file for writing
            writer = csv.writer(writeFile)
            writer.writerows(lines) ## write data from list back to csv

    def amendCourse(courseCode, newCourseCode):
        lines = []
        with open('course.csv', 'r') as readFile: ## open file for reading
            reader = csv.reader(readFile, delimiter=' ') ## read file
            for row in reader:
                if row[0] != courseCode: ## if row doesn't contain courseCode we don't want
                    lines.append(row) ## add to list
        cCode = newCourseCode ## assign newCourseCode to cCode
        title = input('Enter title: ') ## ask for title
        credit = input('Enter credit score: ') ## ask for credit score
        preReq = input('Enter prerequisites: ' ) ## ask for prerequisites
        avalSem = input('Enter available semester: ') ## ask for semester
        newCourse = cCode + ' ' + title + ' ' + credit + ' ' + preReq + ' ' + avalSem ## create newCourse string
        with open('course.csv', 'w') as writeFile: ## open file for writing
            writer = csv.writer(writeFile)
            writer.writerows(lines) ## write data from list back to csv
            writeFile.write(newCourse) ## write new course to csv

## Add/Remove/Amendaprogram(Youwillalsoneedtoconsidertheeffectonotherclassinstancese.g., students.)James
    def addProgram(programCode):
        pCode = programCode ## assign programCode to pCode
        credit = input('Enter credit score: ') ## ask for credit score
        core = input('Enter core subjects: ' ) ## ask for core subjects
        elective = input('Enter electives: ') ## ask for electives
        program = pCode + ' ' + credit + ' ' + core + ' ' + elective ## create program string
        with open('program.csv', 'a') as writeFile: ## open file for writing
            writeFile.write("\n")
            writeFile.write(program) ## write program to csv file

    def removeProgram(programCode):
        lines = []
        with open('program.csv', 'r') as readFile: ## open file for reading
            reader = csv.reader(readFile, delimiter=' ') ## read file
            for row in reader:
                if row[0] != programCode: ## if row doesn't contain programCode we don't want
                    lines.append(row) ## add to list

        with open('program.csv', 'w') as writeFile: ## open file for writing
            writer = csv.writer(writeFile)
            writer.writerows(lines) ## write data from list back to csv

    def amendProgram(programCode, newProgramCode):
        lines = []
        with open('program.csv', 'r') as readFile: ## open file for reading
            reader = csv.reader(readFile) ## read file
            reader = csv.reader(readFile, delimiter=' ') ## read file
            for row in reader:
                if row[0] != programCode: ## if row doesn't contain programCode we don't want
                    lines.append(row) ## add to list
        pCode = newProgramCode ## assign newProgramCode to pCode
        credit = input('Enter credit score: ') ## ask for credit score
        core = input('Enter core subjects: ' ) ## ask for core subjects
        elective = input('Enter electives: ') ## ask for electives
        newProgram = pCode + ' ' + credit + ' ' + core + ' ' + elective ## create newProgram string
        with open('program.csv', 'w') as writeFile: ## open file for writing
            writer = csv.writer(writeFile)
            writer.writerows(lines) ## write data from list back to csv
            writeFile.write(newProgram) ## write new program to csv

## Add/Remove/Amendasemester(Youwillalsoneedtoconsidertheeffectonotherclassinstancese.g., students)James
    def addSemester(semesterID):
        semID = semesterID ## assign semesterID to semID
        cOfferings = input('Enter course offerings: ') ## ask for course offering
        semester = semID + ',' + cOfferings ## create semester string
        with open('semester.csv', 'a') as writeFile: ## open file for writing
            writeFile.write("\n")
            writeFile.write(semester) ## write semester to csv file

    def removeSemester(semesterOffer):
        lines = []
        with open('semester.csv', 'r') as readFile: ## open file for reading
            reader = csv.reader(readFile, delimiter = ' ') ## read file
            for row in reader:
                if row[1] != semesterOffer: ## if row doesn't contain semesterOffer we don't want
                    lines.append(row) ## add to list

        with open('semester.csv', 'w') as writeFile: ## open file for writing
            writer = csv.writer(writeFile)
            writer.writerows(lines) ## write data from list back to csv
            
    def amendSemester(semesterOffer, newSemesterOffer):
        lines = []
        with open('semester.csv', 'r') as readFile: ## open file for reading
            reader = csv.reader(readFile, delimiter = ' ') ## read file
            for row in reader:
                if row[1] != semesterOffer: ## if row doesn't contain semesterOffer we don't want
                    lines.append(row) ## add to list
        cOfferings = newSemesterOffer ## assign semesterID to semID
        semID = input('Enter semester ID: ') ## ask for course offering
        newSemester = semID + ',' + cOfferings ## create semester string
        with open('semester.csv', 'w') as writeFile: ## open file for writing
            writer = csv.writer(writeFile)
            writer.writerows(lines) ## write data from list back to csv
            writeFile.write(newSemester) ## write new semester to csv

## Query student information including academic history and current enrolment Quinn
    def stuQuery(students,search):
            stu = None
            #checks that the search code is a student ID
            search = search.lower()
            for i in students:
                if search == i.studentID:
                    stu = i
            if stu == None:
                print('No matching student')
                exit()
            i = 0
            #prints the students info if it is a real student
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
    def addStudyPlan(studentID): #function for adding studyplan
        for i in students: #checks each student in students list (for loop)
            if i.studentID == studentID: #checks weather the studentlist conatins the studentID the user is looking for
                student = i # Assign the match student to the student variable
                courseCode = input('Enter course code: ') # Stores user input into the CourseCode variable
                semester = input('Enter Semester and the year eg: s1,2021: ')# stores userinput into Semester Variable
                lines = []
                for i in courses: # checks each course in courses list (for loop)
                    if i.code == courseCode and i.avalSem == semester: #Validating whether the coursecode and semester are inputed as their offering semster
                        student.studyPlan.append("(\'{0}\',\'{1}\')".format(courseCode,semester))  #Appends the CourseCode and semster to the existing list of StudyPlan
                    else : print('Error check the course code and available semester') ## Error statement
                return print('The change has been added to the student study plan. {}'.format(student.studyPlan))

## generate a student plan for a student of minimum length Sai
    def studyPlan(studentID): # fucntion to genrate a studyplan

        for i in students: # seachers for the student and prints it
            if i.studentID == studentID:
                student = i 
                return print('The student study plan is below:\n {}'.format(student.studyPlan))
    

## for a particular course offering display a sorted list of students Sai

## in the assignment document it says the input should be course id and semester, 
## we need to add a input column to academic history under the student csv.
## also need to fix the academic spelling

    def achivementList(courseID,sem): # function sorted list
        # fucction should search into the acedemic history of all the students who did the course, sorts them and prints them.
        temp = []
        for s in students:
            for i in s.accedemicHist:
                if courseID in i:
                    temp.append(i)
            # cond = [item for item in s.accedemicHist if courseID in item]
        temp.sort()
        print(temp) # could imporve this function but does not work how its supposed to work. -sai
            


            # for i in range(len(s.accedemicHist)):
    def checkGrad(studentID):
        temp = []
        code = []
        cond = []
        final = []
        credit = 12
        for c in courses:
            code.append(c.code)
        

        
        for s in students:
            if s.studentID == studentID:
                for i in s.accedemicHist:
                
                    # if code in i and not 'NN' in i:
                        i = eval(i)
                        temp.append(i)

            # temp.append(item for item in s.accedemicHist if ini in item)
        for t in temp:
            for z in code:
                if t[0] == z:
                     cond.append(t)
        for f in cond:
            if 'NN' not in cond:
                final.append(f)
        grad = 230- (len(final) * credit)
        if grad == 0:
            return print('Sudent can graduate')
        else :
            return print('Student still needs {} credits points to graduate'.format(grad))

        
            
                


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
            
 ###################### similarly to the studentmenu login however the i.admin == '1' is used to only search administrator passwords and usernames 
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
        print(' 1.Add student \n 2.Remove student\n 3.Amend student\n 4.Add course\n 5.Remove course\n 6.Amend course\n 7.Add program\n 8.Remove Program\n 9.Amend Program\n 10.Add Semester\n 11.Remove Semester\n 12.Amend Semester\n 13.Query student information/Academic history\n 14.Genrate Study plan for a student\n 15.Amend study plan for a student\n 16.Display a sorted list of students achievements in a course\n 17.Check Graduation status Enter search to search for a course\n Enter quit to exit\n\n Enter the number: ')

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
    
    while finish: # while loop which runs until user enters quit
        inp = input()
        if inp.lower() == 'help':
            helpadmin()
        elif inp.lower() == 'quit':
            break
        ## According the user input number it triggers a function corresponding to it
        elif inp == '1':
            studentID = input('Enter studentID: ')
            addStudent(studentID)
        elif inp == '2':
            studentID = input('Enter studentID: ')
            removeStudent(studentID)
        elif inp == '3':
            studentID = input('Enter studentID: ')
            newStudentID = studentID
            amendStudent(studentID, newStudentID)
        elif inp == '4':
            courseCode = input('Enter course code: ')
            addCourse(courseCode)
        elif inp == '5':
            courseCode = input('Enter course code: ')
            removeCourse(courseCode)
        elif inp == '6':
            courseCode = input('Enter course code: ')
            newCourseCode = courseCode
            amendCourse(courseCode, newCourseCode)
        elif inp == '7':
            programCode = input('Enter program code: ')
            addProgram(programCode)
        elif inp == '8':
            programCode = input('Enter program code: ')
            removeProgram(programCode)
        elif inp == '9':
            programCode = input('Enter program code: ')
            newProgramCode = programCode
            amendProgram(programCode, newProgramCode)
        elif inp == '10':
            semesterID = input('Enter semester ID: ')
            addSemester(semesterID)
        elif inp == '11':
            semesterOffer = input('Enter semester offer: ')
            removeSemester(semesterOffer)
        elif inp == '12':
            semesterOffer = input('Enter semester offer: ')
            newSemesterOffer = semesterOffer
            amendSemester(semesterOffer, newSemesterOffer)
        elif inp == '13':
            pass
        elif inp == '14':
            studentID = input('Enter studentID: ')
            studyPlan(studentID)
        elif inp == '15':
            studentID = input('Enter studentID: ')
            addStudyPlan(studentID)
        elif inp == '16':
            courseID = input('Enter courseID: ')
            sem = input('enter semester: ')
            achivementList(courseID,sem)
        elif inp == '17':
            studentID = input('Enter studentID: ')
            checkGrad(studentID)

        ## search for certain course
        elif inp.lower() == 'search': printclassessearch(courses,input('To use the search function you need two imputs title and code if you dont want to search by title or code just press enter for the prompts\nIf you would like to display all courses press enter twice\nenter the title you would like to search for or else press enter to not search with title\n'),input('Enter the course code you would like to search for or else press enter to not search with code\n'))
        else: print('Imput error try again\nTry entering help to see the comands')
    print ('returning to main meu') 