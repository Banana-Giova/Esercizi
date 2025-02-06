package models;

public class Prodotto {
	protected int metri;
	protected String materiale;
	
	public Prodotto(int metri, String materiale) {
		this.metri = metri;
		this.materiale = materiale;
	}
	
	public void setMetri(int metri) {
		this.metri = metri;
	}

	public void setMateriale(String materiale) {
		this.materiale = materiale;
	}

	public int getMetri() {
		return metri;
	}

	public String getMateriale() {
		return materiale;
	}


}
