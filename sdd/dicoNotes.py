dicoNotes={'Julie':{'Maths':12,'SDD':15, 'Droit':8, 'Web':13, 'BD':7},
           'Tom':{'Droit':12, 'Web':12, 'BD':13, 'SDD':5, 'Anglais':17},
           'Alice':{'Anglais':12, 'Web':12, 'Maths':13, 'SDD':13, 'Droit':17, 'BD':17}}
           
# Dans les tris qui suivent, l'absence de note dans une matière pourra 
# être considérée comme un 0 si besoin


# 1- Ecrire une fonction qui retourne la liste des élèves en ordre alphabétique
def tri_eleves_alpha (dico) :
    return sorted(dicoNotes)

print(tri_eleves_alpha(dicoNotes))


# 2- Ecrire une fonction qui retourne la liste des élèves triée par moyenne croissante
def tri_eleves_moyenne (dico):
    def moyenne_eleve (eleve):
        somme = 0
        cpt = 0
        for (_,note) in dico[eleve].items():
            somme += note
            cpt += 1
        return somme/cpt
    return sorted(dico, key=moyenne_eleve)

print(tri_eleves_moyenne(dicoNotes))  


# 3- Ecrire une fonction qui retourne le nom d'une personne qui a obtenu 
#    la plus grande moyenne dans la matiere
def meilleure_note (dico, matiere):
    def moyenne_matiere (eleve):
        return dico[eleve].get(matiere, 0)
    return max(dico, key=moyenne_matiere)

print(meilleure_note(dicoNotes, 'BD'))
print(meilleure_note(dicoNotes, 'Web'))



    
