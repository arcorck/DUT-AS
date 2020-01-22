public class VilleExec {
    public static void main (String[]args){
        Ville v = new Ville("Tours", "France", "métropole", 78);
        System.out.println(v.toString());
        v.setNbHab(300075);
        System.out.println(v.toString());
    }
}