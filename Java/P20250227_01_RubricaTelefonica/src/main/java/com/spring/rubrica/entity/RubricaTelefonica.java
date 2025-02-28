package com.spring.rubrica.entity;

import com.spring.rubrica.utility.RubricaUtility;

public class RubricaTelefonica {
	private String proprietario;
	private int id, anno_creazione;
	
	public RubricaTelefonica() {
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}
	
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

	public RubricaTelefonica(String proprietario, int anno_creazione) {
		super();
		this.id = RubricaUtility.generateRegKey();
		this.proprietario = proprietario;
		this.anno_creazione = anno_creazione;
	}
	
	public RubricaTelefonica(int id, String proprietario, int anno_creazione) {
		super();
		this.id = id;
		this.proprietario = proprietario;
		this.anno_creazione = anno_creazione;
	}
}

