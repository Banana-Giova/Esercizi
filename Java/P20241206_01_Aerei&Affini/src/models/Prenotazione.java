package models;

@SuppressWarnings("unused")
public class Prenotazione {
	private String codice;
	private String utente;
	private int posti_prenotati;
	private Volo volo;
	
	protected Prenotazione(String utente, int posti_prenotati, Volo volo) {
		super();
		this.utente = utente;
		this.posti_prenotati = posti_prenotati;
		this.volo = volo;
		this.codice = utente + posti_prenotati + volo.getCodice();
	}
	
	public String getUtente() {
		return this.utente;
	}
	private void setUtente(String utente) {
		this.utente = utente;
	}
	public String getCodice() {
		return this.codice;
	}
	private void setCodice(String codice) {
		this.codice = codice;
	}
	public Volo getVolo() {
		return this.volo;
	}
	private void setVolo(Volo volo) {
		this.volo = volo;
	}
	public int getPosti_prenotati() {
		return this.posti_prenotati;
	}
	protected void setPosti_prenotati(int posti_prenotati) {
		this.posti_prenotati = posti_prenotati;
	}
}
