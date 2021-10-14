class Semester:
    def __init__(self,ID,cOfferigns = []):
       ## in the format of S2 year(year is the year)
        self.ID = ID
       ## tupple (Name , max student avalibility , current students) 
        self.cOfferings = cOfferigns
