import java.io.IOException;
import java.net.*;
import java.util.Date;
import java.util.Properties;

public class Serveur {
    public static void main(String [] args) throws IOException { 
        DatagramSocket socket = new DatagramSocket(4445);
        byte[] buf = new byte[256];
        // receive request
        DatagramPacket packet = new DatagramPacket(buf, buf.length); 
        socket.receive(packet);
        String req = new String(packet.getData()); 
        req = req.trim();
        // response
        if (req.equals("date")){
            String dString = "Date : " + new Date().toString();
            buf = dString.getBytes();
        }else{
            if (req.equals("os")){
                String dString = "OS : " + System.getProperties().get("os.name");
                buf = dString.getBytes();
            }else{
                if (req.equals("user")){
                    Properties p = System.getProperties(); 
                    String name = "User : " + p.getProperty("user.name"); 
                    buf = name.getBytes();
                }else{
                    String name = "erreur";
                    buf = name.getBytes();
                }
            }
        }
        // send the response to the client at ”address” and ”port”
        InetAddress address = packet.getAddress();
        int port = packet.getPort();
        packet = new DatagramPacket(buf, buf.length, address, port);
        socket.send(packet);
        socket.close();
    }
}