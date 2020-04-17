import java.util.ArrayList;

public class GestionContenants<T> {

    private ArrayList<Contenant<T>> liste;

    public GestionContenants() {
        this.liste = new ArrayList<>();
    }

    public GestionContenants(ArrayList<Contenant<T>> liste) {
        this.liste = liste;
    }

    public boolean contiennentTous(ArrayList<Contenant<T>> liste, T elem){
        for (Contenant<T> c : liste){
            if (! c.contient(elem)){
                return false;
            }
        }
        return true;
    }
}
