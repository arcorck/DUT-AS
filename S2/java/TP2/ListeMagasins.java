import java.util.ArrayList ;

public class ListeMagasins {
    private ArrayList<Magasin> magasins;

    public ListeMagasins() {
        this.magasins = new ArrayList<Magasin>();
    }

    void ajoute(Magasin mag) {
        this.magasins.add(mag);
    }

    public String toString() {
        String res = "";
        for (int i = 0; i < this.magasins.size() ; i++){
            res += (this.magasins.get(i).toString());
            res += ("\n");
        }
        return res;
    }

    ArrayList<String> ouvertsLeLundi() {
        ArrayList<String> res = new ArrayList<String>();
        for (int i = 0; i < this.magasins.size() ; i++){
            if (this.magasins.get(i).ouvertlundi()){
                res.add(this.magasins.get(i).getnom());
            }
        }
        return res;
    }
}