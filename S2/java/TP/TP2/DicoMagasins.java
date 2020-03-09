import java.util.Map ;
import java.util.HashMap;
import java.util.ArrayList;

public class DicoMagasins {
    private Map<String, OuvertLundiDimanche> magasins;

    public DicoMagasins() {
        this.magasins = new HashMap();
    }

    public void ajoute(String nom, boolean lundi, boolean dimanche) {
        this.magasins.put(nom, new OuvertLundiDimanche(lundi, dimanche));
    }

    public String toString() {
        return "Les magasins : "+this.magasins;
    }

    ArrayList<String> ouvertsLeLundi() {
        ArrayList<String> res = new ArrayList<String>();
        for(String m : this.magasins.keySet()){
            if(this.magasins.get(m).getLundi()){
                res.add(m);
            }
        }
        return res;
    }
}