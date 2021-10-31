#start 8/10/21
#last updated: 31/10/21
#Members: James Hijazin:s3895829 , Peter Fulton:s3896790, Quinn How:s3899122, Saicharan Kannan:s3814854. 
#The program is intended to allow students to enrol and observe their  programs and courses as well as allow administative staff to alter courses and student information.
class Student:

    def __init__(self, name ='Wrong', studentID ='Wrong', dob='Wrong', programCode='Wrong', accedemicHist = [()], studyPlan = [], curEnoll = [] ):
        self.name = name 
        self.studentID = studentID
        self.dob = dob
        self.programCode = programCode
        # accedemic history is a lsit of tupples
        self.accedemicHist = accedemicHist
        # studdy plan history is a lsit of tupples
        self.studyPlan = studyPlan
        self.curEnoll = curEnoll
    
    
    def __str__(self):
        statment = self.name + self.studentID + self.dob + self.programCode
        for i in self.accedemicHist:
            statment += i
        for i in self.studyPlan:
            statment += i
        for i in self.curEnoll:
            statment += i
        return statment

    def getStudent(ID):
        pass
        
    def setStudent( self, name, studentID, dob, programCode, accedemicHist = [()], studyPlan = [], curEnoll = [] ):
        self.name = name 
        self.studentID = studentID
        self.dob = dob
        self.programeCode = programCode
        # accedemic history is a lsit of tupples
        self.accedemicHist = accedemicHist
        # studdy plan history is a lsit of tupples
        self.studyPlan = studyPlan
        self.curEnoll = curEnoll

