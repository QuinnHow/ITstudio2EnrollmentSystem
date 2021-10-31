#start 8/10/21
#last updated: 31/10/21
#Members: James Hijazin:s3895829 , Peter Fulton:s3896790, Quinn How:s3899122, Saicharan Kannan:s3814854. 
#The program is intended to allow students to enrol and observe their  programs and courses as well as allow administative staff to alter courses and student information.s
class Password:
    def __init__(self,admin=0, username = 'missing', password = 'password1'):
        self.admin = admin 
        self.username = username        
        self.password = password

        