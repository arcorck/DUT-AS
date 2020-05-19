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
            String s = "";
            while (! res.equals("quit")){
                System.out.println("entrez une phrase a transmettre : ");
                res = sc.nextLine();
                writer.println(res);
                writer.flush();
                System.out.println("message(s) envoyé(s) au serveur : ");
                System.out.println(reader.readLine());
            }
            sock.close();
            sc.close();
        }catch(Exception e){
            System.out.println("Erreur : " + e.toString());
        }
    }
}