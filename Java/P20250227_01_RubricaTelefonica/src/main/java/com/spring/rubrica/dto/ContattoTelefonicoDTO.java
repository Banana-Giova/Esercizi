package com.spring.rubrica.dto;

import java.time.LocalDate;

import com.spring.rubrica.utility.RubricaUtility;

public class ContattoTelefonicoDTO {
	private String nome, cognome, numero, gruppo_appartenza, contact_id;
	private int id;
	private LocalDate data_nascita;
	private boolean preferito;
	
	public ContattoTelefonicoDTO() {
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
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

	public String getNumero() {
		return numero;
	}

	public void setNumero(String numero) {
		this.numero = numero;
	}

	public String getGruppo_appartenza() {
		return gruppo_appartenza;
	}

	public void setGruppo_appartenza(String gruppo_appartenza) {
		this.gruppo_appartenza = gruppo_appartenza;
	}

	public LocalDate getData_nascita() {
		return data_nascita;
	}

	public void setData_nascita(LocalDate data_nascita) {
		this.data_nascita = data_nascita;
	}

	public boolean isPreferito() {
		return preferito;
	}

	public void setPreferito(Boolean preferito) {
		this.preferito = preferito;
	}

	public String getContact_id() {
		return contact_id;
	}

	public void setContact_id(String contact_id) {
		this.contact_id = contact_id;
	}

	public ContattoTelefonicoDTO(String nome, String cognome, String numero, String gruppo_appartenza,
			LocalDate data_nascita, Boolean preferito) {
		super();
		this.id = RubricaUtility.generateNewContact();
		this.nome = nome;
		this.cognome = cognome;
		this.numero = numero;
		this.gruppo_appartenza = (gruppo_appartenza != null? gruppo_appartenza : "default");
		this.data_nascita = data_nascita;
		this.preferito = (preferito != null? preferito : false);
		this.contact_id = (nome + cognome).toLowerCase() + ((Integer)this.id).toString();
	}
	
	public ContattoTelefonicoDTO(int id, String nome, String cognome, String numero, String gruppo_appartenza,
			LocalDate data_nascita, Boolean preferito) {
		super();
		this.id = id;
		this.nome = nome;
		this.cognome = cognome;
		this.numero = numero;
		this.gruppo_appartenza = (gruppo_appartenza != null? gruppo_appartenza : "default");
		this.data_nascita = data_nascita;
		this.preferito = (preferito != null? preferito : false);
		this.contact_id = (nome + cognome).toLowerCase() + ((Integer)this.id).toString();
	}
}
