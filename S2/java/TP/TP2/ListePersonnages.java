import java.util.ArrayList;
import java.util.List;

public class ListePersonnages {
   private List<Personnage> personnages;

    public ListePersonnages() {
        this.personnages = new ArrayList();
    }

    public void ajoute(Personnage personne) {
        this.personnages.add(personne);
    }

    public String toString() {
        return "Liste de mes personnages : " + this.personnages;
    }
   
    //renvoie le nom du personnage qui a le plus grand nombre de points de vie
    public String maxPointsVie() {
        int pdv = 0;
        String nom = "";
        for (Personnage p : this.personnages){
            if (pdv <= p.getPoints()){
                pdv = p.getPoints();
                nom = p.getNom();
            } 
        }
        return nom;
    }
}