package com.spring.apprubrica.entity;
import java.time.LocalDate;

import org.hibernate.annotations.OnDelete;
import org.hibernate.annotations.OnDeleteAction;

import com.spring.apprubrica.utility.RubricaUtility;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "contatti_telefonici") // Nome della tabella nel database
public class ContattoTelefonico {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) // Autogenerazione del campo ID
    private int id;

//    @Column(name = "rub_id", nullable = false) // La chiave esterna che punta alla rubrica
//    private int rub_id;
    
    @ManyToOne
    @JoinColumn(name = "rubrica")
    @OnDelete(action = OnDeleteAction.CASCADE)
    private RubricaTelefonica rubrica;
    //Mi serve che ogni contatto possa essere associato ad una rubrica, che ad una rubrica possano essere associati più contatti e che se la rubrica viene concellata si cancellano anche i suoi contatti

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

	public RubricaTelefonica getRubrica() {
		return rubrica;
	}

	public void setRub_id(RubricaTelefonica rubrica) {
		this.rubrica = rubrica;
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

	public ContattoTelefonico(RubricaTelefonica rubrica, String nome, String cognome, String numero, String gruppo_appartenza,
			LocalDate data_nascita, Boolean preferito) {
		super();
		this.rubrica = rubrica;
		this.nome = nome;
		this.cognome = cognome;
		this.numero = numero;
		this.gruppo_appartenenza = (gruppo_appartenza != null? gruppo_appartenza : "default");
		this.data_nascita = data_nascita;
		this.preferito = (preferito != null? preferito : false);
		this.contact_id = (nome + cognome).toLowerCase() + RubricaUtility.generateNewContact();
	}
	
	public ContattoTelefonico(RubricaTelefonica rubrica, String nome, String cognome, String numero, String gruppo_appartenza,
			LocalDate data_nascita, Boolean preferito, String contact_id) {
		super();
		this.rubrica = rubrica;
		this.nome = nome;
		this.cognome = cognome;
		this.numero = numero;
		this.gruppo_appartenenza = (gruppo_appartenza != null? gruppo_appartenza : "default");
		this.data_nascita = data_nascita;
		this.preferito = (preferito != null? preferito : false);
		this.contact_id = contact_id;
	}
}
