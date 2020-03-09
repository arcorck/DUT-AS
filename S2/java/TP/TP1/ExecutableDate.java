public class ExecutableDate{
    public static void main (String[]args){
        Date d = new Date(15 , 1, 1997);
        Date d1 = new Date(15,2,2020);
        Date non_valide = new Date(31,3,2020);
        Date non_valide2 = new Date(5,20,2020);
        System.out.println(d);
        System.out.println(d1);
        System.out.println(d.getJour());
        System.out.println(d1.getMois());
        System.out.println(non_valide.getAnnee());
        System.out.println(d.bissextile());
        System.out.println(d1.bissextile());
        System.out.println(d.valide());
        System.out.println(d1.valide());
        System.out.println(non_valide + " valide : " + non_valide.valide());
        System.out.println(non_valide2.valide());
        System.out.println(d.nbJourMois());
        System.out.println(d1.nbJourMois());
        System.out.println(non_valide.nbJourMois());
        System.out.println(non_valide2.nbJourMois());
        System.out.println(d.lendemain());
        System.out.println(non_valide.lendemain());
    }
}