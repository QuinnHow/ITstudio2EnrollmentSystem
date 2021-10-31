#import main
def studentMenu (courses,programs,semesters,students,passwords):
    
   
    

    
    import Student
    #import Program
    #import Course
    #import Semester

    ## login Peter
    def login(passwords):
        print('Please sign in')
        username = input('Enter your student number\n')
        pword = input('Enter your password\n')
        for i in passwords:
            if i.admin == '0' and i.username == username:
                ### we need a pasword for each student!!!!!!!!!!!
                if pword == i.password:
                    global userID
                    userID = username
                    return True
        return False
    
    ## Display academic history and current enrolment Quinn
    def displayAc(stu):
        
        i = 0
        print('Student Name:',stu.name)
        print('Student ID:',stu.studentID)
        print('Student Academic History:')        
        while i < len(stu.accedemicHist):
            
            x = eval(stu.accedemicHist[i])
                        
            print('In {0} a grade of {1} was acheived'.format(x[0], x[1]))
            i+=1
            
        
    
    ## Querying course or program information Quinn 
    def courseQuery(search):
        search = search.lower()
        for i in programs:
            if search == i.code:
                statement = 'The program {0} is {1} credit points in total it\'s core subjects are {2} and it\'s electives are {3}'.format(i.code, i.creditPoints, i.core, i.elective)
                break
            else:
                statement = 'No matching program found'    

        print(statement)


        for i in courses:
            if search == i.title or search == i.code:
                statement = 'The course {0}, with code {4} will be held in {1} it is {2} course credits and it\'s prerequisites are {3}'.format(i.title, i.avalSem, i.credit, i.preReq, i.code)
                break
            else:
                statement = 'No matching course found'
            
        print(statement)









    ## Enrol/UnEnrol in a current offering (You will need to consider the pre-req and the impact of an enrollment.) Quinn 
    def enrol(stu, code, semester, req):
        req = req.lower()
        meetsReq = True
        if req != 'none':
            for i in stu.accedemicHist:
                meetsReq = False
                i = eval(i)
                if i == req:
                    meetsReq = True
                    break
        if meetsReq == True:
            stu.curEnoll.append("(\'{0}\',\'{1}\')".format(code,semester))
            print('Completed')
        else:
            print('Pre-requisites not met or impropery entered')


    def unEnrol(stu,code):
        x = 0
        removal = False
        for i in stu.curEnoll:
            
            i = eval(i)
            if i[0] == code:
              stu.curEnoll.pop(x)
              removal = True
            
            x += 1    
        if removal == True:
            print('Removal succesful')
        else:
            print('No removal as no such course currently enrolled')


    






    ## Exit Peter
    def helpstudent():
        print('If you would like to\n\nAccess your accedemic history - enter academic history\nCheck your course or program information - enter course or program information\nEnrol - enter enrol\n Un enrol - enter un enrol\nReturn to the main menu - enter exit')

    success = login(passwords)
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
        
    
    while finish:
        inp = input()
        ## returning to the base menu 
        if inp.lower() == 'help': helpstudent()
        elif inp.lower() == 'exit': break
        elif inp.lower() == 'academic history':
            ## work on this!
            displayAc(user) 
        elif inp.lower() == 'course or program information':
            courseQuery(input('What is the name or code of what you are querying:'))
        elif inp.lower() == 'enrol':
            enrol(user,input('Please enter the course code:'),input('Please enter the semester and year in the format of SS,YYYY:'),input('Please enter the code of any preRequisite classes if none write none:'))
        elif inp.lower() == 'un enrol':
            unEnrol(user,input('Please enter the code of the course you wish to unenroll from:'))
        else: print('Imput error try again\nTry entering help to see the comands')
    print ('returning to main meu') 