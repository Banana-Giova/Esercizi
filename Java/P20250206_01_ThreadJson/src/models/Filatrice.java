package models;
import java.util.Random;
import java.util.concurrent.*;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Filatrice implements Runnable {
	private String[] materiali = {"Cotone", "Lino", "Lana", "Seta", "Poliestere", "Nylon"};
	private Random rng = new Random();
	protected LinkedBlockingQueue<Prodotto> coda_produzione = new LinkedBlockingQueue<Prodotto>(1000);
	private int numero_filatrice;
	private ObjectMapper objectMapper = new ObjectMapper();
	
	public Filatrice(int numero_filatrice) {
		this.numero_filatrice = numero_filatrice;
	}
	@Override
	public void run() {
		System.out.printf("Filatrice numero %d avviata!\n", this.numero_filatrice);
		while (true) {
			String randomaterial = this.materiali[rng.nextInt(this.materiali.length)];
			int randonumber = rng.nextInt(5, 105);
			try {
				this.coda_produzione.put(new Prodotto(randonumber, randomaterial));
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			
			
		}
	}
	
}
