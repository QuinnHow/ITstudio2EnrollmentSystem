def studentMenu (courses,programs,semesters,students):
    ## needs to be after the function deffinitions
    success = login(students)
    if success:
        finish = True
    else :finish = False
    while finish:
        inp = input('welcome to the student menu, What would you like to do?\n')
        ## returning to the base menu 
        if inp.lower() == 'exit': break

    print ('returning to main meu') 
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
