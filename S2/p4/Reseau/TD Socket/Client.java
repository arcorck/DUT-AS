import java.util.Scanner;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {

    public static void main(String[] args) {
        try{
            Scanner sc = new Scanner(System.in);
            Socket sock = new Socket("127.0.0.1", 4444);
            String res = "";
            String total = "";
            while (! res.equals("quit")){
                System.out.println("entrez une phrase a transmettre : ");
                res = sc.nextLine();
                total += res + "\n";
            }
            PrintWriter writer = new PrintWriter(sock.getOutputStream());
            writer.print(total);
            writer.flush();
            sock.close();
            sc.close();
        }catch(Exception e){
            System.out.println("Erreur : " + e.toString());
        }

    }
}