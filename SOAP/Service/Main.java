import javax.xml.ws.Endpoint;
import com.calc.Calculator;

public class Main {
    public static void main(String[] args) {
        System.out.println("The server is running...");
        Endpoint.publish("http://localhost:8080/calc", new Calculator());
        System.out.println("http://localhost:8080/calc?wsdl");
    }
}