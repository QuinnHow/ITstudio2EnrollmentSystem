class Student:

    def __init__(self, name, studentID, dob, programCode, accedemicHist = [], studyPlan = [], curEnoll = [] ):
        self.name = name 
        self.studentID = studentID
        self.dob = dob
        self.programeCode = programCode
        # accedemic history is a lsit of tupples
        self.accedemicHist = accedemicHist
        # studdy plan history is a lsit of tupples
        self.studyPlan = studyPlan
        self.curEnoll = curEnoll


        
