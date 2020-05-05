import java.util.HashSet;
import java.util.Iterator;

public class Accord extends HashSet<Note> implements NotAcc{

    HashSet<Note> accord;

    public Accord (){
        this.accord = new HashSet<>();
    }

    public boolean add (Note n){
        return this.accord.add(n);
    }

    public int duree (){
        int dureemax = 0;
        Iterator<Note> iterator = accord.iterator();
        while (iterator.hasNext()) {
            Note note = iterator.next();
            if (note.getDuree() > dureemax) {
                dureemax += note.getDuree();
            }
        }
        return dureemax;
    }

    boolean isPowerOfTwo(int x) {
        return (x != 0) && ((x & (x - 1)) == 0);
    }

    public boolean estHarmonieux (){
        Iterator<Note> iterator = accord.iterator();
        while (iterator.hasNext()) {
            Note note = iterator.next();
            if (!isPowerOfTwo(note.getFrequence())){
                return false;
            }
        }
        return true;
    }

    public void jouer (){
        Iterator<Note> iterator = accord.iterator();
        while (iterator.hasNext()) {
            Note note = iterator.next();
            note.jouer();
        }
    }
}
