#Pour communiquer avec les autres sous répertoire
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import *
import unittest
from core import user
from core import product
from core import exchange


class TestUM(unittest.TestCase):
    
    def setUp(self):

        #---- Les utilisateurs-----
        # ----- User A(Majeur) -----
        self.uA = user.User()
        self.uA.setEmail('jorisloemba@gmail.com')
        self.uA.setLastname('Loemba')
        self.uA.setFirstname('Joris')
        self.uA.setAge(24)

        # ---- User B(Majeur)
        self.uB = user.User()
        self.uB.setEmail('jorisloemba@gmail.com')
        self.uB.setLastname('Loemba')
        self.uB.setFirstname('Joris')
        self.uB.setAge(18)

        # ---- User C(Mineur & plus de 13 ans)
        self.uC = user.User()
        self.uC.setEmail('jorisloemba@gmail.com')
        self.uC.setLastname('Loemba')
        self.uC.setFirstname('Joris')
        self.uC.setAge(15)

        # ---- User D(Mineur & moins de 13 ans)
        self.uD = user.User()
        self.uD.setEmail('jorisloemba@gmail.com')
        self.uD.setLastname('Loemba')
        self.uD.setFirstname('Joris')
        self.uD.setAge(12)


        #Le produit
        #CAS 1 : Label valide + owner valide
        self.p1 = product.Product()
        self.p1.setLabel("Pierre d'infinité")
        self.p1.setOwner(self.uA)

        #CAS 2 : Label valide + owner invalide
        self.p2 = product.Product()
        self.p2.setLabel("Pierre d'infinité")
        self.p2.setOwner(self.uD)

        #CAS 3 : Label invalide + owner invalide
        self.p3 = product.Product()
        self.p3.setLabel(None)
        self.p3.setOwner(self.uD)


        #Les échanges
        # CAS 1 : Utilisateyr valide + Dates valides + Produit valide
        self.eA = exchange.Exchange()
        self.eA.setProduct(self.p1)
        self.eA.setOwner(self.uA)        
        self.eA.setReceiver(self.uB)
        self.eA.setSDate( datetime(2019, 4, 3) ) 
        self.eA.setEDate( datetime(2019, 4, 20) )

        # CAS 2 : Utilisateur valide + Dates invalides  + Produit valide
        self.eB = exchange.Exchange()
        self.eB.setProduct(self.p1)
        self.eB.setOwner(self.uA)        
        self.eB.setReceiver(self.uB)
        self.eB.setSDate( datetime(2019, 4, 20) )
        self.eB.setEDate( datetime(2019, 4, 3) )

        # CAS 3 : Utilisateur invalide + Dates invalides + Produit valide
        self.eC = exchange.Exchange()
        self.eC.setProduct(self.p1)
        self.eC.setOwner(self.uA)        
        self.eC.setReceiver(self.uB)
        self.eC.setSDate( datetime(2019, 4, 30) )
        self.eC.setEDate( datetime(2019, 4, 3) )

        # CAS 3 : Utilisateur invalide + Dates nulles + Produit valide
        self.eD = exchange.Exchange()
        self.eD.setProduct(self.p1)
        self.eD.setOwner(self.uA)        
        self.eD.setReceiver(self.uB)
        self.eD.setSDate(None)
        self.eD.setEDate(None)

        # CAS 3 : Utilisateur invalide + Dates nulles + Produit valide
        self.eE = exchange.Exchange()
        self.eE.setProduct(self.p1)
        self.eE.setOwner(self.uA)        
        self.eE.setReceiver(self.uB)
        self.eE.setSDate( datetime(2019, 4, 3) )
        self.eE.setEDate(None)

        # CAS 3 : Utilisateur valide + Dates nulles + Produit invalide
        self.eF = exchange.Exchange()
        self.eF.setProduct(self.p2)
        self.eF.setOwner(self.uA)        
        self.eF.setReceiver(self.uB)
        self.eF.setSDate(None)
        self.eF.setEDate(None)

    def testSave(self): #Ok
        self.assertEqual( self.eA.save() , True) 
        self.assertEqual( self.eB.save() , None)
        self.assertEqual( self.eC.save() , None)
        self.assertEqual( self.eD.save() , None)
        self.assertEqual( self.eE.save() , None)
        self.assertEqual( self.eF.save() , None)
    

if __name__ == '__main__':
    unittest.main()