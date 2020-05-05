import java.io.*;
import java.net.*;

public class Client 
{
    public static void main(String[] args) throws IOException
    {
        DatagramSocket socket = new DatagramSocket(4445);
        socket.setBroadcast(true);
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