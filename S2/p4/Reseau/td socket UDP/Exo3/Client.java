import java.io.*;
import java.net.*;

public class Client 
{
    public static void main(String[] args) throws IOException
    {
        MulticastSocket socket = new MulticastSocket(4445);
        socket.setBroadcast(true);
        InetAddress group=InetAddress.getByName("225.0.0.0");
        socket.joinGroup(group);
        while(true)
        {
            byte[] buf = new byte[256];
            DatagramPacket paquet = new DatagramPacket(buf, buf.length);
            socket.receive(paquet);
            String affiche = new String(paquet.getData(), 0, paquet.getLength());
            System.out.println(affiche);
        }
    }
}