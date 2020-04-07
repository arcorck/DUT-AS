public class ExecutableSW{
    public static void main(String[] args) {
        Personnage p1 = new Ewok("Wicket Warrick",0.80, "éclaireur");
        System.out.println(p1);
        // Doit afficher :
        // Je suis un Ewok, je m'appelle Wicket Warrick, je mesure 0.80 mètre(s)
        // et je suis éclaireur.

        Personnage p2 = new Wookie("Attichitcuk", 2.29, "une arbalète");
        System.out.println(p2);
        // Doit afficher :
        // Je suis un Wookie, je m'appelle Attichitcuk, je mesure 2.29 mètre(s)
        // et porte une arbalète.

        Personnage p3 = new Wookie(" Burryaga Agaburry", 2.21, "un sabre laser");
        System.out.println(p3);
        // Doit afficher :
        // Je suis un Wookie, je m'appelle Burryaga Agaburry,
        // je mesure 2.21 mètre(s) et porte un sabre laser.

        Personnage p4 = new Ewok("Chef Chirpa",1.0, "chef");
        System.out.println(p4);
        // Doit afficher :
        // Je suis un Ewok, je m'appelle Chef Chirpa, je mesure 1 mètre(s)
        // et je suis chef.


        RencontreStarWars starWars = new RencontreStarWars();
        starWars.add(p1);
        starWars.add(p2);
        starWars.add(p3);
        starWars.add(p4);
        System.out.println(starWars);
        // Doit afficher :
        // StarWars [Je suis un Ewok, je m'appelle Wicket Warrick, je mesure 0.8
        // mètre(s) et je suis un éclaireur , Je suis un Wookie, je m'appelle
        // Attichitcuk, je mesure 2.29 mètre(s) et porte une arbalète , Je suis
        // un Wookie, je m'appelle Burryaga Agaburry, je mesure 2.21 mètre(s)
        // et porte un sabre laser , Je suis un Ewok, je m'appelle Chef Chirpa,
        // je mesure 1.0 mètre(s) et je suis un chef ]

        starWars.trierParRace();
        System.out.println("Par race "+ starWars);
        // doit afficher :
        // [Je suis un Ewok, je m'appelle Wicket Warrick, je mesure 0.8 mètre(s) // et je suis un éclaireur , Je suis un Ewok, je m'appelle Chef Chirpa, // je mesure 1.0 mètre(s) et je suis un chef , Je suis un Wookie,
        // je m'appelle Attichitcuk, je mesure 2.29 mètre(s) et porte une
        // arbalète , Je suis un Wookie, je m'appelle Burryaga Agaburry, je
        // mesure 2.21 mètre(s) et porte un sabre laser ]

        starWars.trierParTaille();
        System.out.println("Par taille " +starWars);
        // Doit afficher :
        // StarWars [Je suis un Ewok, je m'appelle Wicket Warrick, je mesure 0.8
        // mètre(s) et je suis un éclaireur , Je suis un Ewok, je m'appelle Chef
        // Chirpa, je mesure 1.0 mètre(s) et je suis un chef , Je suis un Wookie,
        // je m'appelle Burryaga Agaburry, je mesure 2.21 mètre(s) et porte un
        // sabre laser , Je suis un Wookie, je m'appelle Attichitcuk, je mesure
        // 2.29 mètre(s) et porte une arbalète ]
    } }