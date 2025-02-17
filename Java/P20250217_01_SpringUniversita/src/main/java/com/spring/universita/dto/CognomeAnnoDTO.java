package com.spring.universita.dto;

public class CognomeAnnoDTO {
	private String cognome; 
	private int anno_nascita, anno_iscrizione;

	public CognomeAnnoDTO() {
	}

	public String getCognome() {
		return cognome;
	}

	public void setCognome(String cognome) {
		this.cognome = cognome;
	}

	public int getAnno_nascita() {
		return anno_nascita;
	}

	public void setAnno_nascita(int anno_nascita) {
		this.anno_nascita = anno_nascita;
	}

	public int getAnno_iscrizione() {
		return anno_iscrizione;
	}

	public void setAnno_iscrizione(int anno_iscrizione) {
		this.anno_iscrizione = anno_iscrizione;
	}
	
	public void setAll(String cognome, int anno_nascita, int anno_iscrizione) {
		this.cognome = cognome;
		this.anno_nascita = anno_nascita;
		this.anno_iscrizione = anno_iscrizione;
	}

	public CognomeAnnoDTO(String cognome, int anno_nascita, int anno_iscrizione) {
		super();
		this.cognome = cognome;
		this.anno_nascita = anno_nascita;
		this.anno_iscrizione = anno_iscrizione;
	}
}
