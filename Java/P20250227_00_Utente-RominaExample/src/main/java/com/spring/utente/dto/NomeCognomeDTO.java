package com.spring.utente.dto;

public class NomeCognomeDTO {

	private String nome, cognome;
	
	public NomeCognomeDTO() {
		// TODO Auto-generated constructor stub
	}

	public NomeCognomeDTO(String nome, String cognome) {
		this.nome = nome;
		this.cognome = cognome;
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
	
	
}
