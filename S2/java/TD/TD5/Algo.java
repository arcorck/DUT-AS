import java.util.List;
import java.util.ArrayList;
import java.lang.Math;

public class Algo{
    public static boolean encommun (List a, List b){
        for (int i = 0; i < a.size(); i++){
            for (int j = 0; j < b.size(); j++){
                if (a.get(i).equals(b.get(j))){
                    return true;
                }
            }
        }
        return false;
    }

    public static int pluspres (List<Integer> a, double b){
        double min = Math.abs(a.get(0) - b);
        int pp = a.get(0);
        for (int d : a){
            if (Math.abs(d-b) < min){
                min = Math.abs(d-b);
                pp = d;
            }
        }
        return pp;
    }

    public static int ecart (List<Integer> a){
        if (a.size() > 1){
            int ecart_min = Math.abs(a.get(1) - a.get(0)); 
            for (int i = 0; i < a.size(); i++){
                for (int j = 0; j < a.size(); j++){
                    if (Math.abs(a.get(i) - a.get(j)) < ecart_min && a.get(i) != a.get(j)){                        
                        ecart_min = Math.abs(a.get(i) - a.get(j));
                    }
                }
            }
            return ecart_min;
        }else{
            return -1;
        }
    }


    public static void main (String[]args){
        List<Integer> a = new ArrayList<>();
        List<Integer> b = new ArrayList<>();
        for (int i = 0; i<10; i++){
            a.add(i);
        }
        for (int i = 19; i<20; i++){
            b.add(i);
        }
        System.out.println("a : " + a);
        System.out.println("b : " + b);
        System.out.println(encommun(a,b));
        List<Integer> c = new ArrayList<>();
        c.add(12);
        c.add(3);
        c.add(4);
        c.add(9);
        System.out.println(pluspres(c, 1.5));
        System.out.println(ecart(a));
        System.out.println(ecart(b));
        System.out.println(ecart(c));
        List<Integer> d = new ArrayList<>();
        d.add(12);
        d.add(3);
        d.add(18);
        d.add(9);
        System.out.println(ecart(d));
    }
}