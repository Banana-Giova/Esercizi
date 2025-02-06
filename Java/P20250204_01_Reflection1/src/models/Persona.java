package models;

public class Persona {
	private int eta = 20;
	private String nome = "Mario";

	public int getEta() {
		return eta;
	}

	public void setEta(int eta) {
		this.eta = eta;
	}

	public void setName(String nome) {
		this.nome = nome;
	}

	private void printData() {
		System.out.println("Eta = " + eta + " Nome = " + nome);
	}

}