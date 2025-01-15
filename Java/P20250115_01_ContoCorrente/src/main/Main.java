package main;
import java.util.Scanner;
import models.*;

public class Main {

	public static void main(String[] args) throws Exception {
		Contocorrente.setSaldo(50);
		Scanner scanner = new Scanner(System.in);
		System.out.println("Sincronizzato o non sincronizzato? (Y/n)");
		String input = scanner.nextLine().trim();
		scanner.close();
		
		if (input.equalsIgnoreCase("Y")) {
			ClienteSync c1 = new ClienteSync("Mario", 20);
			ClienteSync c2 = new ClienteSync("Lucia", 50);
			// Avvio i Threads
			c1.start();
			c2.start();
			// Attendo il completamento
			c1.join();
			c2.join();
		} else if (input.equalsIgnoreCase("n")) {
			ClienteNonSync c1 = new ClienteNonSync("Mario", 20);
			ClienteNonSync c2 = new ClienteNonSync("Lucia", 50);
			// Avvio i Threads
			c1.start();
			c2.start();
			// Attendo il completamento
			c1.join();
			c2.join();
		} else {
			System.out.println("Input invalido.");
			System.exit(0);
		}

	}

}
