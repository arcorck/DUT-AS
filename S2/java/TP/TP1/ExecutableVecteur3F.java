public class ExecutableVecteur3F {
   public static void main(String [] args) {
       Vecteur3F v3f = new Vecteur3F(4.5, 7.325, -6.875);
       System.out.println(v3f.toString());
       Vecteur3F v3ff = v3f;
       v3ff.modif(5.55, 1);
       System.out.println(v3ff.toString());
       System.out.println(v3f.toString()); //On obtient le même résultat pour les deux derniers affichages : normal car v3ff prend l'adresse de v3f donc quand on modifie v3ff on modifie v3f, ce sont deux pointeurs vers la meme adresse
   }
}