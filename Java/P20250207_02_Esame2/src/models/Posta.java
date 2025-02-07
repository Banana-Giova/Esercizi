package models;

public class Posta {
	protected String oggetto;
	protected String contenuto;
	public String getOggetto() {
		return oggetto;
	}
	public void setOggetto(String oggetto) {
		this.oggetto = oggetto;
	}
	public String getContenuto() {
		return contenuto;
	}
	public void setContenuto(String contenuto) {
		this.contenuto = contenuto;
	}
	public Posta(String oggetto, String contenuto) {
		this.setOggetto(oggetto);
		this.setContenuto(contenuto);
	}
}
