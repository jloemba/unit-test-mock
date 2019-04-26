from validate_email import validate_email

class User:

    def __init__(self):
        self.email = None
        self.lastname = None
        self.firstname = None
        self.age = None

    def getEmail(self):
        return self.email

    def setEmail(self,value):
        self.email = value
    
    def getLastname(self):
        return self.lastname

    def setLastname(self,value):
        self.lastname = value

    def getFirstname(self):
        return self.firstname

    def setFirstname(self,value):
        self.firstname = value

    def getAge(self):
        return self.age
    
    def setAge(self,value):
        self.age = value
    
    def checkMail(self):
        #print(validate_email(self.email,verify=True))
        if(self.email != None and validate_email(self.email)): return True
        else: return None

    def checkAge(self):
        return (self.age > 13)

    def isValid(self):
        if(self.checkAge() and self.checkMail()): return True
        else: return None 


