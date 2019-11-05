#!/usr/bin/python3
import unittest
from unittest.mock import patch

import tp7

class TestTp7(unittest.TestCase):
    def message(self,fun,liste_param):
        res="Pb avec l'appel "+fun.__name__+"("
        pref=" "
        for param in liste_param:
            res+=pref+str(param)
            pref=", "
        res+=" )"
        return res
    
    
    def setUp(self):
        self.scores1=[352100,325410,312785,220199,127853]
        self.joueurs1=['Batman','Robin','Batman','Joker','Batman']
        self.cont_fic1='352100,Batman\n325410,Robin\n312785,Batman\n220199,Joker\n127853,Batman\n'
        self.cont_html1='<table>\n<tr> <td>Rang</td> <td>Nom</td> <td>Score</td> </tr>\n<tr> <td>1.</td> <td>Batman</td> <td>352100</td> </tr>\n<tr> <td>2.</td> <td>Robin</td> <td>325410</td> </tr>\n<tr> <td>3.</td> <td>Batman</td> <td>312785</td> </tr>\n<tr> <td>4.</td> <td>Joker</td> <td>220199</td> </tr>\n<tr> <td>5.</td> <td>Batman</td> <td>127853</td> </tr>\n</table>\n'
        self.scores2=[423752,352100,325410,312785,220199,127853]
        self.joueurs2=['Robin','Batman','Robin','Batman','Joker','Batman']
        self.cont_fic2='423752,Robin\n352100,Batman\n325410,Robin\n312785,Batman\n220199,Joker\n127853,Batman\n'
        self.scores3=[352100,325410,312785,252145,220199,127853]
        self.joueurs3=['Batman','Robin','Batman','Oui Oui','Joker','Batman']
        self.cont_fic3='352100,Batman\n325410,Robin\n312785,Batman\n252145,Oui Oui\n220199,Joker\n127853,Batman\n'
        self.scores4=[352100,325410,312785,220199,127853,988]
        self.joueurs4=['Batman','Robin','Batman','Joker','Batman','Robin']
        self.cont_fic4='352100,Batman\n325410,Robin\n312785,Batman\n220199,Joker\n127853,Batman\n988,Robin\n'

        

    #def test_affiche_classement(scores,joueurs):
        #"""
        #affiche le classement des joueurs
        #paramètres:
        #pas de résultat
        #"""
        #...
        
    # exercice 2
    def test_decroissant(self):
        self.assertTrue(tp7.decroissant(self.scores1),
                        self.message(tp7.decroissant,[self.scores1]))
        self.assertFalse(tp7.decroissant([10,9,8,11]),
                         self.message(tp7.decroissant,[[10,9,8,11]]))
        self.assertTrue(tp7.decroissant([]),
                        self.message(tp7.decroissant,[[]]))
                
    #exercice 3
    def test_meilleur_score_joueur(self):
        self.assertEqual(tp7.meilleur_score_joueur("Batman",self.scores1,self.joueurs1),352100,
                         self.message(tp7.meilleur_score_joueur,["Batman",self.scores1,self.joueurs1]))
        self.assertEqual(tp7.meilleur_score_joueur("Joker",self.scores1,self.joueurs1),220199,
                         self.message(tp7.meilleur_score_joueur,["Joker",self.scores1,self.joueurs1]))
        self.assertEqual(tp7.meilleur_score_joueur("Oui Oui",self.scores1,self.joueurs1),-1,
                         self.message(tp7.meilleur_score_joueur,["Oui Oui",self.scores1,self.joueurs1]))
        self.assertEqual(tp7.meilleur_score_joueur("Batman",[],[]),-1,
                         self.message(tp7.meilleur_score_joueur,["Batman",[],[]]))
        
        
    # exercice 5
    def test_nb_fois_meilleur(self):
        self.assertEqual(tp7.nb_fois_meilleur("Batman",self.scores1,self.joueurs1),3,
                         self.message(tp7.nb_fois_meilleur,["Batman",self.scores1,self.joueurs1]))
        self.assertEqual(tp7.nb_fois_meilleur("Joker",self.scores1,self.joueurs1),1,
                         self.message(tp7.nb_fois_meilleur,["Joker",self.scores1,self.joueurs1]))
        self.assertEqual(tp7.nb_fois_meilleur("Oui Oui",self.scores1,self.joueurs1),0,
                         self.message(tp7.nb_fois_meilleur,["Oui Oui",self.scores1,self.joueurs1]))
        self.assertEqual(tp7.nb_fois_meilleur("Batman",[],[]),0,
                         self.message(tp7.nb_fois_meilleur,["Batman",[],[]]))
        
    # exercice 6
    
    # exercice 7
    def test_meilleur_classement_joueur(self):
        self.assertEqual(tp7.meilleur_classement_joueur("Batman",self.scores1,self.joueurs1),1,
                         self.message(tp7.meilleur_classement_joueur,["Batman",self.scores1,self.joueurs1]))
        self.assertEqual(tp7.meilleur_classement_joueur("Joker",self.scores1,self.joueurs1),4,
                         self.message(tp7.meilleur_classement_joueur,["Joker",self.scores1,self.joueurs1]))
        self.assertEqual(tp7.meilleur_classement_joueur("Oui Oui",self.scores1,self.joueurs1),-1,
                         self.message(tp7.meilleur_classement_joueur,["Oui Oui",self.scores1,self.joueurs1]))
        self.assertEqual(tp7.meilleur_classement_joueur("Batman",[],[]),-1,
                         self.message(tp7.meilleur_classement_joueur,["Batman",[],[]]))
     
    # exercice 8
    def test_placeScore(self):
        self.assertEqual(tp7.placeScore(421252,self.scores1),0,
                         self.message(tp7.placeScore,[421252,self.scores1]))
        self.assertEqual(tp7.placeScore(250988,self.scores1),3,
                         self.message(tp7.placeScore,[250988,self.scores1]))
        self.assertEqual(tp7.placeScore(988,self.scores1),5,
                         self.message(tp7.placeScore,[988,self.scores1]))

    # exercice 9
    def test_ajouter_score(self):
        scores=self.scores1[:]
        joueurs=self.joueurs1[:]
        tp7.ajouter_score(423752,'Robin',scores,joueurs)
        self.assertEqual((scores,joueurs),(self.scores2,self.joueurs2),
                         self.message(tp7.ajouter_score,[423752,'Robin',self.scores1,self.joueurs1]))
        scores=self.scores1[:]
        joueurs=self.joueurs1[:]
        tp7.ajouter_score(252145,'Oui Oui',scores,joueurs)
        self.assertEqual((scores,joueurs),(self.scores3,self.joueurs3),
                         self.message(tp7.ajouter_score,[252145,'Oui Oui',self.scores1,self.joueurs1]))
        scores=self.scores1[:]
        joueurs=self.joueurs1[:]
        tp7.ajouter_score(988,'Robin',scores,joueurs)
        self.assertEqual((scores,joueurs),(self.scores4,self.joueurs4),
                         self.message(tp7.ajouter_score,[988,'Robin',self.scores1,self.joueurs1]))
        
        scores=[]
        joueurs=[]
        tp7.ajouter_score(19881,'Batman',scores,joueurs)
        self.assertEqual((scores,joueurs),([19881],['Batman']),
                         self.message(tp7.ajouter_score,[19881,'Batman',[],[]]))
    
    
    def test_ajouter_score_limite(self):
        scores=self.scores1[:]
        joueurs=self.joueurs1[:]
        tp7.ajouter_score_limite(423752,'Robin',scores,joueurs,5)
        self.assertEqual((scores,joueurs),(self.scores2[:5],self.joueurs2[:5]),
                         self.message(tp7.ajouter_score_limite,[423752,'Robin',self.scores1,self.joueurs1,5]))
        scores=self.scores1[:]
        joueurs=self.joueurs1[:]
        tp7.ajouter_score_limite(252145,'Oui Oui',scores,joueurs,5)
        self.assertEqual((scores,joueurs),(self.scores3[:5],self.joueurs3[:5]),
                         self.message(tp7.ajouter_score_limite,[252145,'Oui Oui',self.scores1,self.joueurs1,5]))
        scores=self.scores1[:]
        joueurs=self.joueurs1[:]
        tp7.ajouter_score_limite(988,'Robin',scores,joueurs,5)
        self.assertEqual((scores,joueurs),(self.scores4[:5],self.joueurs4[:5]),
                         self.message(tp7.ajouter_score_limite,[988,'Robin',self.scores1,self.joueurs1,5]))
        
        scores=[]
        joueurs=[]
        tp7.ajouter_score_limite(19881,'Batman',scores,joueurs,5)
        self.assertEqual((scores,joueurs),([19881],['Batman']),
                         self.message(tp7.ajouter_score_limite,[19881,'Batman',[],[],5]))
        
    
    # exercice 11
    def test_sauver_score(self):
        tp7.sauver_score('tmp.txt',self.scores1,self.joueurs1)
        fic=open('tmp.txt')
        cont=fic.read()
        fic.close()
        self.assertEqual(cont,self.cont_fic1,
                         self.message(tp7.sauver_score,['tmp.txt',self.scores1,self.joueurs1]))
        
        tp7.sauver_score('tmp.txt',self.scores2,self.joueurs2)
        fic=open('tmp.txt')
        cont=fic.read()
        fic.close()
        self.assertEqual(cont,self.cont_fic2,
                         self.message(tp7.sauver_score,['tmp.txt',self.scores2,self.joueurs2]))

        tp7.sauver_score('tmp.txt',self.scores3,self.joueurs3)
        fic=open('tmp.txt')
        cont=fic.read()
        fic.close()
        self.assertEqual(cont,self.cont_fic3,
                         self.message(tp7.sauver_score,['tmp.txt',self.scores3,self.joueurs3]))

        tp7.sauver_score('tmp.txt',self.scores4,self.joueurs4)
        fic=open('tmp.txt')
        cont=fic.read()
        fic.close()
        self.assertEqual(cont,self.cont_fic4,
                         self.message(tp7.sauver_score,['tmp.txt',self.scores4,self.joueurs4]))
        
        
    # exercice 12
    def test_restaurer_score(self):
        fic=open('tmp.txt','w')
        fic.write(self.cont_fic1)
        fic.close()
        scores=[]
        joueurs=[]
        tp7.restaurer_score('tmp.txt',scores,joueurs)
        self.assertEqual((scores,joueurs),(self.scores1,self.joueurs1),
                         self.message(tp7.restaurer_score,['fichier contenant:\n'+self.cont_fic1]))
        
        fic=open('tmp.txt','w')
        fic.write(self.cont_fic2)
        fic.close()
        scores=[]
        joueurs=[]
        tp7.restaurer_score('tmp.txt',scores,joueurs)
        self.assertEqual((scores,joueurs),(self.scores2,self.joueurs2),
                         self.message(tp7.restaurer_score,['fichier contenant:\n'+self.cont_fic2]))
        
        fic=open('tmp.txt','w')
        fic.write(self.cont_fic3)
        fic.close()
        scores=[]
        joueurs=[]
        tp7.restaurer_score('tmp.txt',scores,joueurs)
        self.assertEqual((scores,joueurs),(self.scores3,self.joueurs3),
                         self.message(tp7.restaurer_score,['fichier contenant:\n'+self.cont_fic3]))
        
        fic=open('tmp.txt','w')
        fic.write(self.cont_fic4)
        fic.close()
        scores=[]
        joueurs=[]
        tp7.restaurer_score('tmp.txt',scores,joueurs)
        self.assertEqual((scores,joueurs),(self.scores4,self.joueurs4),
                         self.message(tp7.restaurer_score,['fichier contenant:\n'+self.cont_fic4]))

        fic=open('tmp.txt','w')
        fic.write('\n')
        fic.close()
        scores=[]
        joueurs=[]
        tp7.restaurer_score('tmp.txt',scores,joueurs)
        self.assertEqual((scores,joueurs),([],[]),
                         self.message(tp7.restaurer_score,['fichier contenant rien']))
        
    # exercice 13
    def test_scores_HTML(self):
        tp7.scores_HTML('tmp.txt',self.scores1,self.joueurs1)
        fic=open('tmp.txt')
        cont=fic.read()
        fic.close()
        self.assertEqual(cont,self.cont_html1,
                         self.message(tp7.scores_HTML,['tmp.txt',self.scores1,self.joueurs1]))


if __name__ == '__main__':
    unittest.main()
