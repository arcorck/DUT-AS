public class Test{
    static int mul1 (int a, int b){
        int res = 0;
        while (b > 0){
            res += a;
            b--;
        }
        return res; 
    }

    static int mul2 (int a, int b){
        int res = 0;
        while (a > 0){
            res += b;
            a--;
        }
        return res; 
    }

    public static void main (String [] args){
        System.out.println(mul1(2,3));
        System.out.println(mul2(2,3));
    }
}