package com.spring.universita.dto;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Pattern;

public class StudenteDTO {

	@NotNull(message = "La matricola non può essere nulla")
	@Pattern(regexp = "\\d{7}", message = "Il formato della matricola è invalido")
	private String matricola;
	
	@NotNull(message = "Il nome non può essere nullo")
	private String nome;
	
	@NotNull(message = "Il cognome non può essere nullo")
	private String cognome;
	
	@NotNull(message = "L'indirizzo non può essere nullo")
	private String indirizzo;
	
	@NotNull(message = "L'anno di nascita non può essere nullo")
	private int anno_nascita;
	
	@NotNull(message = "L'anno di immatricolazione non può essere nullo")
	private int anno_immatricolazione;
	
	public StudenteDTO() {
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

	public StudenteDTO(String matricola, String nome, String cognome, String indirizzo, 
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