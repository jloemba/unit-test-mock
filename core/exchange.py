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
    
    def getEDate(self,value):
        return self.eDate


    def save(self):