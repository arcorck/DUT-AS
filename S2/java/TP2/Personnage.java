public class Personnage {
   private String nom;
   private int pointsVie;

   public Personnage (String nom) {// 5 points de vie par défaut
       this.nom = nom;
       this.pointsVie = 5;
   } 

   public Personnage (String nom, int points) {
       this.nom = nom;
       this.pointsVie = points;
   }

   public String getNom() {
       return this.nom;
   }

   public int getPoints() {
       return this.pointsVie;
   }

   public String toString() {
       return "Le personnage de " + this.nom + " a " + this.pointsVie + " points de vie";
   }
}