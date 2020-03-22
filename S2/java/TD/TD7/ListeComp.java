import java.util.*;
import java.util.Collections;

public class ListeComp{
    List<Complexe> lc;

    public ListeComp(){
       this.lc = new ArrayList<>();
    }

    public void add (Complexe c){
        this.lc.add(c);
    }

    public Complexe pluspetitreel(List<Complexe> liste){
        Complexe ppr = liste.get(0);
        Comparator<Complexe> comp = new CompareCompReel();
        for (Complexe c : liste){
            if (comp.compare(c, ppr) < 0){
                ppr = c;
            }
        }
        return ppr;
    }

    public void tri_reel (){
        List<Complexe> res = new ArrayList<>();
        List<Complexe> copie = new ArrayList<>(this.lc);
        while (! copie.isEmpty()){
            res.add(pluspetitreel(copie));
            copie.remove(pluspetitreel(copie));
        }
        this.lc = res;
    }

    public Complexe pluspetitnorme(List<Complexe> liste){
        Complexe ppr = liste.get(0);
        Comparator<Complexe> comp = new CompareCompNorme();
        for (Complexe c : liste){
            if (comp.compare(c, ppr) < 0){
                ppr = c;
            }
        }
        return ppr;
    }

    public void tri_norme (){
        List<Complexe> res = new ArrayList<>();
        List<Complexe> copie = new ArrayList<>(this.lc);
        while (! copie.isEmpty()){
            res.add(pluspetitreel(copie));
            copie.remove(pluspetitreel(copie));
        }
        this.lc = res;
    }

    public String toString(){
        String res = "";
        for (Complexe c : this.lc){
            res += c.toString();
        }
        return res;
    }

    public static void main(String[] args) {
        ListeComp l = new ListeComp();
        Comparator<Complexe> comp = new CompareCompNorme();
        l.add(new Complexe(56.3, -2.5));
        l.add(new Complexe(-67.9, 0.0));
        l.add(new Complexe(-21.6, -38.0));
        l.add(new Complexe(98.09, 87.543));
        l.add(new Complexe(-92.87, 65.67));
        System.out.println(l.toString());
        l.tri_reel();
        System.out.println("Tri de la liste par les reels :");
        System.out.println(l.toString());
        l.tri_norme();
        System.out.println("Tri de la liste par les normes :");
        System.out.println(l.toString());
        System.out.println("Max par collection : ");
        System.out.println(Collections.max(l, comp));
    }
}