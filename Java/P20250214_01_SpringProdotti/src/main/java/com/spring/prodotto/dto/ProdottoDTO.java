package com.spring.prodotto.dto;

public class ProdottoDTO {

	private int id;
	private String marca, modello, descrizione, categoria;
	private double prezzo_max, prezzo_sugg;
	private int quantita;
	
	public ProdottoDTO() {
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getMarca() {
		return marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public String getModello() {
		return modello;
	}

	public void setModello(String modello) {
		this.modello = modello;
	}

	public String getDescrizione() {
		return descrizione;
	}

	public void setDescrizione(String descrizione) {
		this.descrizione = descrizione;
	}

	public String getCategoria() {
		return categoria;
	}

	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}

	public double getPrezzo_max() {
		return prezzo_max;
	}

	public void setPrezzo_max(double prezzo_max) {
		if (prezzo_max >= 0) {
			this.prezzo_max = prezzo_max;
		} else {
			System.out.println("Impossibile impostare un prezzo minore di 0! Default a 1.00");
			this.prezzo_max = 1.00;
		}
	}

	public double getPrezzo_sugg() {
		return prezzo_sugg;
	}

	public void setPrezzo_sugg(double prezzo_sugg) {
		if (prezzo_sugg >= 0) {
			this.prezzo_sugg = prezzo_sugg;
		} else {
			System.out.println("Impossibile impostare un prezzo minore di 0! Default a 1.00");
			this.prezzo_sugg = 1.00;
		}
	}

	public int getQuantita() {
		return quantita;
	}

	public void setQuantita(int quantita) {
		if (quantita >= 0) {
			this.quantita = quantita;
		} else {
			System.out.println("Impossibile impostare un prezzo minore di 0! Default a 1");
			this.quantita = 1;
		}
	}

	public ProdottoDTO(int id, String marca, String modello, String descrizione, String categoria, double prezzo_max,
			double prezzo_sugg, int quantita) {
		super();
		this.id = id;
		this.marca = marca;
		this.modello = modello;
		this.descrizione = descrizione;
		this.categoria = categoria;
		this.prezzo_max = prezzo_max;
		this.prezzo_sugg = prezzo_sugg;
		this.quantita = quantita;
	}
}