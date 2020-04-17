import java.util.ArrayList;

public class Exec {

    public static void main(String[] args) {
        Couple c = new Couple(0,1);
        Ensemble e = new Ensemble();
        e.add(0);
        e.add(1);
        e.add(2);
        e.add(3);
        e.add(4);
        Couple d = new Couple(0,2);
        System.out.println("Couple 1 : " + c.toString());
        System.out.println("Ensemble : " + e.toString());
        System.out.println("Couple 2 : " + d.toString());
        ArrayList<Contenant<Integer>> liste = new ArrayList<>();
        liste.add(c);
        liste.add(e);
        liste.add(d);
        GestionContenants g = new GestionContenants(liste);
        System.out.println(g.contiennentTous(liste, 0));
        System.out.println(g.contiennentTous(liste, 1));
    }
}
