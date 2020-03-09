import java.util.List;
import java.util.ArrayList;

public class Main{
    private List<Carte> main;

    public Main (){
        this.main = new ArrayList<>();
    }

    public void add (Carte c){
        this.main.add(c);
    }

    public Carte getCarteSelectionnee() {
        if (this.main.isEmpty()){
            return null;
        }else{
            return this.main.get(0);
        }
    }

    public ArrayList<Carte> getMesCartes(){
        return this.main;
    }

    
}