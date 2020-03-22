public class Avion implements Motorise{
    
    public void faireLePlein (){
        System.out.println("Le plein de l'avion est fait !!");
    }

    public void seDeplacer (){
        vole();
    }

    public void vole (){
        System.out.println("L'avion vole'");
    }
}