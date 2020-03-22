import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;

public class ListePers{
    private List<Personne> lp;

    public ListePers(){
        lp = new ArrayList<>();
    }

    public String toString(){
        String res = "";
        for (Personne p : this.lp){
            res += p.toString();
        }
        return res;
    }

    public void add (Personne p){
        this.lp.add(p);
    }

    public Personne plusjeune(List<Personne> liste){
        Personne pj = liste.get(0);
        Comparator<Integer> comp = new CompareAge();
        for (Personne p : liste){
            if (comp.compare(p.getAge(), pj.getAge()) < 0){
                pj = p;
            }
        }
        return pj;
    }

    public void tri (){
        List<Personne> res = new ArrayList<>();
        List<Personne> copie = new ArrayList<>(this.lp);
        while (! copie.isEmpty()){
            res.add(plusjeune(copie));
            copie.remove(plusjeune(copie));
        }
        this.lp = res;
    }

    public static void main(String[] args) {
        ListePers l = new ListePers();
        l.add(new Personne("Jean", 56));
        l.add(new Personne("Pierre", 48));
        l.add(new Personne("Paul", 38));
        l.add(new Personne("Jacques", 87));
        l.add(new Personne());
        System.out.println(l.toString());
        l.tri();
        System.out.println("Tri de la liste :");
        System.out.println(l.toString());
    }
}