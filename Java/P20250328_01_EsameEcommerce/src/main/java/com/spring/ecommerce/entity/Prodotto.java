package com.spring.ecommerce.entity;

import java.math.BigDecimal;

import org.hibernate.annotations.OnDelete;
import org.hibernate.annotations.OnDeleteAction;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.Table;
import jakarta.validation.constraints.Size;

@Entity
@Table(name = "prodotti")
public class Prodotto {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;
	
	@Column(name = "descrizione", nullable = false, length = 255)
	private String descrizione;
	
	@Column(name = "quantita", nullable = false, precision = 6, updatable = true)
	private int quantita;
	
	@Column(name = "prezzo", nullable = false, precision = 6, scale = 2)
	@Size(min = 0)
	private BigDecimal prezzo;
	
	@Column(name = "sconto", nullable = false)
	@Size(min = 0, max = 100)
	private int sconto;
	
	@Column(name = "categoria", nullable = true, length = 31)
	private String categoria;
	
    @JoinColumn(name = "FK_Venditore", nullable = false)
    @OnDelete(action = OnDeleteAction.CASCADE)
	private Venditore venditore;
	
	public Prodotto() {
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
	public int getId() {
		return id;
	}
	public Venditore getVenditore() {
		return venditore;
	}
	public void setVenditore(Venditore venditore) {
		this.venditore = venditore;
	}

	public Prodotto(String descrizione, int quantita, @Size(min = 0) BigDecimal prezzo,
			@Size(min = 0, max = 100) int sconto, String categoria, Venditore venditore) {
		super();
		this.descrizione = descrizione;
		this.quantita = quantita;
		this.prezzo = prezzo;
		this.sconto = sconto;
		this.categoria = categoria;
		this.venditore = venditore;
	}
}
