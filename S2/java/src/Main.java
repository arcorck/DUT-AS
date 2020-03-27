import java.util.List;
import java.util.ArrayList;

public class Main {
    private List<Carte> main;

    public Main(){
        this.main = new ArrayList<>();
    }

    public List<Carte> getMesCartes(){
        return this.main;
    }

    public void add (Carte c){
        this.main.add(c);
    }

    public int nombreDeCartes(){
        return this.main.size();
    }

    @Override
    public String toString() {
        return "Main{" +
                "main=" + main +
                '}';
    }

    public void triParType(){

    }

    public void triParValeur(){

    }
}
