package com.spring.rubrica.dto;

import java.util.ArrayList;
import java.util.HashMap;

import com.spring.rubrica.entity.*;

public class RubricaAndContattiDTO {
    private RubricaTelefonica rubrica;
    private HashMap<String, ContattoTelefonico> contatti;
	private HashMap<String, ArrayList<ContattoTelefonico>> gruppi_appartenenza;

    public RubricaAndContattiDTO() {
    }
    
    public RubricaAndContattiDTO(RubricaTelefonica rubrica) {
        this.rubrica = rubrica;
        this.contatti = new HashMap<String, ContattoTelefonico>();
        this.gruppi_appartenenza = new HashMap<String, ArrayList<ContattoTelefonico>>();
    }

    public RubricaTelefonica getRubrica() {
        return rubrica;
    }

    public HashMap<String, ContattoTelefonico> getContatti() {
        return contatti;
    }
    
	public HashMap<String, ArrayList<ContattoTelefonico>> getGruppi_appartenenza() {
		return gruppi_appartenenza;
	}
    
    public void addContatto(ContattoTelefonico con) {
    	this.contatti.put(con.getContact_id(), con);
    }
    
    public ContattoTelefonico removeContatto(String con_id) {
    	return this.contatti.remove(con_id);
    }
}
