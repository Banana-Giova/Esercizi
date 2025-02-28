package com.spring.rubrica.dto;

import com.spring.rubrica.entity.*;
import com.spring.rubrica.utility.*;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class RegistroRubricheDTO {
	
	private HashMap<Integer, RubricaAndContattiDTO> registro_rubriche;

	
	public RegistroRubricheDTO() {
		this.registro_rubriche = new HashMap<Integer, RubricaAndContattiDTO>();
	}
	
	public HashMap<Integer, RubricaAndContattiDTO> getRegistro_rubriche() {
		return registro_rubriche;
	}
	
	/*
	 * 
	Funzionalità relative alle rubriche
	*
	*/

	public void addRubrica(RubricaTelefonica rub) {
		registro_rubriche.put(rub.getId(), new RubricaAndContattiDTO(rub));
	}
	
	public void removeRubrica(int rub_id) {
		registro_rubriche.remove(rub_id);
	}
	
	public RubricaTelefonica getRubrica(int rub_id) {
		return registro_rubriche.get(rub_id).getRubrica();
	}
	
	public RubricaTelefonica modProprietario(int rub_id, String new_proprietario) {
		registro_rubriche.get(rub_id).getRubrica().setProprietario(new_proprietario);
		return registro_rubriche.get(rub_id).getRubrica();
	}
	
	public RubricaTelefonica modAnnoCreazione(int rub_id, int new_anno) {
		registro_rubriche.get(rub_id).getRubrica().setAnno_creazione(new_anno);;
		return registro_rubriche.get(rub_id).getRubrica();
	}
	
	
	
	/*
	 * 
	Funzionalità per una data rubrica
	*
	*/
	
	public void addContatto(int rub_id, ContattoTelefonico con) {
		registro_rubriche.get(rub_id).addContatto(con);
		HashMap<String, ArrayList<ContattoTelefonico>> gruppi_appartenenza = registro_rubriche.get(rub_id).getGruppi_appartenenza();
		
		if (!gruppi_appartenenza.containsKey(con.getGruppo_appartenza()))
			gruppi_appartenenza.put(con.getGruppo_appartenza(), new ArrayList<ContattoTelefonico>());

		gruppi_appartenenza.get(con.getGruppo_appartenza()).add(con);
	}
	
	public void removeContatto(int rub_id, String con_id) {
		ContattoTelefonico rem_con = registro_rubriche.get(rub_id).removeContatto(con_id);
		HashMap<String, ArrayList<ContattoTelefonico>> gruppi_appartenenza = registro_rubriche.get(rub_id).getGruppi_appartenenza();
		gruppi_appartenenza.get(rem_con.getGruppo_appartenza()).removeIf(c -> c.equals(rem_con));
	}
	
	public ContattoTelefonico getContatto(int rub_id, String con_id) {
		return registro_rubriche.get(rub_id).getContatti().get(con_id);
	}
	
	public ContattoTelefonico modNomeContatto(int rub_id, String con_id, String new_nome) {
		getContatto(rub_id, con_id).setNome(new_nome);
		return getContatto(rub_id, con_id);
	}
	
	public ContattoTelefonico modCognomeContatto(int rub_id, String con_id, String new_cognome) {
		getContatto(rub_id, con_id).setCognome(new_cognome);
		return getContatto(rub_id, con_id);
	}
	
	public ContattoTelefonico modNumeroContatto(int rub_id, String con_id, String new_numero) {
		getContatto(rub_id, con_id).setNumero(new_numero);
		return getContatto(rub_id, con_id);
	}
	
	public ContattoTelefonico modGruppoAppartenenza(int rub_id, String con_id, String new_gruppo) {
		getContatto(rub_id, con_id).setGruppo_appartenza(new_gruppo);
		ContattoTelefonico mod_con = getContatto(rub_id, con_id);
		HashMap<String, ArrayList<ContattoTelefonico>> gruppi_appartenenza = registro_rubriche.get(rub_id).getGruppi_appartenenza();
		
		gruppi_appartenenza.get(mod_con.getGruppo_appartenza()).removeIf(c -> c.equals(mod_con));
		if (!gruppi_appartenenza.containsKey(mod_con.getGruppo_appartenza()))
			gruppi_appartenenza.put(mod_con.getGruppo_appartenza(), new ArrayList<ContattoTelefonico>());

		gruppi_appartenenza.get(mod_con.getGruppo_appartenza()).add(mod_con);
		return mod_con;
	}
	
	public ContattoTelefonico modDataNascita(int rub_id, String con_id, LocalDate new_date) {
		getContatto(rub_id, con_id).setData_nascita(new_date);
		return getContatto(rub_id, con_id);
	}
	
	public ContattoTelefonico modPrefContatto(int rub_id, String con_id, boolean pref) {
		getContatto(rub_id, con_id).setPreferito(pref);
		return getContatto(rub_id, con_id);
	}
	
	/*
	 * 
	Funzionalità extra per una data rubrica
	*
	*/
	
	public ArrayList<ContattoTelefonico> getAllContatti(int rub_id) {
		return (ArrayList<ContattoTelefonico>) registro_rubriche.get(rub_id).getContatti().values();
	}
	
	public int getNumeroContatti(int rub_id) {
		return registro_rubriche.get(rub_id).getContatti().values().size();
	}
	
	public ContattoTelefonico getContattoByNumero(int rub_id, String numero) {
		ArrayList<ContattoTelefonico> lista_contatti = getAllContatti(rub_id);
		for (ContattoTelefonico contatto : lista_contatti) {
			if (contatto.getNumero().equals(numero))
				return contatto;
		} return null;
	}
	
	public List<ContattoNomeCognomeDTO> getNomeCognomeGruppo(int rub_id, String gruppo) {
		ArrayList<ContattoTelefonico> contatti_gruppo = 
		registro_rubriche.get(rub_id).getGruppi_appartenenza().get(gruppo);
		
		return contatti_gruppo.stream()
			   .map(contatto -> RubricaUtility.fromContattotoNomeCognomeDTO(contatto))
			   .collect(Collectors.toList());
	}
	
	public int getNumContattiInGruppo(int rub_id, String gruppo) {
		ArrayList<ContattoTelefonico> contatti_gruppo = 
		registro_rubriche.get(rub_id).getGruppi_appartenenza().get(gruppo);
		return contatti_gruppo.size();
	}
}







