package com.spring.ecommerce.entity;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;

@Entity
@Table(name = "venditori")
public class Venditore {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;
	
	@Column(name = "nome", nullable = false, length = 63)
	public String nome;
	
	@Column(name = "cognome", nullable = false, length = 63)
	public String cognome;
	
	@Column(name = "password", nullable = false, length = 63)
	public String password;
	
	@Column(name = "username", nullable = false, length = 31, unique = true, updatable = false)
	public String username;
	
	@Column(name = "via", nullable = true, length = 127)
	public String via;
	
	@Column(name = "citta", nullable = true, length = 31)
	public String citta;
	
    @OneToMany(mappedBy = "venditore", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Prodotto> prodotti;
	
	public Venditore() {
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
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getVia() {
		return via;
	}
	public void setVia(String via) {
		this.via = via;
	}
	public String getCitta() {
		return citta;
	}
	public void setCitta(String citta) {
		this.citta = citta;
	}
	public int getId() {
		return id;
	}
	public List<Prodotto> getProdotti() {
		return prodotti;
	}
	
	public void addProdotto(Prodotto prodotto) {
	    prodotti.add(prodotto);
	    prodotto.setVenditore(this);
	}
	public Optional<Prodotto> getProdotto(int prod_id) {
		for (Prodotto prod : prodotti) {
			if (prod.getId() == prod_id) {
				return Optional.of(null);
			}
		}
		return Optional.empty();
	}

	public Venditore(String nome, String cognome, String password, String username, String via, String citta) {
		super();
		this.nome = nome;
		this.cognome = cognome;
		this.password = password;
		this.username = username;
		this.via = via;
		this.citta = citta;
		this.prodotti = new ArrayList<Prodotto>();
	}
}
