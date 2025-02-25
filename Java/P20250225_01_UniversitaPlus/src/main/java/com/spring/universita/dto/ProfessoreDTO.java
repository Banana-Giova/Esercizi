package com.spring.universita.dto;

import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Pattern;

public class ProfessoreDTO {
	
	@NotNull(message = "L'id non può essere nullo")
	@Pattern(regexp = "[A-Za-z]{3}\\d{6}", message = "Il formato dell'id è invalido")
	private String id;
	
	@NotNull(message = "Il nome non può essere nullo")
	private String nome;
	
	@NotNull(message = "Il cognome non può essere nullo")
	private String cognome;
	
	@NotNull(message = "La materia insegnata non può essere nulla")
	private String materia_inse;
	
	
	public ProfessoreDTO () {
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

	public ProfessoreDTO (String id, String nome, String cognome, String materia_inse) {
		super();
		this.id = id;
		this.nome = nome;
		this.cognome = cognome;
		this.materia_inse = materia_inse;
	}
}
