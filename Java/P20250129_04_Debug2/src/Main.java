
public class Main {

	public static void main(String[] args) throws InterruptedException {
		Cliente c1 = new Cliente("Mario", 20);
		Cliente c2 = new Cliente("Lucia", 50);

		// Avvio i Threads
		c1.start();
		c2.start();
		
		// Attendo il completamento
		c1.join();
		c2.join();
		
	}

}
