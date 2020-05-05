import java.util.Objects;

public class Note{

    private int frequence, duree;

    public Note(int frequence, int duree){
        this.frequence = frequence;
        this.duree = duree;
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
        Note note = (Note) o;
        return frequence == note.frequence &&
                duree == note.duree;
    }

    @Override
    public int hashCode() {
        return System.identityHashCode(this);
    }
}