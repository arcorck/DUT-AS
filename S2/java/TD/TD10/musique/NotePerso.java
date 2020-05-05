import java.util.Objects;

public class NotePerso extends Note implements NotAcc{

    private int frequence, duree;

    public NotePerso(int frequence, int duree){
        super(frequence, duree);
        this.frequence=frequence;
        this.duree=duree;
    }

    public int getDuree(){
        return this.duree;
    }

    public int getFrequence(){
        return this.frequence;
    }

    public void jouer(){
        System.out.println("Fréquence : " + this.frequence + ", durée : " + this.duree);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        NotePerso notePerso = (NotePerso) o;
        return frequence == notePerso.frequence &&
                duree == notePerso.duree;
    }

    @Override
    public int hashCode() {
        return System.identityHashCode(this);
    }
}