#include <iostream>
#include <string>
using namespace std;

/*
 * On vous propose ici d'implémenter une hierarchie de classes en C++ qui vont nous permettre de gérer des plantes.
 * 
 * Chaque plante a un nom, cela peut-être :
 * un arbre qui disposera d'une hauteur, 
 * un fruitier qui en plus d'une hauteur disposera aussi du nom du fruit qu'il produit, 
 * une fleur avec une couleur,
 * un légume avec féculent oui/non et un prix au kilo.
 * 
 * 1. Proposez un diagramme de classes.
 * 2. Rappelez ce qu'est la forme coplien pour une classe?
 * 3. Pensez-vous avoir besoin de mettre sous forme coplien certaines classes de votre hierarchie?
 * 4. Implémentatez les différentes classes avec les méthodes classiques.
 * 5. Ajoutez la méthode "ostream & affiche(ostream &s) const" à chacune de vos classes.
 * 6. Ajoutez dans vos constructeurs l'affichage d'un message "constructeur plante" ...
 * 7. Ajoutez des destructeurs avec juste un affichage "destructeur plante" ...
 * 8. Testez votre implémentation dans un programme principale en manipulant au moins une instance de chaque classe.
 * 
 * Soit la déclaration suivante : Plante * tab[6]; qui sera un tableau de 6 cases.
 * 9. Quel est le type des éléments contenus dans chaque case.
 * 10. Quels types d'instance peuvent réellement être mises dans tab?
 * 11. Remplissez la variable tab en utilisant de l'allocation dynamique.
.* 12. Faites affichez le contenu de votre tableau.
 * 13. Que constatez-vous?
 * 
 * En attendant de voir comment faire de la compilation séparée en C++ vous mettrez toutes vos classes dans un même 
 * fichier Plante.cpp
 */
