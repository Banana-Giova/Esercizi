package models;

public class Studente {
	protected String getNome() {
		return nome;
	}

	protected void setNome(String nome) {
		this.nome = nome;
	}

	protected String getCognome() {
		return cognome;
	}

	protected void setCognome(String cognome) {
		this.cognome = cognome;
	}

	protected int getAge() {
		return age;
	}

	protected void setAge(int age) {
		this.age = age;
	}

	protected String getMatricola() {
		return matricola;
	}

	protected void setMatricola(String matricola) {
		this.matricola = matricola;
	}

	private String nome;
	private String cognome;
	private int age;
	private String matricola;
	
	protected Studente (String nome, String cognome, int age, String matricola) {
		this.nome = nome;
		this.cognome = cognome;
		this.age = age;
		this.matricola = matricola;
	}
}
