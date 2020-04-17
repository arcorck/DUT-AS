import java.util.*;

public class Ensemble implements Contenant<Integer>{

    private Set<Integer> lesentiers;

    public Ensemble() {
        this.lesentiers = new TreeSet<Integer>();
    }

    public void add (Integer a){
        this.lesentiers.add(a);
    }

    public Set<Integer> getLesentiers() {
        return this.lesentiers;
    }

    @Override
    public String toString() {
        String res = "";
        for(Integer i : this.lesentiers){
            res += i.toString() + "; ";
        }
        return res;
    }

    @Override
    public boolean contient(Integer obj) {
        return lesentiers.contains(obj);
    }
}
