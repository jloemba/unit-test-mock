class Calculator:


    def initialize(self):
        self.sign = None

    def add(a,b):
        return round(a+b,2)

    def sub(a,b):
        return round(a-b,2)
    
    def mul(a,b):
        return round(a*b,2)

    def avg(a,b):
        if a > 0 and b > 0:

            if a != None and b != None:
                return round(a/b)
            else: return None

        else :
            return None



#print(round(4*(-1.1)))
#print(0*(-4))
print(round(6/2))
print(round(0/4))