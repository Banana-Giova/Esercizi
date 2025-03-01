package com.spring.apprubrica.dto;
import java.time.LocalDate;

import jakarta.validation.constraints.PastOrPresent;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;

public class ModificaContattoRequest {
    private String con_id;
    
    @Size(max = 50, message = "Il nome non può superare i 50 caratteri")
    private String new_nome;
    
    @Size(max = 50, message = "Il cognome non può superare i 50 caratteri")
    private String new_cognome;
    
    @Pattern(regexp = "^[0-9]{8,15}$", message = "Il numero di telefono deve contenere solo cifre e avere tra 8 e 15 caratteri")
    private String new_numero;

	@Size(max = 50, message = "Il gruppo di appartenenza non può superare i 50 caratteri")
    private String new_gruppo;
    
    @PastOrPresent(message = "La data di nascita non può essere nel futuro")
    private LocalDate new_date;
    private Boolean pref;

    public ModificaContattoRequest() {}

    public String getCon_id() {
        return con_id;
    }

    public void setCon_id(String con_id) {
        this.con_id = con_id;
    }

    public String getNew_nome() {
        return new_nome;
    }

    public void setNew_nome(String new_nome) {
        this.new_nome = new_nome;
    }

    public String getNew_cognome() {
        return new_cognome;
    }

    public void setNew_cognome(String new_cognome) {
        this.new_cognome = new_cognome;
    }

    public String getNew_numero() {
        return new_numero;
    }

    public void setNew_numero(String new_numero) {
        this.new_numero = new_numero;
    }

    public String getNew_gruppo() {
        return new_gruppo;
    }

    public void setNew_gruppo(String new_gruppo) {
        this.new_gruppo = new_gruppo;
    }

    public LocalDate getNew_date() {
        return new_date;
    }

    public void setNew_date(LocalDate new_date) {
        this.new_date = new_date;
    }

    public Boolean getPref() {
        return pref;
    }

    public void setPref(Boolean pref) {
        this.pref = pref;
    }
}
