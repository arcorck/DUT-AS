class Score(object):

    def __init__(self,nomdujoueur,nb_points):
        """
        constructeur
        """
        self.nom=nomdujoueur
        self.points=nb_points

    def getNom(self):
        return self.nom

    def getPoints(self):
        return self.points


class Classement(object):
    def __init__(self, capacite_du_classement):
        """
        constructeur
        """
        self.nb_place=capacite_du_classement
        self.classement=[]
    
    def getNbPlace(self) :
        return self.nb_place

    def getScore(self, i) :
        if self.classement != [] : 
            if len(self.classement) > i :
                return self.classement[i]
            else : 
                return None
        else : 
            return None
    
    def ajouter(self, score) :
        if self.classement == [] : 
            self.classement = [score]
        else : 
            if len(self.classement) < self.nb_place :
                for indice in range(len(self.classement)):
                    if score.points > self.classement[indice].points : 
                        self.classement.pop(len(self.classement)-1)
                        self.classement.insert(indice, score)

    def afficher (self) : 
        print(self.classement)

score1 = Score("Fab", 1235)
print(score1.nom, score1.points)
score2 = Score("Tintin", 1254)
print(score2.nom, score2.points)
score3 = Score("Milou", 1252)
print(score3.nom, score3.points)
classemen = Classement(4)
classemen.afficher
classemen.ajouter(score1)
classemen.afficher
classemen.ajouter(score2)
classemen.afficher
classemen.ajouter(score3)
classemen.afficher

