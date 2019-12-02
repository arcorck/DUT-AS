#!/usr/bin/python3
import unittest


from transport import *

class TestTransport(unittest.TestCase):
    def setUp(self):
        self.p1=Personne("toto",42,"tram")
        self.p2=Personne("titi",35,"vélo")
        self.p3=Personne("tutu",25,"vélo")
        self.p4=Personne("tyty",44,"tram")
        self.p5=Personne("xxx",22,"voiture")
        self.lp=[self.p1,self.p2,self.p3,self.p4,self.p5]
    
    def test_get_nom(self):
        self.assertEqual(get_nom(self.p1),"toto","Pb avec l'appel get_nom("+str(self.p1)+")")
        self.assertEqual(get_nom(self.p3),"tutu","Pb avec l'appel get_nom("+str(self.p3)+")")
        self.assertEqual(get_nom(self.p5),"xxx","Pb avec l'appel get_nom("+str(self.p5)+")")


    def test_get_age(self):
        self.assertEqual(get_age(self.p1),42,"Pb avec l'appel get_age("+str(self.p1)+")")
        self.assertEqual(get_age(self.p2),35,"Pb avec l'appel get_age("+str(self.p2)+")")
        self.assertEqual(get_age(self.p4),44,"Pb avec l'appel get_age("+str(self.p4)+")")
        

    def test_get_moyen_transport(self):
        self.assertEqual(get_moyen_transport(self.p1),"tram","Pb avec l'appel get_moyen_transport("+str(self.p1)+")")
        self.assertEqual(get_moyen_transport(self.p3),"vélo","Pb avec l'appel get_moyen_transport("+str(self.p3)+")")
        self.assertEqual(get_moyen_transport(self.p5),"voiture","Pb avec l'appel get_moyen_transport("+str(self.p5)+")")
        

    def test_set_nom(self):
        p=Personne("xxx",32,"vélo")
        for nom in ['yyyy','zzzz','wwww']:
            set_nom(p,nom)
            self.assertEqual(get_nom(p),nom,"Pb avec l'appel set_nom("+str(p)+","+nom+")")

    def test_set_age(self):
        p=Personne("xxx",32,"vélo")
        for age in [12,25,55]:
            set_age(p,age)
            self.assertEqual(get_age(p),age,"Pb avec l'appel set_age("+str(p)+","+str(age)+")")

    def test_set_moyen_transport(self):
        p=Personne("xxx",32,"vélo")
        for moyen in ["train","voiture","fusée"]:
            set_moyen_transport(p,moyen)
            self.assertEqual(get_moyen_transport(p),moyen,"Pb avec l'appel set_moyen_transport("+str(p)+","+str(moyen)+")")


    def test_age_moyen_utilisateur_transport(self):
        res=[("tram",43),("vélo",30),("voiture",22),("fusée",-1)]
        for moyen,age in res:
            self.assertEqual(age_moyen_utilisateur_transport(self.lp,moyen),age,"Pb avec l'appel set_moyen_transport("+str(self.lp)+','+str(moyen)+")\n")


    def test_liste_moyens_transport(self):
        self.assertEqual(liste_moyens_transport([]),[],"Pb avec l'appel liste_moyens_transport([])")
        res=liste_moyens_transport(self.lp)
        res.sort()
        attendu=["tram","vélo","voiture"]
        attendu.sort()
        self.assertEqual(res,attendu,"Pb avec l'appel liste_moyens_transport("+str(self.lp)+")")
        
        
if __name__ == '__main__':
    unittest.main()
