class Semester:
    def __init__(self, ID, cOfferings = []):
       ## in the format of S2 year(year is the year)
        self.ID = ID
       ## tuple (name, max student avalibility, current students (list of student ids)) 
        self.cOfferings = cOfferings

    def __str__(self):
        return '{}, {}'.format(self.ID, self.cOfferings)


    def add_cOffer(self, cOffer):
        if self.cOfferings[1] == self.cOfferings[2]:
            print('Max students reached!')
        else:
            self.cOfferings = self.cOfferings.append(cOffer)

    def remove_cOffer(self,cOffer):
        if self.cOfferings[cOffer]:
            self.cOfferings = self.cOfferings.pop(cOffer)
    
    def getSemester(ID): ## may be changing this later
        semester = Semester.ID = ID
        return semester

    def setSemester(self, ID, cOfferings = []): ## may be changing this later
       ## in the format of S2 year(year is the year)
        self.ID = ID
       ## tuple (name, max student avalibility, current students) 
        self.cOfferings = cOfferings