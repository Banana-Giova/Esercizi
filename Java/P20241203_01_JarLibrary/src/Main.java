import java.io.IOException;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		
		
		Computer comp = new Computer(500, 10, 24, 12, 8, "Lenovo", 2012);
		
		
	   /*System.out.println("Informazioni sul computer\nPrezzo: " + comp.getPrezzo() + "\n" +
		"Peso: " + comp.getPeso() + "\n" +
		"Dimensioni: " + comp.getDimensioni() + "\n" +
		"Produttore: " + comp.getProduttore() + "\n" +
		"Anno di Produzione: " + comp.getAnno_produzione()
		);
		
		System.out.println("Numero di PC al momento: " + comp.getPCnum());*/
		
		Computer comp2 = new Computer(399, 12, 28, 10, 6, "Lenovo", 2014);
		Computer comp3 = new Computer(149, 8, 20, 8, 4, "Lenovo", 2016);
		
		//System.out.println("Numero di PC al momento: " + comp.getPCnum());
		
		String jsonString;
		ObjectMapper objectMapper = new ObjectMapper();
		jsonString = objectMapper.writeValueAsString(comp);
		System.out.println(jsonString);
		
	}

}
