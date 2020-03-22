public class Voiture implements Motorise{
    
    public void faireLePlein (){
        System.out.println("Le plein de la voiture est fait !!");
    }

    public void seDeplacer (){
        roule();
    }

    public void roule (){
        System.out.println("La voiture roule");
    }
}