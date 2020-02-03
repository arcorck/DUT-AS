import java.util.*;

public class Table {
    private ArrayList<Personne> convives;

    public Table(){
        this.convives = new ArrayList<Personne>();
    }

    public void ajouteconvive (Personne convive){
        this.convives.add(convive);
    }

    public String toString(){
        String s = "";
        for (int i = 0; i < this.convives.size(); i++){
            if (i < this.convives.size()-1){
                s += this.convives.get(i).toString() + " | ";
            }else{
                s += this.convives.get(i).toString();
            }
        }
        return s;
    }

    public boolean sontACote (String p1, String p2){
        for (int i = 0; i < this.convives.size()-1; i++){
            if (this.convives.get(i).getnom().equals(p1) && this.convives.get(i+1).getnom().equals(p2) || this.convives.get(i).getnom().equals(p2) && this.convives.get(i+1).getnom().equals(p1)){
                return true;
            }
        }
        return false;
    }

    public void change (String p1, String p2){
        int indicep1 = 0, indicep2 = 0;
        for (int i = 0; i < this.convives.size(); i++){
            if (this.convives.get(i).getnom().equals(p1)){
                indicep1 = i;
            }
            if (this.convives.get(i).getnom().equals(p2)){
                indicep2 = i;
            }
            Personne aux = new Personne(this.convives.get(indicep1).getnom(), this.convives.get(indicep1).getage());
            this.convives.set(indicep1, this.convives.get(indicep2));
            this.convives.set(indicep2, aux);
        }
    }
}