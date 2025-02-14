package com.spring.prodotto.entity;
import com.spring.prodotto.utility.*;
import java.security.SecureRandom;


public class Prodotto {
	
	private int id;
	private String marca, modello, descrizione, categoria;
	private double prezzo_max, prezzo_sugg;
	private int quantita;
	
	public Prodotto() {
	}

	public int getId() {
		return id;
	}
	
	public void setId(int id) {
		this.id = id;
	}
	
	public void setNewId() {
        int length = 8;
		String characters = "123456789";
        
        SecureRandom random = new SecureRandom();
        StringBuilder randomString = new StringBuilder(length);
        
        for (int i = 0; i < length; i++) {
            int randomIndex = random.nextInt(characters.length());
            randomString.append(characters.charAt(randomIndex));
        }
        int new_id = Integer.parseInt(randomString.toString());
        
        if (ProdottoUtility.validateID(new_id)) {
        	this.id = new_id;
        	return;
        } else {
        	this.setNewId();
        }
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
	public Prodotto(String marca, String modello, String descrizione, String categoria, double prezzo_max,
			double prezzo_sugg, int quantita) {
		super();
		this.setNewId();
		this.marca = marca;
		this.modello = modello;
		this.descrizione = descrizione;
		this.categoria = categoria;
		this.setPrezzo_max(prezzo_max);
		this.setPrezzo_sugg(prezzo_sugg);
		this.setQuantita(quantita);;
	}
}