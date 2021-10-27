class Student:

    def __init__(self, name, studentID, dob, programCode, accedemicHist = [], studyPlan = [], curEnoll = [] ):
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
        statment = self.name + self.studentID + self.dob + self.programCode + self.accedemicHist + self.studyPlan + self.curEnoll
        return statment

    def getStudent(ID):
        student = Student.studentID == ID
        return student
        
    def setStudent( self, name, studentID, dob, programCode, accedemicHist = [], studyPlan = [], curEnoll = [] ):
        self.name = name 
        self.studentID = studentID
        self.dob = dob
        self.programeCode = programCode
        # accedemic history is a lsit of tupples
        self.accedemicHist = accedemicHist
        # studdy plan history is a lsit of tupples
        self.studyPlan = studyPlan
        self.curEnoll = curEnoll
    
