import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class Serveur {

    public static void main(String[] args) {
        try{
            ServerSocket serveur = new ServerSocket(4444);
            Socket sock = serveur.accept();
            InputStreamReader stream = new InputStreamReader(sock.getInputStream());
            BufferedReader reader = new BufferedReader(stream);
            String s = reader.readLine();
            System.out.println("message reçu : ");
            while (s != null && ! s.equals("quit")){
                System.out.println(s);
                s = reader.readLine();
            }
            sock.close();
            serveur.close();
        }catch(Exception e){
            System.out.println("Erreur : " + e.toString());
        }

    }
}