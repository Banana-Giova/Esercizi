
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		
		Computer comp = new Computer(500, 10, 24, 12, 8, "Lenovo", 2012);
		
		
		System.out.println("Informazioni sul computer\nPrezzo: " + comp.getPrezzo() + "\n" +
		"Peso: " + comp.getPeso() + "\n" +
		"Dimensioni: " + comp.getDimensioni() + "\n" +
		"Produttore: " + comp.getProduttore() + "\n" +
		"Anno di Produzione: " + comp.getAnno_produzione()
		);
		
		System.out.println("Numero di PC al momento: " + comp.getPCnum());
		
		Computer comp2 = new Computer(500, 10, 24, 12, 8, "Lenovo", 2012);
		Computer comp3 = new Computer(500, 10, 24, 12, 8, "Lenovo", 2012);
		
		System.out.println("Numero di PC al momento: " + comp.getPCnum());
	}

}