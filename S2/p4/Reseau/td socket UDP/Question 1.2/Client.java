import java.io.IOException;
import java.net.*;

public class Client {
    public static void main(String[] args) throws IOException { // get a datagram socket
        DatagramSocket socket = new DatagramSocket();
        // send request
        byte[] buf = args[0].getBytes();
        InetAddress address = InetAddress.getByName("127.0.0.1");
        DatagramPacket packet = new DatagramPacket(buf, buf.length, address, 4445); 
        socket.send(packet);
        // get respons
        byte[] reponse = new byte[256];
        packet = new DatagramPacket(reponse, reponse.length); 
        socket.receive(packet);
        // display response
        String received = new String(packet.getData(), 0, packet.getLength()); 
        System.out.println(received);
        socket.close();
    }
}