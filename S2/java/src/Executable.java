public class Executable {
    public static void main(String[] args) {
        CarteCouleur c = new CarteCouleur("Carreau", 11);
        System.out.println(c.getValeur());
        System.out.println(c.getValeurInt());
        System.out.println(c.toString());
        Atout a = new Atout(20);
        System.out.println(a.getValeur());
        System.out.println(a.toString());
        a.setValeur(15);
        System.out.print(a.toString());
    }
}
