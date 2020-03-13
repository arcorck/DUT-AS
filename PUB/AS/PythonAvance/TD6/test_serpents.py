#!/usr/bin/python3
import unittest
from unittest.mock import patch

import serpents as serpents

class TestSerpent(unittest.TestCase):
    def setUp(self):
        self.s1=("Python3",0.3,0)
        self.s2=("titi",1.2,1)
        self.s3=("tutu",2.5,2)
        self.s4=("tyty",0.5,4)
        self.s5=("xxx",0.9,4)
        self.s6=("yyy",0.7,1)
        self.s7=("zzz",0.8,1)
        self.s8=("uuu",1.4,2)
        self.s9=("vvv",0.3,5)

        self.ls=[self.s1,self.s2,self.s3,self.s4,self.s5,\
                 self.s6,self.s7,self.s8]

    def test_serpent_to_str(self):
        self.assertEqual(serpents.serpent_to_str(self.s1),"--------------------\nNom: Python3\nTaille: 0.3\nDanger: 0\n--------------------\n","Pb avec l'appel serpent_to_str("+str(self.s1)+")")
        self.assertEqual(serpents.serpent_to_str(self.s3),"--------------------\nNom: tutu\nTaille: 2.5\nDanger: 2\n--------------------\n","Pb avec l'appel serpent_to_str("+str(self.s3)+")")


    def test_liste_serpents_to_str(self):
        self.assertEqual(serpents.liste_serpents_to_str(self.ls),"--------------------\nNom: Python3\nTaille: 0.3\nDanger: 0\n--------------------\n--------------------\nNom: titi\nTaille: 1.2\nDanger: 1\n--------------------\n--------------------\nNom: tutu\nTaille: 2.5\nDanger: 2\n--------------------\n--------------------\nNom: tyty\nTaille: 0.5\nDanger: 4\n--------------------\n--------------------\nNom: xxx\nTaille: 0.9\nDanger: 4\n--------------------\n--------------------\nNom: yyy\nTaille: 0.7\nDanger: 1\n--------------------\n--------------------\nNom: zzz\nTaille: 0.8\nDanger: 1\n--------------------\n--------------------\nNom: uuu\nTaille: 1.4\nDanger: 2\n--------------------\n","Pb avec l'appel liste_serpents_to_str("+str(self.ls)+")")


    def test_saisir_un_serpent(self):
        user_input = ['toto','1.0','1','titi','2','3']

        with patch('builtins.input', side_effect=user_input):
            self.assertEqual(serpents.saisir_un_serpent(),('toto',1.0,1),"Pb avec l'appel saisir_un_serpent()")
            self.assertEqual(serpents.saisir_un_serpent(),('titi',2.0,3),"Pb avec l'appel saisir_un_serpent()")


    def test_ajouter_serpents(self):
        l=[self.s1]
        user_input=['toto','1.0','1','O','titi','2','3','N']
        with patch('builtins.input', side_effect=user_input):
            serpents.ajouter_serpents(l)
            self.assertEqual(l,[self.s1,('toto',1.0,1),('titi',2.0,3)],"Pb avec l'appel ajouter_serpents()")

    def test_sauver_serpents(self):
        serpents.sauver_serpents("testsauve.txt",self.ls[:3])
        fic=open("testsauve.txt")
        contenu=fic.read()
        fic.close()
        self.assertEqual(contenu,"Python3,0.3,0\ntiti,1.2,1\ntutu,2.5,2\n","Pb avec l'appel ajouter_serpents('testsauve.txt',"+str(self.ls[:3])+")")

    def test_charger_serpents(self):
        fic=open("testsauve.txt","w")
        fic.write("Python3,0.3,0\ntiti,1.2,1\ntutu,2.5,2\n")
        fic.close()
        self.assertEqual(serpents.charger_serpents("testsauve.txt"),self.ls[:3], "Pb avec l'appel charger_serpents('testsauve.txt')")

    def test_rechercher_dangereux(self):
        self.assertEqual(serpents.rechercher_dangereux(self.ls),[],"Pb avec l'appel rechercher_dangereux("+str(self.ls)+"')")
        self.assertEqual(serpents.rechercher_dangereux(self.ls+[self.s9]),[self.s9[0]],"Pb avec l'appel rechercher_dangereux("+str(self.ls+[self.s9])+"')")

    def test_moyenne_taille_dangerosite(self):
        self.assertEqual(serpents.moyenne_taille_dangerosite(self.ls,4),0.7,"Pb avec l'appel moyenne_taille_dangerosite("+str(self.ls)+",4)")
        self.assertEqual(serpents.moyenne_taille_dangerosite(self.ls,1),0.9,"Pb avec l'appel moyenne_taille_dangerosite("+str(self.ls)+",1)")

    def test_nb_serpents_par_danger(self):
        self.assertEqual(serpents.nb_serpents_par_danger(self.ls),[1,3,2,0,2,0],"Pb avec l'appel nb_serpents_par_danger("+str(self.ls)+")")
        self.assertEqual(serpents.nb_serpents_par_danger(self.ls[:5]),[1,1,1,0,2,0],"Pb avec l'appel nb_serpents_par_danger("+str(self.ls[:5])+")")



if __name__ == '__main__':
    unittest.main()
