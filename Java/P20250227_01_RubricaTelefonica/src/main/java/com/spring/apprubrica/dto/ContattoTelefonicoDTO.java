package com.spring.apprubrica.dto;

import java.time.LocalDate;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.PastOrPresent;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;

public class ContattoTelefonicoDTO {
	
	@NotNull(message = "Il nome non può essere nullo")
    @NotBlank(message = "Il nome non può essere vuoto")
    @Size(max = 50, message = "Il nome non può superare i 50 caratteri")
    private String nome;

	@NotNull(message = "Il cognome non può essere nullo")
    @NotBlank(message = "Il cognome non può essere vuoto")
    @Size(max = 50, message = "Il cognome non può superare i 50 caratteri")
    private String cognome;

	@NotNull(message = "Il numero di telefono non può essere nullo")
    @NotBlank(message = "Il numero di telefono non può essere vuoto")
    @Pattern(regexp = "^[0-9]{8,15}$", message = "Il numero di telefono deve contenere solo cifre e avere tra 8 e 15 caratteri")
    private String numero;

	@Size(max = 50, message = "Il gruppo di appartenenza non può superare i 50 caratteri")
    private String gruppo_appartenenza;

    @NotNull(message = "La data di nascita non può essere nulla")
    @PastOrPresent(message = "La data di nascita non può essere nel futuro")
    private LocalDate data_nascita;
	
    private int rub_id;
	private String con_id;
	
	private boolean preferito;
	
	public ContattoTelefonicoDTO() {
	}
	
	public int getRub_id() {
		return rub_id;
	}

	public void setRub_id(int rub_id) {
		this.rub_id = rub_id;
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

	public String getGruppo_appartenenza() {
		return gruppo_appartenenza;
	}

	public void setGruppo_appartenenza(String gruppo_appartenza) {
		this.gruppo_appartenenza = gruppo_appartenza;
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

	public String getCon_id() {
		return con_id;
	}

	public void setCon_id(String contact_id) {
		this.con_id = contact_id;
	}
	
	public ContattoTelefonicoDTO(int rub_id, String con_id, String nome, String cognome, String numero, String gruppo_appartenza,
			LocalDate data_nascita, Boolean preferito) {
		super();
		this.rub_id = rub_id;
		this.nome = nome;
		this.cognome = cognome;
		this.numero = numero;
		this.gruppo_appartenenza = (gruppo_appartenza != null? gruppo_appartenza : "default");
		this.data_nascita = data_nascita;
		this.preferito = (preferito != null? preferito : false);
		this.con_id = con_id;
	}
}
