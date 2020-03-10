import java.util.Comparator;
import java.util.List;
import java.util.ArrayList;

public class Tp6Comparator{

    public static void methode(Comparator<String> c){
        if(c.compare("Bonjour","toto") > 0){
            System.out.println("Oh Oh");
        }else{
            System.out.println("Ah Ah");
        }
    }

    public static boolean premier_plusgrand (Comparator<String> c, List<String> s){
    String premier = s.get(0);
    for (int i = 1; i < s.size(); i++){
        if (c.compare(premier, s.get(i)) <= 0){
            return false;
        }
    }
    return true;
}

    public static void main (String[]args){
        //Question 1
        Comparator<String> c = new CompChaine();
        System.out.println(c.compare("toto","tut"));
        //Question 2
        methode(c);
        //Question 3
        Comparator<String> c2 = new CompChaine2();
        methode(c2);
        //Question 4
        List<String> tab = new ArrayList<>();
        tab.add("bonjour");
        tab.add("tout");
        tab.add("le");
        tab.add("monde");
        System.out.println(tab);
        System.out.println(premier_plusgrand(c, tab));
        tab.add("du");
        tab.add("kazakstan");
        System.out.println(tab);
        System.out.println(premier_plusgrand(c, tab));
        //Question 5 
        System.out.println(premier_plusgrand(c2, tab));
        tab.add(0,"a");
        System.out.println(tab);
        System.out.println(premier_plusgrand(c2, tab));
    }
}