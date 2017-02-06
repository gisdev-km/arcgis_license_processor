class License(object):
    ''' 
        The license object that contains users and functions for reporting total and available amounts
    '''
    def __init__(self, name=None, total=0, id=None, display=None, order=-1):
        self.id = id
        self.name = name
        self.total = int(total)
        self.users = [] # User: Machine
        self.avail = 0
        self.display = display
        self.order=order
        

    def addUser(self, hash=None, user=None, machine=None):
        self.users.append({ "hash": hash, "user": user, "machine": machine })

    @property
    def licensesInUse(self):
        '''
        Returns the total licenes in use based on the length of self.users
        '''
        numLicenses = len(self.users)

        return int(numLicenses)
    
    
    def calcValues(self):
        ''' 
        Master function to call sub functions that will calculate the total # of licenses, available and e-mails for people with licenses currently checked out
        '''
        self.calcLicenses()
        self.calcID()

    def calcLicenses(self):
        ''' 
        Calc available licenses based on total vs licenses in use
        '''
        self.avail = int(self.total) - self.licensesInUse
        try:
            self.availPercentage = float(self.avail) / float(self.total)
        except: 
            self.availPercentage = 0

    def calcID(self):
        '''
        Calculates the license ID, removes the "slash" for ARC/INFO
        '''
        self.id = self.id.replace("/","")