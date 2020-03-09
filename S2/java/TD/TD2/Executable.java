public class Executable{
    public static void main (String [] args){
        Table table = new Table();
        table.ajouteconvive(new Personne("Papa", 25));
        table.ajouteconvive(new Personne("GrandPapy", 85));
        table.ajouteconvive(new Personne("Mamie", 63));
        table.ajouteconvive(new Personne("Junior", 2));
        table.ajouteconvive(new Personne("Maman", 22));
        table.ajouteconvive(new Personne("Tonton", 47));
        System.out.print("Affichage de la table : ");
        System.out.println(table);
        System.out.println("\n");
        System.out.println("Tests de Acotes : ");
        System.out.println("Papa à coté de Maman : " + table.sontACote("Papa", "Maman"));
        System.out.println("Papa à coté de GrandPapy : " + table.sontACote("Papa", "GrandPapy"));
        System.out.println("\n");
        System.out.println("Tests de change : ");
        table.change("Papa", "Tonton");
        System.out.println(table);
        System.out.println("\n");
        System.out.println("Tests de doyen : ");
        System.out.println("La personne la plus agée de la table est agée de " + table.doyen() + " ans");
        System.out.println("\n");
        System.out.println("Tests de estTrié : ");
        System.out.println("table triée : " + table.estTrie());
        Table t = new Table();
        t.ajouteconvive(new Personne("Papa", 25));
        t.ajouteconvive(new Personne("GrandPapy", 85));
        t.ajouteconvive(new Personne("Mamie", 93));
        System.out.println("t triée : " + t.estTrie());
        System.out.println("\n");
        System.out.println("Tests de benjamin : ");
        System.out.println("benjamin de table : " + table.benjamin());
        System.out.println("benjamin de t : " + t.benjamin());
        System.out.println("\n");
        System.out.println("Tests de trie : ");
        table.trie();
        System.out.println(table);
    }
}