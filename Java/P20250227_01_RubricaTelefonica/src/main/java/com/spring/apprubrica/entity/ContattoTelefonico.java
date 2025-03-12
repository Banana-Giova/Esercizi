package com.spring.apprubrica.entity;
import java.time.LocalDate;

import com.spring.apprubrica.utility.RubricaUtility;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "contatti_telefonici") // Nome della tabella nel database
public class ContattoTelefonico {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) // Autogenerazione del campo ID
    private int id;

    @Column(name = "rub_id", nullable = false) // La chiave esterna che punta alla rubrica
    private int rub_id;
    
//    @ManyToOne
//    @JoinColumn(name = "rub_id", insertable = false, updatable = false)
//    private RubricaTelefonica rubrica;

    @Column(name = "nome", nullable = false, length = 50)
    private String nome;

    @Column(name = "cognome", nullable = false, length = 50)
    private String cognome;

    @Column(name = "numero", nullable = false, length = 15)
    private String numero;

    @Column(name = "gruppo_appartenenza", nullable = false, length = 50)
    private String gruppo_appartenenza;

    @Column(name = "data_nascita")
    private LocalDate data_nascita;

    @Column(name = "preferito", nullable = false)
    private boolean preferito;

    @Column(name = "contact_id", nullable = false, unique = true, length = 100)
    private String contact_id;
    
	public ContattoTelefonico() {
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
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

	public String getContact_id() {
		return contact_id;
	}

	public void setContact_id(String contact_id) {
		this.contact_id = contact_id;
	}

	public ContattoTelefonico(int rub_id, String nome, String cognome, String numero, String gruppo_appartenza,
			LocalDate data_nascita, Boolean preferito) {
		super();
		this.id = RubricaUtility.generateNewContact();
		this.rub_id = rub_id;
		this.nome = nome;
		this.cognome = cognome;
		this.numero = numero;
		this.gruppo_appartenenza = (gruppo_appartenza != null? gruppo_appartenza : "default");
		this.data_nascita = data_nascita;
		this.preferito = (preferito != null? preferito : false);
		this.contact_id = (nome + cognome).toLowerCase() + ((Integer)this.id).toString();
	}
	
	public ContattoTelefonico(int id, int rub_id, String nome, String cognome, String numero, String gruppo_appartenza,
			LocalDate data_nascita, Boolean preferito) {
		super();
		this.id = id;
		this.rub_id = rub_id;
		this.nome = nome;
		this.cognome = cognome;
		this.numero = numero;
		this.gruppo_appartenenza = (gruppo_appartenza != null? gruppo_appartenza : "default");
		this.data_nascita = data_nascita;
		this.preferito = (preferito != null? preferito : false);
		this.contact_id = (nome + cognome).toLowerCase() + ((Integer)this.id).toString();
	}
}
