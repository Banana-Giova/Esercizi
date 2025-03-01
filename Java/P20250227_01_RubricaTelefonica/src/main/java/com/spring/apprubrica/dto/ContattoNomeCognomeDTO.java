package com.spring.apprubrica.dto;

public class ContattoNomeCognomeDTO {
	private String nome, cognome;

	public ContattoNomeCognomeDTO() {
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

	public ContattoNomeCognomeDTO(String nome, String cognome) {
		super();
		this.nome = nome;
		this.cognome = cognome;
	}
	
	
}
