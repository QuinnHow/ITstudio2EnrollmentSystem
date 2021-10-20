
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
    print('Program code:',(self.code))
    print('Credit points:',(self.creditPoints))
    ## we want the corse code to be printed???????
    ## dose this use the strmethod from course????
    print('Core courses:',(self.core))
    print('Elective courses:',(self.elective))