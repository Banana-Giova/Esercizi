package models;

@SuppressWarnings("unused")
public class Prenotazione {
	private String codice;
	private String utente;
	private int posti_prenotati;
	private Volo volo;
	
	public Prenotazione(String utente, int posti_prenotati, Volo volo) {
		this.utente = utente;
		this.posti_prenotati = posti_prenotati;
		this.volo = volo;
		this.codice = utente + posti_prenotati + volo.getCodice();
	}
	
	public String getUtente() {
		return utente;
	}
	private void setUtente(String utente) {
		this.utente = utente;
	}
	public String getCodice() {
		return codice;
	}
	private void setCodice(String codice) {
		this.codice = codice;
	}
	public int getPosti_prenotati() {
		return posti_prenotati;
	}
	public void setPosti_prenotati(int posti_prenotati) {
		this.posti_prenotati = posti_prenotati;
	}
}
