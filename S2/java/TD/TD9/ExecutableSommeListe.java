import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class BibSommeMax {
    public static int sommeMax(List<List<Integer>> liste) { // minimum peut lever une exception (quand la lite est vide)
        int somme = 0;
        for (List<Integer> l : liste){
            try{
                somme += Collections.max(l);
            }catch(NullPointerException e){
                somme += 0;
            }
        }
        return somme;
    }
}

public class ExecutableSommeListe{ 
    public static void main(String[] args) {
        List<Integer> a = new ArrayList<>();
        List<Integer> b = new ArrayList<>();
        List<Integer> c = new ArrayList<>();
        List<List<Integer>> d = new ArrayList<>();
        List<List<Integer>> e = new ArrayList<>();
        b = Arrays.asList(2, 8, 3, -6, 90);
        a = Arrays.asList(2, 8, 3, -6, 90);
        d.add(a);
        d.add(b);
        d.add(c);
        e.add(a);
        e.add(b);


        System.out.println(BibSommeMax.sommeMax(e));
        System.out.println(BibSommeMax.sommeMax(d));
    }
}