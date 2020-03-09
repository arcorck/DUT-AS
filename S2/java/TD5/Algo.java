import java.util.List;
import java.util.ArrayList;

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
    }
}