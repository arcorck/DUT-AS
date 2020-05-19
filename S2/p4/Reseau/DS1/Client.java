import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {

    public static void main(String[] args) {
        try{
            Scanner sc = new Scanner(System.in);
            Socket sock = new Socket("127.0.0.1", 4444);
            String res = "";
            PrintWriter writer = new PrintWriter(sock.getOutputStream());
            InputStreamReader stream = new InputStreamReader(sock.getInputStream());
            BufferedReader reader = new BufferedReader(stream);
            while (!res.equals("quit")){
                System.out.println("entrez une opération : ");
                res = sc.nextLine();
                if (!res.equals("quit")){
                    writer.println(res);
                    writer.flush();
                    System.out.println(res + " = " + reader.readLine());
                }
            }
            sock.close();
            sc.close();
        }catch(Exception e){
            System.out.println("Erreur : " + e.toString());
        }
    }
}