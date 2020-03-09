import java.util.*;

public class Test {

    public static ArrayList<Integer> elementsEnPlusieursExemplaires(ArrayList<Integer> a){
        ArrayList<Integer> res = new ArrayList<>();
        ArrayList<Integer> b = (ArrayList<Integer>) a.clone();
        Collections.sort(b);
        for (int i = 0; i < b.size() - 1; i ++){
            if(b.get(i) == b.get(i+1)){
                if (! res.contains(b.get(i))){
                    res.add(b.get(i));
                }
            }
        }
        return res;
    }

    public static int mediane (ArrayList<Integer> l){
        ArrayList<Integer> a = (ArrayList<Integer>) l.clone();
        Collections.sort(a);
        System.out.println("liste triée : " + a);
        return (a.get(a.size()/2));
    }

    public static void main (String[]args){
        ArrayList<Integer> liste = new ArrayList<>();
        ArrayList<Integer> liste1 = new ArrayList<>();
        liste.add(1);
        liste.add(6);
        liste.add(2);
        liste.add(-4);
        liste.add(1);
        liste.add(9);
        liste.add(6);
        System.out.println(liste);
        liste1.add(1);
        liste1.add(6);
        liste1.add(2);
        liste1.add(-4);
        liste1.add(1);
        liste1.add(9);
        System.out.println(liste1);
        System.out.println(Test.mediane(liste));
        System.out.println(Test.mediane(liste1));
        System.out.println(Test.elementsEnPlusieursExemplaires(liste));
        System.out.println(Test.elementsEnPlusieursExemplaires(liste1));
    }
}