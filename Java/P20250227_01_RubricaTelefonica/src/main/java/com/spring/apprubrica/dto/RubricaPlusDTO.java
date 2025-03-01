package com.spring.apprubrica.dto;

public class RubricaPlusDTO {
	private String proprietario;
	private int anno_creazione, numero_contatti;
	public String getProprietario() {
		return proprietario;
	}
	public void setProprietario(String proprietario) {
		this.proprietario = proprietario;
	}
	public int getAnno_creazione() {
		return anno_creazione;
	}
	public void setAnno_creazione(int anno_creazione) {
		this.anno_creazione = anno_creazione;
	}
	public int getNumero_contatti() {
		return numero_contatti;
	}
	public void setNumero_contatti(int numero_contatti) {
		this.numero_contatti = numero_contatti;
	}
	public RubricaPlusDTO(String proprietario, int anno_creazione, int numero_contatti) {
		super();
		this.proprietario = proprietario;
		this.anno_creazione = anno_creazione;
		this.numero_contatti = numero_contatti;
	}
	
	
}
