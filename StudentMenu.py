#import main
def studentMenu (courses,programs,semesters,students,passwords):
    
   
    

    
    import Student
    #import Program
    #import Course
    #import Semester

    ## login Peter
    # usees the passwords list to see if the entered username and password are valid befroe proceeding to the menu or else yu are returned to the main menu
    def login(passwords):
        print('Please sign in')
        username = input('Enter your student number\n')
        pword = input('Enter your password\n')
        for i in passwords:
            if i.admin == '0' and i.username == username: # the 0 in i.admin is to only search the student logins and not the admin ones 
                if pword == i.password:
                    global userID
                    userID = username
                    return True
        return False
    
    ## Display academic history and current enrolment Quinn
    def displayAc(stu):
        #takes data from the student, the student will always be user
        i = 0
        print('Student Name:',stu.name)
        print('Student ID:',stu.studentID)
        print('Student Academic History:')        
        while i < len(stu.accedemicHist):
        #for all classes taken the grades are written out 
            x = eval(stu.accedemicHist[i])
                        
            print('In {0} a grade of {1} was acheived'.format(x[0], x[1]))
            i+=1
        print('Student current enrollment:')
        i = 0
        while i < len(stu.curEnoll):
        #writes all current enrolled classes      
                x = eval(stu.curEnoll[i])
                            
                print('The course {0} is being taken in {1}'.format(x[0], x[1]))
                i+=1
            
        
    
    ## Querying course or program information Quinn 
    def courseQuery(search):
        search = search.lower()
        for i in programs:
            #searches if the query is for a program
            if search == i.code:
                statement = 'The program {0} is {1} credit points in total it\'s core subjects are {2} and it\'s electives are {3}'.format(i.code, i.creditPoints, i.core, i.elective)
                break
            else:
                statement = 'No matching program found'    

        print(statement)


        for i in courses:
            #searches if the query is for a course, vhecks title and code in the search
            if search == i.title or search == i.code:
                statement = 'The course {0}, with code {4} will be held in {1} it is {2} course credits and it\'s prerequisites are {3}'.format(i.title, i.avalSem, i.credit, i.preReq, i.code)
                break
            else:
                statement = 'No matching course found'
            
        print(statement)









    ## Enrol/UnEnrol in a current offering (You will need to consider the pre-req and the impact of an enrollment.) Quinn 
    def enrol(stu, code, semester, req):
        req = req.lower()
        #sets the requirements
        meetsReq = True
        if req != 'none':
            #checks the given requirements against academic history
            meetsReq = False
            for i in stu.accedemicHist:
                i = eval(i)
                if i[0] == req:
                    meetsReq = True
                    break
        if meetsReq == True:
            #apends an enrolment
            stu.curEnoll.append("(\'{0}\',\'{1}\')".format(code,semester))
            print('Completed')
        else:
            print('Pre-requisites not met or impropery entered')


    def unEnrol(stu,code):
        #checks the student is taking the course
        x = 0
        removal = False
        for i in stu.curEnoll:
            
            i = eval(i)
            #removes the course if the given code equals one of the currently enrolled course codes
            if i[0] == code:
              stu.curEnoll.pop(x)
              removal = True
            
            x += 1    
        if removal == True:
            print('Removal succesful')
        else:
            print('No removal as no such course currently enrolled')

#this adds a sum of the scores acheived in each class by each student and finds the largest one which is the easiest class
    def easy():

        classList = []
        #goes through every subject in courses and checks them against the academic history of every student adding the scores up and incrementing the student number
        #if the student has taken that course
        for i in courses:
            overallGrade = 0
            numStu = 0
            for j in students:
                for y in j.accedemicHist:
                    y = eval(y)
                    if y[0] == i.code:
                        numStu += 1
                        if y[1] == 'HD':
                            overallGrade += 4
                        if y[1] == 'DI':
                            overallGrade += 3
                        if y[1] == 'CR':
                            overallGrade += 2
                        if y[1] == 'PA':
                            overallGrade += 1
                        if y[1] == 'NN':
                            overallGrade += 0
            classList.append('(\'{0}\',{1},{2})'.format(i.title,overallGrade,numStu))
        #finds the easiest class of the taken classes and makes it a separate tuple    
        easiest = classList[0]
        for i in classList:
            ease = eval(easiest)
            i = eval(i)
            if ease[1]/ease[2] < int(i[1])/int(i[2]):
                easiest = i
        #finds the average mark and then asigns that an average letter grade
        easiest = eval(easiest)
        avMark = int(easiest[1])/int(easiest[2])
        if avMark >= 4:
