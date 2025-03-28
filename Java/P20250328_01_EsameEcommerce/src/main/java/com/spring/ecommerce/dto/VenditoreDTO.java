package com.spring.ecommerce.dto;

import java.util.List;

import com.spring.ecommerce.entity.Prodotto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

public class VenditoreDTO {

    private int id;

    @NotNull(message = "Il nome del venditore non può essere nullo.")
    @NotBlank(message = "Il nome del venditore non può essere vuoto.")
    @Size(max = 63, message = "Il nome non può superare i 63 caratteri.")
    private String nome;

    @NotNull(message = "Il cognome del venditore non può essere nullo.")
    @NotBlank(message = "Il cognome del venditore non può essere vuoto.")
    @Size(max = 63, message = "Il cognome non può superare i 63 caratteri.")
    private String cognome;

    @NotNull(message = "L'username del venditore non può essere nullo.")
    @NotBlank(message = "L'username del venditore non può essere vuoto.")
    @Size(max = 31, message = "L'username non può superare i 31 caratteri.")
    private String username;

    @NotNull(message = "La password del venditore non può essere nulla.")
    @NotBlank(message = "La password del venditore non può essere vuota.")
    @Size(min = 8, max = 63, message = "La password deve essere lunga almeno 8 caratteri.")
    private String password;

    @Size(max = 127, message = "La via non può superare i 127 caratteri.")
    private String via;

    @Size(max = 31, message = "La citta non può superare i 31 caratteri.")
    private String citta;
    
    private List<Prodotto> prodotti;

    public VenditoreDTO() {
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
    public String getUsername() {
        return username;
    }
    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }
    public void setPassword(String password) {
        this.password = password;
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
	public List<Prodotto> getProdotti() {
		return prodotti;
	}
	public void setProdotti(List<Prodotto> prodotti) {
		this.prodotti = prodotti;
	}

	public VenditoreDTO(int id,
			@NotNull(message = "Il nome del venditore non può essere nullo.") @NotBlank(message = "Il nome del venditore non può essere vuoto.") @Size(max = 63, message = "Il nome non può superare i 63 caratteri.") String nome,
			@NotNull(message = "Il cognome del venditore non può essere nullo.") @NotBlank(message = "Il cognome del venditore non può essere vuoto.") @Size(max = 63, message = "Il cognome non può superare i 63 caratteri.") String cognome,
			@NotNull(message = "L'username del venditore non può essere nullo.") @NotBlank(message = "L'username del venditore non può essere vuoto.") @Size(max = 31, message = "L'username non può superare i 31 caratteri.") String username,
			@NotNull(message = "La password del venditore non può essere nulla.") @NotBlank(message = "La password del venditore non può essere vuota.") @Size(min = 8, max = 63, message = "La password deve essere lunga almeno 8 caratteri.") String password,
			@Size(max = 127, message = "La via non può superare i 127 caratteri.") String via,
			@Size(max = 31, message = "La citta non può superare i 31 caratteri.") String citta,
			List<Prodotto> prodotti) {
		super();
		this.id = id;
		this.nome = nome;
		this.cognome = cognome;
		this.username = username;
		this.password = password;
		this.via = via;
		this.citta = citta;
		this.prodotti = prodotti;
	}
    
    
}
