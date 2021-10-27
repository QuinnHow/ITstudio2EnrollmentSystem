import csv


class Course:
    
    def __init__(self,code,title,credit,preReq = [] ,avalSem = []):
        self.code = code
        self.title = title
        self.credit = credit
        self.preReq = preReq
        self.avalSem = avalSem
    
        
    def __str__(self):
        statment = self.code + self.title + self.credit + self.preReq + self.avalSem
        return statment 


    def getCourse(self,code):
        if self.code == code:
            return True
        else:
            return False
        
