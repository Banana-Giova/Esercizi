package models;
import java.util.concurrent.*;

public class MandaPosta implements Runnable {
	private LinkedBlockingQueue<Posta> casella;
	private final String nome = "Manda Posta";
	public LinkedBlockingQueue<Posta> getCasella() {
		return casella;
	}
	public String getNome() {
		return this.nome;
	}
	public void setCasella(LinkedBlockingQueue<Posta> casella) {
		this.casella = casella;
	}
	
	public MandaPosta(LinkedBlockingQueue<Posta> casella) {
		this.setCasella(casella);
	}
	
	private void sendToCasella() throws InterruptedException {
		synchronized (casella) {
			if (casella.size() < 10) {
				casella.put(new Posta("Oggetto", "Contenuto"));
				System.out.printf("%s: Posta mandata! Posta al momento nella casella: %d\n", 
								  this.getNome(), casella.size());
				casella.notifyAll();
			} else {
				System.out.printf("%s: Troppa posta, attendo.\n", this.getNome());
				casella.wait();
			}
		}
	}
	
	@Override
	public void run() {
		try {
			Thread.sleep(1300);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		while (true) {
			try {
				this.sendToCasella();
				Thread.sleep(600);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}
