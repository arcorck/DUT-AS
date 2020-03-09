import java.util.*;

public class GroupeAmis{
    private Map<String, Set<String>> lesAmis;

    public GroupeAmis (){
        this.lesAmis = new HashMap<>();
    }

    public String toString(){
        return this.lesAmis.toString();
    }

    public void add (String nom, String activite){
        if (! this.lesAmis.containsKey(nom)){
            this.lesAmis.put(nom, new HashSet<>());    
        }
        this.lesAmis.get(nom).add(activite);
    }

    public static void main(String[]args){
        GroupeAmis gr = new GroupeAmis();
        gr.add("Camille", "Velo");
        gr.add("Dominique", "Velo");
        gr.add("Camille", "Kayak");
        gr.add("Camille", "Boxe");
        gr.add("Camille", "Velo");
        gr.add("Claude", "Lecture");
        gr.add("Claude", "Tricot");
        gr.add("Claude", "Boxe");
        gr.add("Claude", "Velo");
        System.out.println(gr);
    }
}