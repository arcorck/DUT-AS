public class Executable{
    public static void main (String [] args){
        Table table = new Table();
        table.ajouteconvive(new Personne("Papa", 25));
        table.ajouteconvive(new Personne("GrandPapy", 85));
        table.ajouteconvive(new Personne("Mamie", 63));
        table.ajouteconvive(new Personne("Junior", 2));
        table.ajouteconvive(new Personne("Maman", 22));
        table.ajouteconvive(new Personne("Tonton", 47));
        System.out.println(table);
        System.out.println("Papa à coté de Maman : " + table.sontACote("Papa", "Maman"));
        System.out.println("Papa à coté de GrandPapy : " + table.sontACote("Papa", "GrandPapy"));
        table.change("Papa", "Tonton");
        System.out.println(table);
    }
}