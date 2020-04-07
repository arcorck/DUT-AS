import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class RencontreStarWars {
    @Override
    public String toString() {
        return "RencontreStarWars{" +
                "mesPersonnages=" + mesPersonnages +
                '}';
    }

    private List<Personnage> mesPersonnages;

    public RencontreStarWars (){
        this.mesPersonnages = new ArrayList<>();
    }

    public List<Personnage> getMesPersonnages (){
        return this.mesPersonnages;
    }

    public void add (Personnage p){
        this.mesPersonnages.add(p);
    }

    public int nombreDePersonnages(){
        return this.mesPersonnages.size();
    }

    public void trierParTaille(){
        Collections.sort(this.mesPersonnages, new CompareTaille());
    }

    public void trierParRace(){
        Collections.sort(this.mesPersonnages, new CompareRace());
    }
}
