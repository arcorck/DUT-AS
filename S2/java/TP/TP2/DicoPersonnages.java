import java.util.Map;
import java.util.HashMap;

public class DicoPersonnages {
 private Map<String, Integer> personnages;
   public DicoPersonnages() {
       this.personnages = new HashMap();
   }

   public void ajoute(String nom, Integer points) {
       this.personnages.put(nom, points);
   }

   public void ajoute(String nom) {
       this.personnages.put(nom, 5);
   }

   public String toString() {
       return "Mes personnages : "+this.personnages;
   }

   public String maxPointsVie() {
        Integer pdv = 0;
        String nom = "";
        for (Map.Entry mapentry : this.personnages.entrySet()) {
            if(pdv <= (Integer)mapentry.getValue()){
                pdv = (Integer)mapentry.getValue();
                nom = (String)mapentry.getKey();
            }
        }
        return nom;
   }

}