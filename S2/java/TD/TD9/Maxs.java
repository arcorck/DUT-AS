import java.util.List;
import java.util.NoSuchElementException;
import java.util.ArrayList;
import java.util.Collections;

public class Maxs {

    public static int max (List<Integer> l) throws NoSuchElementException{
        if (l.isEmpty()){
            throw new NoSuchElementException();
        }else{
            return Collections.max(l);
        }
    }

    public static int produitMax (List<List<Integer>> listes){
        int prod = 1;
        for (List<Integer> l : listes){
            try{
                prod *= max(l);
            }catch(NoSuchElementException e){
                System.out.println("Liste Vide !");
            }
        }
        return prod;
    } 

    public static int sommeMax (List<List<Integer>> listes){
        int somme = 0;
        for (List<Integer> l : listes){
            try{
                somme += max(l);
            }catch(NoSuchElementException e){
                System.out.println("Liste Vide !");
            }
        }
        return somme;
    } 

    public static void main(String[] args) {
        List<Integer> a = new ArrayList<>();
        List<Integer> b = new ArrayList<>();
        List<Integer> c = new ArrayList<>();
        List<Integer> d = new ArrayList<>();
        List<Integer> e = new ArrayList<>();
        for (int i = 0; i < 5; i++){
            b.add((int)(Math.random() * ((100 - 0) + 1)));
            c.add((int)(Math.random() * ((100 - 0) + 1)));
            d.add((int)(Math.random() * ((100 - 0) + 1)));
        }
        List<List<Integer>> leslistes = new ArrayList<>();
        leslistes.add(a);
        leslistes.add(b);
        leslistes.add(c);
        leslistes.add(d);
        leslistes.add(e);
        System.out.println(leslistes);
        System.out.println("ProdMax : " + produitMax(leslistes));
        System.out.println("SommeMax : " + sommeMax(leslistes));
    }
}