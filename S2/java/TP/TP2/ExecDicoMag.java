public class ExecDicoMag{
    
    public static void main (String[]args){
        DicoMagasins dico = new DicoMagasins();
        dico.ajoute("Hollister", true, true);
        dico.ajoute("Apple",true, false);
        dico.ajoute("Boulangerie", false, true);
        System.out.println(dico);
        System.out.println("Les magasins ouverts le dimanche sont : " + dico.ouvertsLeLundi());
    }
}