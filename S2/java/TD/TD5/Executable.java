import java.util.*;

class Executable{
    public static void main (String[]args){
        Integer x = 3;
        Integer y = new Integer(3);
        System.out.println(x == y);
        System.out.println(x.equals(y));
        System.out.println(x.toString());
        System.out.println(x);
        System.out.println(x.hashCode() == y.hashCode());

        ArrayList<Object> tableau = new ArrayList<Object>();
        ArrayList<Object> tab2 = new ArrayList<Object>();
        tableau.add(new Integer(5));
        tableau.add(new Double(5.));
        tableau.add(new Boolean(true));
        tableau.add(tab2);
        System.out.println(tab2);

        tableau = new ArrayList<Object>();
        tab2 = new ArrayList<Object>();
        tableau.add(new Integer(4));
        tab2.add(new Integer(4));
        System.out.println(tab2 == tableau);
        System.out.println(tab2.equals(tableau));

        System.out.println("\nPassons au projectile");
        Projectile p1;
        Projectile p2 = new Projectile(10,10);
        Projectile p3 = new Projectile(10,10);
        //System.out.println(p1);
        System.out.println(p2);
        System.out.println(p2 == p3);
        System.out.println(p2.equals(p3));
    }
}