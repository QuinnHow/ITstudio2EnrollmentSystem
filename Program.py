#start 8/10/21
#last updated: 31/10/21
#Members: James Hijazin:s3895829 , Peter Fulton:s3896790, Quinn How:s3899122, Saicharan Kannan:s3814854. 
#The program is intended to allow students to enrol and observe their  programs and courses as well as allow administative staff to alter courses and student information.
class Program:
    def __init__(self,code,credPoints,core = [], elective = [] ):
        self.code = code
        self.creditPoints = credPoints
        self.core = core
        self.elective = elective

    def add_core(self,course):
        self.core = self.core.append(course)
    def add_eletive(self,course):
        self.elective = self.elective.append(course)
    
    def remove_core(self,course):
    ## checking if the course exists within the program before removing 
        if self.core[course]:
            self.core = self.core.pop(course)
    def remove_elective(self,course):
        if self.elective[course]:
            self.elective = self.elective.pop(course)

    def __str__(self):
        return 'Program code: ' + str(self.code) + '\n' + 'Credit points: ' + str(self.creditPoints) + '\n' + 'Core courses: ' + str(self.core) + '\n' + 'Elective courses: ' + str(self.elective)
# testing str function#############################################
#cheese = [3,2,1]
#cheese.append(4)
#temp = Program(123,45,cheese,('cheese','burger'))
#print (temp)
# output was :
#Program code: 123
#Credit points: 45
#Core courses: [3, 2, 1, 4]
#Elective courses: ('cheese', 'burger')
###################################################################
