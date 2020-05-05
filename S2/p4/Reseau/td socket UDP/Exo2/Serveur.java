import java.io.*;
import java.net.*;
import java.util.*;

public class Serveur 
{
    public static void main(String[] args) throws IOException, InterruptedException
    {
        DatagramSocket socket = new DatagramSocket();
        socket.setBroadcast(true);
        while(true)
        {
            byte[] buf = new byte[256];
            buf = new Date().toString().getBytes();
            InetAddress adresse = InetAddress.getByName("192.168.1.255");
            DatagramPacket paquet = new DatagramPacket(buf, buf.length, adresse, 4445);
            socket.send(paquet);
            Thread.sleep(1000);
        }
    }
}