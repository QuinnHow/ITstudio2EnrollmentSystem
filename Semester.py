class Semester:
    def __init__(self,ID,cOfferings = []):
       ## in the format of S2 year(year is the year)
        self.ID = ID
       ## tuple (name, max student avalibility, current students) 
        self.cOfferings = cOfferings
