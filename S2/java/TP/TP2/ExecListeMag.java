public class ExecListeMag{
    
    public static void main (String[]args){
        ListeMagasins liste = new ListeMagasins();
        liste.ajoute(new Magasin("Hollister", true, true));
        liste.ajoute(new Magasin("Apple", true, false));
        liste.ajoute(new Magasin("Boulangerie", false, true));
        System.out.println(liste);
        System.out.println("Les magasins ouverts le dimanche sont : " + liste.ouvertsLeLundi());
    }
}