#Pour communiquer avec les autres sous répertoire
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from core import user
from core import product

class TestUM(unittest.TestCase):
    
    def setUp(self):

        #---- Les utilisateurs-----
        # ----- User A(Majeur) -----
        self.u = user.User()
        self.u.setEmail('jorisloemba@gmail.com')
        self.u.setLastname('Loemba')
        self.u.setFirstname('Joris')
        self.u.setAge(24)

        # ---- User B(Majeur)

        # ---- User C(Mineur & plus de 13 ans)

        # ---- User D(Mineur & moins de 13 ans)

        #Le produit
        self.p = product.Product()
        self.p.setLabel("Marteau de Thor")
        self.p.setOwner(self.u)




    def testIsValid(self): #Ok
        self.assertEqual( self.p.isValid() , True)
    

if __name__ == '__main__':
    unittest.main()