import java.io.*;
import java.net.*;
import java.util.*;

public class Serveur 
{
    public static void main(String[] args) throws IOException, InterruptedException
    {
        Scanner in = new Scanner(System.in);
        DatagramSocket socket = new DatagramSocket();
        socket.setBroadcast(true);
        while(true)
        {
            byte[] buf = new byte[256];
            System.out.println("Ecrivez le texte a envoyer au client : ");
            buf = in.nextLine().getBytes();
            InetAddress adresse = InetAddress.getByName("225.0.0.0");
            DatagramPacket paquet = new DatagramPacket(buf, buf.length, adresse, 4445);
            socket.send(paquet);
        }
    }
}