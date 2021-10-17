class Course:
    def __init__(self,code,title,credit,preReq = [] ,avalSem = []):
        self.code = code
        self.title = title
        self.credit = credit
        self.preReq = preReq
        self.avalSem = avalSem