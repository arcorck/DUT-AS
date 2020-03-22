import java.util.List;
import java.util.ArrayList;
import java.util.Collections;


public class Chenil{
    private List<Chien> leschiens;

    public Chenil (){
        this.leschiens = new ArrayList<>();
    }

    public void deposer(Chien ch){
        if(! this.leschiens.contains(ch)){
             this.leschiens.add(ch);
         }
    }

    public String toString (){
        String res = "";
        for (Chien c : this.leschiens){
            res += c.toString();
        }
        return res;
    }

    public List<Chien> trier (){
        Collections.sort(this.leschiens, new CompareChienPoil());
        return this.leschiens;
    }
    public static void main(String [] args) {
        Chenil chenil =new Chenil();
        chenil.deposer(new Chien("Médor", 15, "brune"));
        chenil.deposer(new Chien("Toutou", 10, "auburn"));
        chenil.deposer(new Chien("Milou", 17, "acajou"));
        chenil.deposer(new Chien("Milou", 17, "acajou"));
        System.out.println(chenil);
        System.out.println(chenil.trier());
    }
}