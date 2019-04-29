class Exchange:

    def __init__(self):
        self.receiver = None
        self.product = None
        self.owner = None
        self.sDate = None#Date de début
        self.eDate = None#Date de fin

    
    def getReceiver(self):
        return self.receiver

    def setReceiver(self,value):
        self.receiver = value
    
    def getProduct(self):
        return self.product

    def setProduct(self,value):
        self.product = value
    
    def getOwner(self):
        return self.owner

    def setOwner(self,value):
        self.owner = value
    
    def getSDate(self):
        return self.sDate

    def setSDate(self,value):
        self.sDate = value
    
    def getEDate(self):
        return self.eDate


    def setEDate(self,value):
        self.eDate = value

    def dateIsValid(self):
        if(self.getSDate() is not None and self.getEDate() is not None):
            print("Date non nulle")
            if(self.getSDate() < self.getEDate()):
                print("Date conforme")
                return True
            else: return None
        else: return None


    def save(self):
        if(self.getReceiver() is not None and self.getProduct() is not None):
            print("Non null")
            if(self.getReceiver().isValid() and self.getProduct().isValid()):
                print("Valide")
                if(self.dateIsValid()): return True
                else: return None
            else: 
                print("Non valide")
                return None
        else: 
            print("est null")
            return None
        