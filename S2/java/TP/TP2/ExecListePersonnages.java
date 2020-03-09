public class ExecListePersonnages {

    public static void main (String[]args){
        ListePersonnages liste = new ListePersonnages();
        liste.ajoute(new Personnage("Thomas", 9));
        liste.ajoute(new Personnage("Francis", 8)); 
        liste.ajoute(new Personnage("Jean"));
        System.out.println(liste);
        System.out.println(liste.maxPointsVie());
    }
}