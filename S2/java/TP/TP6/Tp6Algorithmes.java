import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Collections;

public class Tp6Algorithmes{

    public static void main (String[]args){
        List<Integer> l = new ArrayList<>();
        l.add(5);
        l.add(8);
        l.add(-4);
        l.add(1);
        System.out.println(l + "\n");
        Collections.sort(l);
        System.out.print("TRI CROISSANT DE LA LISTE : ");
        System.out.println(l + "\n");
        Comparator<Integer> c = new CompEntier();
        Collections.sort(l, c);
        System.out.print("TRI DECROISSANT DE LA LISTE : ");
        System.out.println(l + "\n");
    }
}