public class ExecutableMagasins{

    public static void main (String[]args){
        ListeMagasins l = new ListeMagasins();
        l.ajoute(new Magasin("Fleurus", true, false));
        l.ajoute(new Magasin("BeauMagasin", true, true));
        l.ajoute(new Magasin("Venir", false, false));
        l.ajoute(new Magasin("Magnifique", false, true));
        System.out.println(l);
        System.out.println(l.ouvertsLeLundi());
    }
}