import java.util.ArrayList;

public class ExecutableDichotomie{
    public static void main(String[] args){
        ArrayList<Integer> liste = new ArrayList<Integer>();
        System.out.println(LibEntiers.recherche(liste,0));// false
        for(int i=0;i<100000;i++)
            liste.add(2*i);
        System.out.println(LibEntiers.recherche(liste,100));// true
        System.out.println(LibEntiers.recherche(liste,0));// true
        System.out.println(LibEntiers.recherche(liste,3));// false
        System.out.println(LibEntiers.recherche(liste,-3));// false
        System.out.println(LibEntiers.recherche(liste,400000));// false
    }
}