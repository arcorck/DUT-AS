# RENDU DE LA FEUILLE TD 6 Exercice 1

def reponse(expression,valeurAttendue):
    try:
        assert(type(expression)==str)
    except:
        print("Attention!!! l'expression doit être fournie sous la forme d'une chaine de caractères")
        print("Le test n'a pas pu être effectué")
        return
    
    print('exp:',expression,'valeur:',valeurAttendue)
    try:
        assert(eval(expression)==valeurAttendue)
        print("La reponse est correcte")
    except  AssertionError:
        print("Le test a échoué car la valeur et l'expression ne sont pas égaux")
    except:
        print("Le test a échoué car l'expression est incorrecte")

# ------------------------------------------------------------------
# EXERCICE 1
# Remplacez les None par le résultat attendu 
# Remplacez les chaines vides par l'expression qui permet d'obtenir le résultat escompté
# Remplacez l'instruction pass par l'instruction attendue

#Partie A
print("Partie A")
art=[(152,"Chaussures",37.5),(145,"Veste",87.2),(147,"T-shirt",25.3),(165,"Bonnet",11.0)]
#Réponse 1
print("- point 1")
reponse("art[1]",(145,"Veste",87.2))
reponse("art[0][1]","Chaussures")
reponse("art[0][1][0]",'C')
reponse("art[3][2]",11.0)
#Réponse 2
print("- point 2")
reponse("art[2]",(147,"T-shirt",25.3))
#Réponse 3
print("- point 3")
reponse("art[1][2]",87.2)
#Réponse 4
print("- point 4")
reponse("art[3][1]","Bonnet")
#Réponse 5
print("- point 5")
#Remplacez pass par  l'instruction demandée
print("Test de l'ajout d'une chemise en fin de liste")
art.append((138,"Chemise", 50.26))
try:
    assert(art[len(art)-1][0]==256 and art[len(art)-1][1]=='Chemise' and art[len(art)-1][2]==51.1)
    print("La réponse est correcte")
except:
    print("Le test a échoué")

#Partie B
print("Partie B")
commande=(174,"Dupont",[(145,1),(147,5),(152,1)])
#Réponse 1
print("- point 1")
# Complétez les print
print("commande[0] représente le numero de commande : 174")
print("commande[1] représente le nom du client : Dupont")
print("commande[2] représente la liste contenant des couples de reference d'articles et de quantités")

#Réponse 2
print("- point 2")
reponse("commande[2][0]", (145,1))
reponse("commande[2][0][0]", 145)
reponse("commande[2][0][1]", 1)

#Réponse 3
print("- point 3")
reponse("commande[2][1][0]",147)
reponse("commande[2][2][1]",1)
