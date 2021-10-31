#start 8/10/21
#last updated: 31/10/21
#Members: James Hijazin:s3895829 , Peter Fulton:s3896790, Quinn How:s3899122, Saicharan Kannan:s3814854. 
#The program is intended to allow students to enrol and observe their  programs and courses as well as allow administative staff to alter courses and student information.
import csv


class Course:
    
    def __init__(self,code,title,credit,preReq = [] ,avalSem = []):
        self.code = code
        self.title = title
        self.credit = credit
        self.preReq = preReq
        self.avalSem = avalSem
    
        
    def __str__(self):
        statment = self.code + " " + self.title + " "+self.credit +" "+ self.preReq +" "+ self.avalSem
        return statment 


    def getCourse(self,code):
        if self.code == code:
            return True
        else:
            return False
        
