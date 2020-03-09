public class CompteBancaireExec {
    public static void main(String [] args){
        CompteBancaire comp = new CompteBancaire ("Paul Maccartney");
        comp.deposer(50);
        comp.retirer(20);
        CompteBancaire comp2 = new CompteBancaire ("John Lennon", 100);
        comp2.retirer(40);
        System.out.println(comp.toString());
        System.out.println(comp2.toString());
    }
}