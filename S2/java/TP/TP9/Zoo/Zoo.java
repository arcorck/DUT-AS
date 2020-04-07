import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

public class Zoo {
    private String nom;
    private List<Animal> lesAnimaux;

    public Zoo(String nom) {
        this.nom = nom;
        this.lesAnimaux = new ArrayList<>();
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public List<Animal> getLesAnimaux() {
        return lesAnimaux;
    }

    public void acceuillir (Animal a){
        this.lesAnimaux.add(a);
    }

    public void soigner (Animal a) throws NestpasBlesseException, NestpasdansleZooException{
        if (!this.lesAnimaux.contains(a)){
            throw new NestpasdansleZooException();
        }else {
            if (!a.isBlesse()) {
                throw new NestpasBlesseException();
            }else{
                a.setBlesse(false);
            }
        }
    }
}
