package com.spring.universita.entity;

public class Studente {

	private String matricola, nome, cognome, indirizzo;
	private int anno_nascita, anno_immatricolazione;
	
	public Studente() {
	}
	
	public String getMatricola() {
		return matricola;
	}
	public void setMatricola(String matricola) {
		this.matricola = matricola;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getCognome() {
		return cognome;
	}
	public void setCognome(String cognome) {
		this.cognome = cognome;
	}
	public String getIndirizzo() {
		return indirizzo;
	}
	public void setIndirizzo(String indirizzo) {
		this.indirizzo = indirizzo;
	}
	public int getAnno_nascita() {
		return anno_nascita;
	}
	public void setAnno_nascita(int anno_nascita) {
		this.anno_nascita = anno_nascita;
	}
	public int getAnno_immatricolazione() {
		return anno_immatricolazione;
	}
	public void setAnno_immatricolazione(int anno_immatricolazione) {
		this.anno_immatricolazione = anno_immatricolazione;
	}

	public Studente(String matricola, String nome, String cognome, String indirizzo, 
					int anno_nascita, int anno_immatricolazione) {
		super();
		this.matricola = matricola;
		this.nome = nome;
		this.cognome = cognome;
		this.indirizzo = indirizzo;
		this.anno_nascita = anno_nascita;
		this.anno_immatricolazione = anno_immatricolazione;
	}
}
