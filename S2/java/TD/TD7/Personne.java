public class Personne{
    private String nom;
    private Integer age;

    public Personne (){
        this.nom = "Sans nom";
        this.age = 0;
    }

    public Personne (String n, int a){
        this.nom = n;
        this.age = a;
    }

    public Integer getAge(){
        return this.age;
    }

    public String toString(){
        return this.nom + " a " + this.age + " an(s)\n";
    }
}