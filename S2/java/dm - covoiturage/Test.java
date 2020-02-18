

public class Test{
    public static void main(String[] args) {
        String s = "abc";
        String a = "abd";
        String b = "abb";
        String c = "abc";
        System.out.println(s.compareTo(a));
        System.out.println(s.compareTo(b));
        System.out.println(s.compareTo(c));
    }
}