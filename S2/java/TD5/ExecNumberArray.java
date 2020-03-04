import java.util.*;
import java.lang.*;

class ExecNumberArray{
    public static void main (String[]args){
        ArrayList<Number> t = new ArrayList<Number>();
        t.add(5);
        t.add(6.);
        t.add(7.f);
        int somme = 0;
        for (int i = 0; i < t.size(); i++){
            somme += (Integer)t.get(i);
        }
        System.out.println(somme);
    }
}