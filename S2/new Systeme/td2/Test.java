public class Test{
    static int mul1 (int a, int b){
        int res = 0;
        for (int i = 0; i < b; i++){
            res += a;
        }
        return res; 
    }

    static int mul2 (int a, int b){
        int res = 0;
        for (int i = 0; i < a; i++){
            res += b;
        }
        return res; 
    }

    public static void main (String [] args){
        System.out.println(mul1(2,3));
        System.out.println(mul2(2,3));
    }
}