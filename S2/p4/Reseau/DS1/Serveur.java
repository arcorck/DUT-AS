import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Serveur {

    public static void main(String[] args) {
        try{
            ServerSocket serveur = new ServerSocket(4444);
            while(true) {
                Socket sock = serveur.accept();
                InputStreamReader stream = new InputStreamReader(sock.getInputStream());
                BufferedReader reader = new BufferedReader(stream);
                PrintWriter writer = new PrintWriter(sock.getOutputStream());
                String s = reader.readLine();
                while (s != null && !s.equals("quit")) {
                    String [] lescaracteres = s.split(" ");
                    if (lescaracteres.length == 3){
                        int premierchiffre = Integer.parseInt(lescaracteres[0]); 
                        int secondchiffre = Integer.parseInt(lescaracteres[2]); 
                        int res = 0;
                        if(lescaracteres[1].equals("+") || lescaracteres[1].equals("-") || lescaracteres[1].equals("*") || lescaracteres[1].equals("/")){
                            if (lescaracteres[1].equals("+")){
                                res = premierchiffre + secondchiffre;
                                s = Integer.toString(res);
                            }else{
                                if (lescaracteres[1].equals("-")){
                                    res = premierchiffre - secondchiffre;
                                    s = Integer.toString(res);
                                }else{
                                    if (lescaracteres[1].equals("*")){
                                        res = premierchiffre * secondchiffre;
                                        s = Integer.toString(res);
                                    }else{
                                        res = premierchiffre / secondchiffre;
                                        s = Integer.toString(res);
                                    }
                                }
                            }
                        }
                    }else{
                        s = "Erreur dans le format de la requête : " + s;
                    }
                System.out.println(s);
                writer.println(s);
                writer.flush();
                s = reader.readLine();
                }
            }
        }catch(Exception e){
            System.out.println("Erreur : " + e.toString());
        }
    }
}