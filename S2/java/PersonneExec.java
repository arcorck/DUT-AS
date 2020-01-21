public class PersonneExec {
    public static void main (String[]args){
        Personne pers = new Personne("Dupont", "Arthur", 13, 4, 1996, 1.56);
        System.out.println(pers.toString());
        pers.setAnneeNaissance(1997);
        System.out.println(pers.signeAstrologique());
    }
} 