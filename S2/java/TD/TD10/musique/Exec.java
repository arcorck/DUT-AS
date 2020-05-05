public class Exec {

    public static void main(String[] args) {
        Accord acc = new Accord();
        acc.add(new Note(5, 4));
        acc.add(new Note(4, 3));
        acc.add(new Note(3, 2));
        acc.jouer();
        System.out.println("\n");
        Partition p = new Partition();
        p.add(new NotePerso(5, 4));
        p.add(acc);
        p.add(new NotePerso(1,8));
        p.jouer();
    }
}
