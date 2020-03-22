import java.util.ArrayList;
public class ExecutableDichotomieDecroissant{
    public static void main(String[] args){
        ArrayList<Integer> liste =new ArrayList<Integer>();
        System.out.println(LibEntiers.rechercheDecroissant(liste,0));// false
        for(int i=100000;i>=0;i--)
            liste.add(2*i);
        System.out.println(LibEntiers.rechercheDecroissant(liste,100));// true
        System.out.println(LibEntiers.rechercheDecroissant(liste,0));// true
        System.out.println(LibEntiers.rechercheDecroissant(liste,3));// false
        System.out.println(LibEntiers.rechercheDecroissant(liste,-3));// false
        System.out.println(LibEntiers.rechercheDecroissant(liste,400000));// false
    }
}
