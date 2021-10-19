class Semester:
    def __init__(self, ID, cOfferings = []):
       ## in the format of S2 year(year is the year)
        self.ID = ID
       ## tuple (name, max student avalibility, current students) 
        self.cOfferings = cOfferings

    def __str__(self):
        return '{}, {}'.format(self.ID, self.cOfferings)

    def getSemester(ID): ## may be changing this later
        semester = Semester.ID = ID
        return semester

    def setSemester(self, ID, cOfferings = []): ## may be changing this later
       ## in the format of S2 year(year is the year)
        self.ID = ID
       ## tuple (name, max student avalibility, current students) 
        self.cOfferings = cOfferings