public class Bateau implements Motorise{
    
    public void faireLePlein (){
        System.out.println("Le plein du bateau est fait !!");
    }

    public void seDeplacer (){
        navigue();
    }

    public void navigue (){
        System.out.println("Le bateau navigue");
    }
}