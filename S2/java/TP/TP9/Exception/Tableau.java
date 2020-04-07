import java.util.Collections;
import java.util.List;
import java.util.ArrayList;
import java.lang.Math;
import java.util.NoSuchElementException;

public class Tableau {
    private List<Integer> tab;

    public Tableau () {
        tab = new ArrayList<Integer>();
    }

    public void remplir() {
        int nb = (int)(Math.random()* 10);
        for(int i = 0; i< nb; ++i)
            tab.add((int)(Math.random()* 50));
    }

    @Override
    public String toString() {
        return tab.toString();
    }

    public List<Integer> getTableau() {
        return this.tab;
    }

    public int getElement (int indice) throws NoSuchElementException {
        if (indice < 0 || indice >= this.tab.size()){
            throw new NoSuchElementException();
        }else{
            return this.tab.get(indice);
        }
    }

    public int getMax () throws NoSuchElementException{
        if (this.tab.isEmpty()){
            throw new NoSuchElementException();
        }else{
            return Collections.max(tab);
        }
    }

    public int getMin () throws PasDeTelElementException{
        if (this.tab.isEmpty()){
            throw new PasDeTelElementException();
        }else{
            return Collections.min(tab);
        }
    }
}