package com.spring.ecommerce.dto;

import java.math.BigDecimal;

import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

public class ProdottoDTO {
	private int id;
	
	@NotNull(message = "La descrizione non può essere nulla.")
	@NotBlank(message = "La descrizione non può essere vuota.")
    @Size(max = 255, message = "La descrizione non può superare i 255 caratteri.")
	private String descrizione;
	
	@NotNull(message = "La quantita non può essere nulla")
	@Min(value = 0, message = "La quantita deve essere maggiore o uguale a 0.")
	private int quantita;
	
	@NotNull(message = "Il prezzo del prodotto non può essere nullo.")
    @DecimalMin(value = "0.00", inclusive = true, message = "Il prezzo deve essere maggiore o uguale a 0.00.")
	private BigDecimal prezzo;
	
	@NotNull(message = "Lo sconto non può essere nullo.")
	@Min(value = 0, message = "Lo sconto deve essere maggiore o uguale a 0.")
	@Max(value = 100, message = "Lo sconto non può essere maggiore di 100.")
	private int sconto;
	
    @Size(max = 31, message = "La categoria non può superare i 31 caratteri.")
	private String categoria;
    
    @NotNull(message = "L'ID del venditore non può essere null.")
    private int venditore_id;
    
    public ProdottoDTO() {
    }

	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getDescrizione() {
		return descrizione;
	}
	public void setDescrizione(String descrizione) {
		this.descrizione = descrizione;
	}
	public int getQuantita() {
		return quantita;
	}
	public void setQuantita(int quantita) {
		this.quantita = quantita;
	}
	public BigDecimal getPrezzo() {
		return prezzo;
	}
	public void setPrezzo(BigDecimal prezzo) {
		this.prezzo = prezzo;
	}
	public int getSconto() {
		return sconto;
	}
	public void setSconto(int sconto) {
		this.sconto = sconto;
	}
	public String getCategoria() {
		return categoria;
	}
	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}
	public int getVenditore_id() {
		return venditore_id;
	}
	public void setVenditore_id(int venditore_id) {
		this.venditore_id = venditore_id;
	}

	public ProdottoDTO(int id,
			@NotNull(message = "La descrizione non può essere nulla.") @NotBlank(message = "La descrizione non può essere vuota.") @Size(max = 255, message = "La descrizione non può superare i 255 caratteri.") String descrizione,
			@NotNull(message = "La quantita non può essere nulla") @Min(value = 0, message = "La quantita deve essere maggiore o uguale a 0.") int quantita,
			@NotNull(message = "Il prezzo del prodotto non può essere nullo.") @DecimalMin(value = "0.00", inclusive = true, message = "Il prezzo deve essere maggiore o uguale a 0.00.") BigDecimal prezzo,
			@NotNull(message = "Lo sconto non può essere nullo.") @Min(value = 0, message = "Lo sconto deve essere maggiore o uguale a 0.") @Max(value = 100, message = "Lo sconto non può essere maggiore di 100.") int sconto,
			@Size(max = 31, message = "La categoria non può superare i 31 caratteri.") String categoria,
			@NotNull(message = "L'ID del venditore non può essere null.") int venditore_id) {
		super();
		this.id = id;
		this.descrizione = descrizione;
		this.quantita = quantita;
		this.prezzo = prezzo;
		this.sconto = sconto;
		this.categoria = categoria;
		this.venditore_id = venditore_id;
	}
 
    
}
