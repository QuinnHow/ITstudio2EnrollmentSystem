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
        statment = self.name + self.studentID + self.dob + self.programCode + self.studyPlan + self.curEnoll
        for i in self.accedemicHist:
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
    
