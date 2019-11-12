#!/usr/bin/python3
import unittest
import sys
from unittest.mock import patch

import factures
import listeDeListes
import tri

class TestTD7(unittest.TestCase):

    def enlever_caracteres(self,chaine,cars=' '):
        res=''
        for c in chaine:
            if c not in cars:
                res+=c
        return res

    def setUp(self):
        self.liste1=[[12,4,6],[7,4],[6,9,11],[]]
        self.liste2=[[],[4,7],[9,15,12]]
        self.liste3=[]
        self.facture1=[(123,"Dupont",[("Verre",6,2.4),("Assiette",6,1.5)]),(125,"Durand",[("Vase",1,10.0)])]
        self.res1=[(123, 'Dupont', 23.4), (125, 'Durand', 10.0)]
        self.aff1="--------------------\nnuméro: 123 Nom: Dupont\nproduit               qte       prix      total\nVerre                   6 *     2.40 =    14.40\nAssiette                6 *     1.50 =     9.00\n                                       --------\ntotal                                     23.40\n--------------------\nnuméro: 125 Nom: Durand\nproduit               qte       prix      total\nVase                    1 *    10.00 =    10.00\n                                       --------\ntotal                                     10.00\n"

        self.facture2=[(154,"Duval",[("Vase",2,10.0),("Assiette",2,1.5),("Verre",3,2.0)])]
        self.res2=[(154, 'Duval', 29.0)]
        self.aff2="--------------------\nnuméro: 154 Nom: Duval\nproduit               qte       prix      total\nVase                    2 *    10.00 =    20.00\nAssiette                2 *     1.50 =     3.00\nVerre                   3 *     2.00 =     6.00\n                                       --------\ntotal                                     29.00\n"

        self.listet1=[7,3,6,2,6,7,1]
        self.tri1='[3, 6, 2, 6, 7, 1, 7]\n[3, 2, 6, 6, 1, 7, 7]\n[2, 3, 6, 1, 6, 7, 7]\n[2, 3, 1, 6, 6, 7, 7]\n[2, 1, 3, 6, 6, 7, 7]\n[1, 2, 3, 6, 6, 7, 7]\n'
        self.listet2=[12,4,5,7,5,6]
        self.tri2='[4, 5, 7, 5, 6, 12]\n[4, 5, 5, 6, 7, 12]\n[4, 5, 5, 6, 7, 12]\n[4, 5, 5, 6, 7, 12]\n[4, 5, 5, 6, 7, 12]\n'

        
    def test_liste_de_listes_to_str(self):
        self.assertEqual(listeDeListes.liste_de_listes_to_str(self.liste1),"1246\n74\n6911\n\n","Pb avec l'appel liste_de_listes_to_str("+str(self.liste1)+")")
        self.assertEqual(listeDeListes.liste_de_listes_to_str(self.liste2),"\n47\n91512\n","Pb avec l'appel liste_de_listes_to_str("+str(self.liste2)+")")
        self.assertEqual(listeDeListes.liste_de_listes_to_str(self.liste3),"","Pb avec l'appel liste_de_listes_to_str("+str(self.liste3)+")")


    def test_max_dans_liste_de_listes(self):
        self.assertEqual(listeDeListes.max_dans_liste_de_listes(self.liste1),12,"Pb avec l'appel max_dans_liste_de_listes("+str(self.liste1)+")")
        self.assertEqual(listeDeListes.max_dans_liste_de_listes(self.liste2),15,"Pb avec l'appel max_dans_liste_de_listes("+str(self.liste2)+")")
        self.assertEqual(listeDeListes.max_dans_liste_de_listes(self.liste3),None,"Pb avec l'appel max_dans_liste_de_listes("+str(self.liste3)+")")

    def test_max_par_ligne_dans_liste_de_listes(self):
        self.assertEqual(listeDeListes.max_par_ligne_dans_liste_de_listes(self.liste1),[12,7,11,None],"Pb avec l'appel max_par_ligne_dans_liste_de_listes("+str(self.liste1)+")")
        self.assertEqual(listeDeListes.max_par_ligne_dans_liste_de_listes(self.liste2),[None,7,15],"Pb avec l'appel max_par_ligne_dans_liste_de_listes("+str(self.liste2)+")")
        self.assertEqual(listeDeListes.max_par_ligne_dans_liste_de_listes(self.liste3),[],"Pb avec l'appel max_par_ligne_dans_liste_de_listes("+str(self.liste3)+")")
        
    def test_factures(self):
        self.assertEqual(factures.factures(self.facture1),self.res1,"Pb avec l'appel factures("+str(self.facture1)+")")
        self.assertEqual(factures.factures(self.facture2),self.res2,"Pb avec l'appel factures("+str(self.facture2)+")")

    def test_affiche_factures(self):
        out=sys.stdout
        sys.stdout = open('tmp1.txt', 'w')
        try:
            factures.affiche_factures(self.facture1)
        except:
            pass
        sys.stdout.close()
        sys.stdout=out
        fic=open('tmp1.txt','r')
        res=fic.read()
        fic.close()
        self.assertEqual(self.enlever_caracteres(res," \t-"),self.enlever_caracteres(self.aff1," \t-"),"Pb avec l'appel affiche_factures("+str(self.facture1)+")")
        out=sys.stdout
        sys.stdout = open('tmp1.txt', 'w')
        try:
            factures.affiche_factures(self.facture2)
        except:
            pass
        sys.stdout.close()
        sys.stdout=out
        fic=open('tmp1.txt','r')
        res=fic.read()
        fic.close()
        self.assertEqual(self.enlever_caracteres(res," \t-"),self.enlever_caracteres(self.aff2," \t-"),"Pb avec l'appel affiche_factures("+str(self.facture2)+")")

    
    def test_tri(self):
        l1=self.listet1[:]
        out=sys.stdout
        sys.stdout = open('tmp1.txt', 'w')
        try:
            tri.tri(l1)
        except:
            pass
        sys.stdout.close()
        sys.stdout=out
        fic=open('tmp1.txt','r')
        res=fic.read()
        fic.close()
        self.assertEqual(res,self.tri1,"Pb avec l'appel tri("+str(self.listet1)+")")
        l2=self.listet2[:]
        out=sys.stdout
        sys.stdout = open('tmp1.txt', 'w')
        try:
            tri.tri(l2)
        except:
            pass
        sys.stdout.close()
        sys.stdout=out
        fic=open('tmp1.txt','r')
        res=fic.read()
        fic.close()
        self.assertEqual(res,self.tri2,"Pb avec l'appel tri("+str(self.listet2)+")")

        
if __name__ == '__main__':
    unittest.main()
