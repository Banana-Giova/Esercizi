package com.spring.apprubrica.dto;

import com.spring.apprubrica.utility.RubricaUtility;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;
import java.time.Year;

public class RubricaTelefonicaDTO {
	private int id;
	
	@NotNull(message = "Il proprietario non può essere nullo")
	@NotBlank(message = "Il proprietario non può essere vuoto")
    @Size(max = 50, message = "Il proprietario non può superare i 50 caratteri")
	private String proprietario;
	
	@NotNull(message = "L'anno di creazione non può essere nullo")
	@Min(value = 1900, message = "L'anno di creazione deve essere almeno 1900")
	private int anno_creazione;
	
	public RubricaTelefonicaDTO() {
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
        if (anno_creazione > Year.now().getValue()) {
            throw new IllegalArgumentException("L'anno non può essere maggiore di quello attuale");
        }
        this.anno_creazione = anno_creazione;
	}

	public RubricaTelefonicaDTO(String proprietario, int anno_creazione) {
		super();
		this.id = RubricaUtility.generateRegKey();
		this.proprietario = proprietario;
		this.anno_creazione = anno_creazione;
	}
	
	public RubricaTelefonicaDTO(int id, String proprietario, int anno_creazione) {
		super();
		this.id = id;
		this.proprietario = proprietario;
		this.anno_creazione = anno_creazione;
	}
}
