package models;

public class ClienteNonSync extends Thread {
	String nome;
	double somma;
	
	public ClienteNonSync(String nome, double somma) {
		this.nome = nome;
		this.somma = somma;
	}
	
	@Override
	public void run() {
		try {
			Contocorrente.prelievoNonSync(this.somma);
			System.out.println("Prelievo di " + this.somma + 
					           " effettuato con successo da " 
					           + this.nome + "!");
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println("Prelievo di " + this.nome + " fallito!");
		}
	}
}
