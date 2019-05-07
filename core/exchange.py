from service.dbconnection import DBConnection
from service.emailsender import EmailSender



class Exchange:

    def __init__(self):
        self.receiver = None
        self.product = None
        self.owner = None
        self.sDate = None#Date de début
        self.eDate = None#Date de fin
        self.db = DBConnection()
        self.mailer = EmailSender()

         

    
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
        #now = datetime.datetime.now()
        if(self.getSDate() is not None and self.getEDate() is not None):
            print("Date non nulle")
            if(  self.getSDate() and self.getSDate() < self.getEDate()):
                print("Date conforme")
                return True
            else: return None
        else: return None



    def checkUserAdult(self):
        if(self.getReceiver().getAge() > 18):
            return True
        else:
            return False

    

    def save(self):
            if(self.getReceiver().isValid() and self.getProduct().isValid()):
                if(self.dateIsValid()): 
                    if(self.checkUserAdult() is False):
                        message ="Bonjour %s , nous avons été informé de votre demande d'échange avec %s .Seulement nous ne pouvons l'autoriser au vu de votre âge."%(self.getReceiver(),self.getOwner(),)
                        return self.mailer.sendemail(self.getReceiver(),message)
                    else:
                        return self.db.insert(self.getReceiver(),self.getOwner(),self.getProduct())
                else: 
                    return None
            else: 
                message ="Bonjour %s , nous avons été informé de votre demande d'échange avec %s .Seulement nous ne pouvons l'autoriser au vu des critères non respectés."%(self.getReceiver(),self.getOwner(),)
                return self.mailer.sendemail(self.getReceiver(),message)
      