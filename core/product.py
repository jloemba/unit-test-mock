class Product:

    label = ""
    owner = ""

    def __init__(self):
        self.label = None
        self.owner =  None

    def setLabel(self,value):
        self.label = value
    
    def getLabel(self):
        return label    

    def setOwner(self,value):
        self.owner = value

    def getOwner(self):
        return self.owner

    def isValid(self):
        return (self.label != "" and self.owner.isValid())        