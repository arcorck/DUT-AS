import java.util.List;
import java.util.ArrayList;

public class Executable{
    public static void main(String [] args){
        List<Integer> l1 = new ArrayList<>();
        l1.add(1);
        l1.add(3);
        l1.add(6);
        l1.add(7);
        l1.add(9);
        l1.add(10);
        List<Integer> l2 = new ArrayList<>();
        l2.add(3);
        l2.add(5);
        l2.add(6);
        l2.add(8);
        l2.add(11);
        
        System.out.println(BibCollections.intersection(l1,l2));
        
        l1 = new ArrayList<>();
        Integer elt = 0;
        while(elt<=200000){
            l1.add(elt);
            elt+=2;
        }
        l2 = new ArrayList<>();
        elt = 1;
        while(elt<=200001){
            l2.add(elt);
            elt+=2;
        }
        
        System.out.println(BibCollections.intersection(l1,l2));
        l2 = new ArrayList<>();
        elt = 0;
        while(elt<=1000000){
            l2.add(elt);
            elt+=2;
        }  
        System.out.println(BibCollections.intersection(l1,l2).size());



      l1 = new ArrayList<>();
      l1.add(1);
      l1.add(4);
      l1.add(3);
      l1.add(7);
      l1.add(1);
      l1.add(4);
      l1.add(3);
      l1.add(3);
      l1.add(9);
      l1.add(3);
      l1.add(5);
      l1.add(3);
      System.out.println(BibCollections.elementMajoritaire(l1));
      }
}