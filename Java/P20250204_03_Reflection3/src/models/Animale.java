package models;

public class Animale {
	public String razza;
	private int eta = 8;

	public Animale(String razza) {
	}

	private Animale(String razza, int eta) {
		this.razza = razza;
		this.eta = eta;
	}

	public String getRazza() {
		return razza;
	}

	public void setRazza(String razza) {
		this.razza = razza;
	}

	public int getEta() {
		return eta;
	}

	public void setEta(int eta) {
		this.eta = eta;
	}

}