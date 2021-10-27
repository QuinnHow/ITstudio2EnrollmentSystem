def studentMenu (courses,programs,semesters,students):
   
    

    
    #import Student
    #import Program
    #import Course
    #import Semester

    ## login Peter
    def login(students):
        print('Please sign in')
        studentnum = input('Enter your student number\n')
        pword = input('Enter your password\n')
        for i in students:
            if i.studentID == studentnum:
                ### we need a pasword for each student!!!!!!!!!!!
                if pword == i.pword:
                    return True
        return False

    ## Display academic history and current enrolment Quinn


    ## Querying course or program information Quinn 


    ## Enrol/UnEnrol in a current offering (You will need to consider the pre-req and the impact of an enrollment.) Quinn 


    ## Exit Peter
    def helpstudent():
        print('If you would like to\n\nAccess your accedemic history - enter academic history\nCheck your course or program information - enter course or program information\nEnrol - enter enrol\n Un enrol - enter un enrol\nReturn to the main menu - enter exit')

    success = login(students)
    if success:
        finish = True
        print('\nwelcome to the student menu\n')
        helpstudent()  
    else :
        ## change back to false when passwords are implimented as this True is just so we can test the other functions
        finish = True
        ## remove the print and help call when passwords have been implemented as they are there for testingstud
        print('welcome to the student menu\n')
        help()  
        #################
        print('incorrect details')
    
    while finish:
        inp = input()
        ## returning to the base menu 
        if inp.lower() == 'help': helpstudent()
        if inp.lower() == 'exit': break
        if inp.lower() == 'academic history':
            pass #acc hsit function 
        if inp.lower() == 'course or program information':
            pass #course or program information function
        if inp.lower() == 'enrol':
            pass #Enrol function
        if inp.lower() == 'un enrol':
            pass #Un enrol function
        else: print('Imput error try again\nTry entering help to see the comands')
    print ('returning to main meu') 