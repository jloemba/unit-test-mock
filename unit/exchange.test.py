

from datetime import *
import unittest
from core import user
from core import product
from core import exchange
from unittest.mock import patch, Mock


class TestUM(unittest.TestCase):
    
    @patch('service.dbconnection.DBConnection', autospec=True)
    @patch('service.emailsender.EmailSender', autospec=True)
    def setUp(self,mockdb,mockmailer):

        #help(MockUser)
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
        self.uC.setAge(19)

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


        # CAS 1 : Utilisateyr valide + Dates valides + Produit valide => Insertion en Base de données
        mockdb.return_value.message = "Insertion de l'échange"
        self.mockA = mockdb
        self.eA = exchange.Exchange()
        self.eA.setProduct(self.p1)
        self.eA.setOwner(self.uA)        
        self.eA.setReceiver(self.uC)
        self.eA.setSDate( datetime(2019, 6, 3) ) 
        self.eA.setEDate( datetime(2019, 6, 20) )

        # CAS 2 : Dates invalides car la date de début à lieu après la date de fin => Retourne nulle
        mockmailer.return_value.message = "Envoi du mail"
        self.mockB =  mockmailer

        self.eB = exchange.Exchange()
        self.eB.setProduct(self.p1)
        self.eB.setOwner(self.uA)        
        self.eB.setReceiver(self.uB)
        self.eB.setSDate( datetime(2019, 6, 20) )
        self.eB.setEDate( datetime(2019, 6, 3) )

        # CAS 3 : Produit non valide car le propriétaire n'est pas valide
        self.mockC =  mockmailer
        self.eC = exchange.Exchange()
        self.eC.setProduct(self.p2)
        self.eC.setOwner(self.uA)        
        self.eC.setReceiver(self.uB)
        self.eC.setSDate( datetime(2019, 6, 1) )
        self.eC.setEDate( datetime(2019, 6, 13) )

        # CAS 4 : Invalide car l'emprunteur n'est pas majeur => Envoie d'un mail
        self.mockD =  mockmailer
        self.eD = exchange.Exchange()
        self.eD.setProduct(self.p1)
        self.eD.setOwner(self.uA)        
        self.eD.setReceiver(self.uD)
        self.eC.setSDate( datetime(2019, 6, 1) )
        self.eC.setEDate( datetime(2019, 6, 13) )

    
    def testSave(self): #Ok
        self.assertEqual( self.eA.save() , self.mockA.return_value.message )  # CAS 1 : Utilisateyr valide + Dates valides + Produit valide => Insertion en Base de données
        self.assertEqual( self.eB.save() , None ) # CAS 2 : Dates invalides car la date de début à lieu après la date de fin => Retourne nulle
        self.assertEqual( self.eC.save() , self.mockC.return_value.message )# CAS 3 : Produit non valide car le propriétaire n'est pas valide
        self.assertEqual( self.eD.save() , self.mockD.return_value.message )# CAS 4 : Invalide car l'emprunteur n'est pas majeur => Envoie d'un mail
    

if __name__ == '__main__':
    unittest.main()