<<<<<<< HEAD
            string = 'The hardest class is {0} with an average grade of HD'.format(hardest[0])
        elif avMark >= 3:
            string = 'The hardest class is {0} with an average grade of DI'.format(hardest[0])
        elif avMark >= 2:
            string = 'The hardest class is {0} with an average grade of CR'.format(hardest[0])
        elif avMark >= 1:
            string = 'The hardest class is {0} with an average grade of PA'.format(hardest[0])
        else:
            string = 'The hardest class is {0} with an average grade of NN'.format(hardest[0])
=======
            string = 'The hardest class is {0} with an average grade of HD'.format(easiest[0])
        elif avMark >= 3:
            string = 'The hardest class is {0} with an average grade of DI'.format(easiest[0])
        elif avMark >= 2:
            string = 'The hardest class is {0} with an average grade of CR'.format(easiest[0])
        elif avMark >= 1:
            string = 'The hardest class is {0} with an average grade of PA'.format(easiest[0])
        else:
            string = 'The hardest class is {0} with an average grade of NN'.format(easiest[0])
>>>>>>> 9320e4e82c42909ed93dd3d9cfa01ebb75f85c97
        print(string)
    
    
    #this adds a sum of the scores acheived in each class by each student and finds the smallest one which is the hardest class
    def hard():
        classList = []
        #goes through every subject in courses and checks them against the academic history of every student adding the scores up and incrementing the student number
        #if the student has taken that course
        for i in courses:
            overallGrade = 0
            numStu = 0
            for j in students:
                for y in j.accedemicHist:
                    y = eval(y)
                    if y[0] == i.code:
                        numStu += 1
                        if y[1] == 'HD':
                            overallGrade += 4
                        if y[1] == 'DI':
                            overallGrade += 3
                        if y[1] == 'CR':
                            overallGrade += 2
                        if y[1] == 'PA':
                            overallGrade += 1
                        if y[1] == 'NN':
                            overallGrade += 0
            classList.append('(\'{0}\',{1},{2})'.format(i.title,overallGrade,numStu))
        #finds the hardest class of the taken classes and makes it a separate tuple    
        hardest = classList[0]
        for i in classList:
            har = eval(hardest)
            i = eval(i)
            if har[1]/har[2] > int(i[1])/int(i[2]):
                hardest = i
        
        #finds the average mark and then asigns that an average letter grade
        avMark = int(hardest[1])/int(hardest[2])
        if avMark >= 4:
            string = 'The hardest class is {0} with an average grade of HD'.format(hardest[0])
        elif avMark >= 3:
            string = 'The hardest class is {0} with an average grade of DI'.format(hardest[0])
        elif avMark >= 2:
            string = 'The hardest class is {0} with an average grade of CR'.format(hardest[0])
        elif avMark >= 1:
            string = 'The hardest class is {0} with an average grade of PA'.format(hardest[0])
        else:
            string = 'The hardest class is {0} with an average grade of NN'.format(hardest[0])
        print(string)
   


                








    ## Exit Peter
    ## see main for what the two below functions do
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
    # a help function similar to the one in main displaying possible actions 
    def helpstudent():
        print('If you would like to\n\n1.Access your accedemic history \n2.Check your course or program information\n3.Enrol in a course\n4.Un enrol in a course \n5.See the easiest class\n6.See the hardest class\nexit.Return to the main menu')

    success = login(passwords)# if a successful login it starts the menu
    if success:
        finish = True
        print('\nwelcome to the student menu\n')
        helpstudent()  
        for i in students:
            if i.studentID == userID:
                user = i
    else :
        
        finish = False
        print('incorrect details')
        
        #################
        
    
    while finish: # wont start without finish being True which is determined by the login
        inp = input()
        ## returning to the base menu 
        # similar to main the matching imputs trigger the functions
        if inp.lower() == 'help': helpstudent()
        elif inp.lower() == 'exit': break
        elif inp.lower() == '1':
            ## work on this!
            displayAc(user) 
        elif inp.lower() == '2':
            courseQuery(input('What is the name or code of what you are querying:'))
        elif inp.lower() == '3':
            enrol(user,input('Please enter the course code:'),input('Please enter the semester and year in the format of SS,YYYY:'),input('Please enter the code of any preRequisite classes if none write none:'))
        elif inp.lower() == '4':
            unEnrol(user,input('Please enter the code of the course you wish to unenroll from:'))
        elif inp.lower() == '5':
            easy()
        elif inp.lower() == '6':
            hard()
        elif inp.lower() == 'search': printclassessearch(courses,input('To use the search function you need two imputs title and code if you dont want to search by title or code just press enter for the prompts\nIf you would like to display all courses press enter twice\nenter the title you would like to search for or else press enter to not search with title\n'),input('Enter the course code you would like to search for or else press enter to not search with code\n'))
        else: print('Imput error try again\nTry entering help to see the comands')
    print ('returning to main meu') 