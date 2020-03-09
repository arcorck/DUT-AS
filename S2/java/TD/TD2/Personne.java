public class Personne {
    private String nom;
    private int age;

    public Personne (String nom, int age){
        this.nom = nom;
        this.age = age;
    }

    public String getnom(){
        return this.nom;
    }

    public int getage(){
        return this.age;
    }

    public void setage(int age){
        this.age = age;
    }

    public void setnom(String nom){
        this.nom = nom;
    }

    public String toString(){
        return this.getnom() + ", " + this.getage();
    }
}