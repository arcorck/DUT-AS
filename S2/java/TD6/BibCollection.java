import java.util.Collections; 
import java.util.List; 
import java.util.ArrayList;

public class BibCollection{
    public static void inverse (List<Integer> l){
        int deb = 0;
        int fin = l.size()-1;
        while (deb < fin){
            Collections.swap(l, deb, fin);
            deb++;
            fin--;
        }
    }

    public static int nb_occ_premier_element (List<Integer> l){
        return (Collections.frequency(l, l.get(0)));
    }

    public static int plus_frequent (List<Integer> l){
        int pf = l.get(0);
        for (int i = 0; i < l.size(); i++){
            if (Collections.frequency(l, l.get(i)) > pf){
                pf = l.get(i);
            }
        }
        return pf;
    }

    public static void main (String[]args){
        List<Integer> l = new ArrayList<>();
        l.add(1);
        l.add(2);
        l.add(1);
        l.add(3);
        l.add(4);
        l.add(1);
        l.add(5);
        l.add(1);
        l.add(4);
        l.add(4);
        l.add(4);
        l.add(4);
        l.add(4);
        l.add(4);
        l.add(4);
        l.add(4);
        System.out.println(l);
        inverse(l);
        System.out.println(l);
        System.out.println("\n" + nb_occ_premier_element(l));
        System.out.println("\n" + plus_frequent(l));
    }
}