package com.spring.apprubrica.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "rubriche")
public class RubricaTelefonica {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "proprietario", nullable = false, length = 50) // Aggiungi le caratteristiche delle colonne
    private String proprietario;

    @Column(name = "anno_creazione", nullable = false)
    private int anno_creazione;
	
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

