import unittest
import calculator


class TestUM(unittest.TestCase):
    
    
    def setUp(self):
        self.c = calculator.Calculator
        
    #Pour chaque opération, avoir un cas :
    # Entier et Entier   
    # Décimal et Entier   
    # Décimal et Décimal
    # Décimal et Nombre relative
    # 0 et Décimal      
    # Null et Null
    # Entier(ou autre) et Null
 
    def test_add(self): #Ok
        
        self.assertEqual( self.c.add(3,4), 7)
        self.assertEqual( self.c.add(1.4,4), 5.4)
        self.assertEqual( self.c.add(1.4,4.4), 5.8)
        self.assertEqual( self.c.add(1.4,-4), -2.6)
        self.assertEqual( self.c.add(0,-4), -4)


    def test_sub(self): #Ok
        self.assertEqual( self.c.sub(4,3), 1)
        self.assertEqual( self.c.sub(4,-1.1), 5.1)
        self.assertEqual( self.c.sub(4.4,1.1), 3.3)
        self.assertEqual( self.c.sub(-1.4,4), -5.4)
        self.assertEqual( self.c.sub(0,-4), 4)


    def test_multiply(self): #Ok
        self.assertEqual( self.c.mul(4,3), 12)
        self.assertEqual( self.c.mul(4,-1.1), -4.4)
        self.assertEqual( self.c.mul(4.4,1.1), 4.84)
        self.assertEqual( self.c.mul(-1.4,4), -5.6)
        self.assertEqual( self.c.mul(0,-4), 0)


    def test_avg(self): #Ok
        self.assertEqual( self.c.avg(12,-1.1), None)
        self.assertEqual( self.c.avg(-1.4,4), None)
        self.assertEqual( self.c.avg(0,4), None)
        self.assertEqual( self.c.avg(20,4), 5)


if __name__ == '__main__':
    unittest.main()