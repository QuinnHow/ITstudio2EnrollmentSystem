#start 8/10/21
#last updated: 31/10/21
#Members: James Hijazin:s3895829 , Peter Fulton:s3896790, Quinn How:s3899122, Saicharan Kannan:s3814854. 
#The program is intended to allow students to enrol and observe their  programs and courses as well as allow administative staff to alter courses and student information.
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