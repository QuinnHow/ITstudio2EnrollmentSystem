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
                    return True
        return False

    ## Display academic history and current enrolment Quinn
    def displayAc(stu):
        print('0000000000000000000000000000000000000000000000')
        i = 0
        print('Student Name:',stu.name)
        print('Student ID:',stu.studentID)
        print('Student Academic History:')        
        while i < len(stu.accedemicHist):
            
            x = eval(stu.accedemicHist[i])
                        
            print('In {0} a grade of {1} was acheived'.format(x[0], x[1]))
            i+=1
            
        
    
    ## Querying course or program information Quinn 
    









    ## Enrol/UnEnrol in a current offering (You will need to consider the pre-req and the impact of an enrollment.) Quinn 


    ## Exit Peter
    def helpstudent():
        print('If you would like to\n\nAccess your accedemic history - enter academic history\nCheck your course or program information - enter course or program information\nEnrol - enter enrol\n Un enrol - enter un enrol\nReturn to the main menu - enter exit')

    success = login(passwords)
    if success:
        finish = True
        print('\nwelcome to the student menu\n')
        helpstudent()  
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
            pass #acc hsit function 
        elif inp.lower() == 'course or program information':
            pass #course or program information function
        elif inp.lower() == 'enrol':
            pass #Enrol function
        elif inp.lower() == 'un enrol':
            pass #Un enrol function
        else: print('Imput error try again\nTry entering help to see the comands')
    print ('returning to main meu') 