package com.spring.universita.entity;

public class Professore {
	private String id, nome, cognome, materia_inse;
	
	public Professore () {
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
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

	public String getMateria_inse() {
		return materia_inse;
	}

	public void setMateria_inse(String materia_inse) {
		this.materia_inse = materia_inse;
	}

	public Professore(String id, String nome, String cognome, String materia_inse) {
		super();
		this.id = id;
		this.nome = nome;
		this.cognome = cognome;
		this.materia_inse = materia_inse;
	}
}
