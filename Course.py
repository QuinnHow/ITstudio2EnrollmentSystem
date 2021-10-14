class Course:
    def __init__(self,code,title,credit,points,preReq = [] ,avalSem = []):
        self.code = code
        self.title = title
        self.credit = credit
        self.points = points
        self.preReq = preReq
        self.avalSem = avalSem