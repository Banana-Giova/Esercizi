package models;

@SuppressWarnings("unused")
public class Aereo {

	private String codice;
	private int posti_totali;
	
	public String getCodice() {
		return codice;
	}

	public int getPosti_totali() {
		return posti_totali;
	}
	
	private void setPosti_totali(int posti_totali) {
		this.posti_totali = posti_totali;
	}
	
	public Aereo (String codice, int posti_totali) {
		this.codice = codice;
		if (posti_totali > 0) {
			this.posti_totali = posti_totali;
		} else {
			throw new IllegalArgumentException("I posti dell'aereo non possono essere meno di 0!");
		}
	}
}
