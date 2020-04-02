import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class BibProdMax {
    public static int produitMax(List<List<Integer>> liste) throws ListeVideException{ // minimum peut lever une exception (quand la lite est vide)
        int prod = 1;
        for (List<Integer> l : liste){
            if (l.size() == 0){
                throw new ListeVideException();
            }else {
                prod = prod * Collections.max(l);
            }
        }
        return prod;
    }
}

public class ExecutableProduitListe{ 
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

        try{
            System.out.println(BibProdMax.produitMax(e));
            System.out.println(BibProdMax.produitMax(d));
        }catch(ListeVideException m){
            System.out.println("erreur de type : " + m);
        }
    }
}