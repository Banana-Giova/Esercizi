package models;
import java.util.concurrent.*;

public class LeggiPosta implements Runnable {
	private LinkedBlockingQueue<Posta> casella;
	private final String nome = "Leggi Posta";
	public LinkedBlockingQueue<Posta> getCasella() {
		return casella;
	}
	public String getNome() {
		return this.nome;
	}
	public void setCasella(LinkedBlockingQueue<Posta> casella) {
		this.casella = casella;
	}
	
	public LeggiPosta(LinkedBlockingQueue<Posta> casella) {
		this.setCasella(casella);
	}
	
	private void readFromCasella() throws InterruptedException {
		synchronized (casella) {
			if (casella.size() > 0) {
				casella.remove();
				System.out.printf("%s: Posta letta! Posta al momento nella casella: %d\n", 
								  this.getNome(), casella.size());
				casella.notifyAll();
			} else {
				System.out.printf("%s: Niente posta, attendo.\n", this.getNome());
				casella.wait();
			}
		}
	}
	
	@Override
	public void run() {
		while (true) {
			try {
				this.readFromCasella();
				Thread.sleep(700);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}
