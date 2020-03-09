public class ExecDicoPersonnages {

    public static void main (String[]args){
        DicoPersonnages dico = new DicoPersonnages();
        dico.ajoute("Thomas", 9);
        dico.ajoute("Francis", 8); 
        dico.ajoute("Jean");
        System.out.println(dico);
        System.out.println(dico.maxPointsVie());
    }
}