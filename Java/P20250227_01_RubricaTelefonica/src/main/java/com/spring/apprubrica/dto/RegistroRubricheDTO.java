package com.spring.apprubrica.dto;

import com.spring.apprubrica.dao.DAOContatti;
import com.spring.apprubrica.dao.DAORubriche;
import com.spring.apprubrica.entity.*; 
import com.spring.apprubrica.exception.ContattoNotFoundException;
import com.spring.apprubrica.exception.RubricaNotFoundException;
import com.spring.apprubrica.utility.*;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class RegistroRubricheDTO {
	
	private static HashMap<Integer, RubricaAndContattiDTO> registro_rubriche = new HashMap<Integer, RubricaAndContattiDTO>();
	
	public static HashMap<Integer, RubricaAndContattiDTO> getRegistro_rubriche() {
		return registro_rubriche;
	}
	
	/*
	 * 
	Controlli e utility
	*
	*/
	
	public static void isRubrica(int rub_id) {
	    if (!registro_rubriche.containsKey(rub_id)) {
	        throw new RubricaNotFoundException("Rubrica con ID " + rub_id + " non trovata!");
	    }
	}
	
	public static void isContatto(int rub_id, String con_id) {
		isRubrica(rub_id);
	    if (!registro_rubriche.get(rub_id).getContatti().containsKey(con_id)) {
	        throw new ContattoNotFoundException("Contatto con ID " + con_id + " non trovato nella rubrica " + rub_id);
	    }
	}
	
	public static void updateRegistroRubriche(DAORubriche dao_rub) {
		List<RubricaTelefonica> rub_list = dao_rub.selectAll();
		for (RubricaTelefonica rub : rub_list) {
			addRubrica(rub);
		}
	}
	
	public static void updateRegistroContatti(DAOContatti dao_con) {
		List<ContattoTelefonico> con_list = dao_con.selectAll();
		for (ContattoTelefonico con : con_list) {
			addContatto(con.getRub_id(), con);
		}
	}
	
	/*
	 * 
	Funzionalità relative alle rubriche
	*
	*/

	public static void addRubrica(RubricaTelefonica rub) {
		registro_rubriche.put(rub.getId(), new RubricaAndContattiDTO(rub));
	}
	
	public static void removeRubrica(int rub_id) {
		isRubrica(rub_id);
		registro_rubriche.remove(rub_id);
	}
	
	public static RubricaTelefonica modProprietario(int rub_id, String new_proprietario) {
		isRubrica(rub_id);
		registro_rubriche.get(rub_id).getRubrica().setProprietario(new_proprietario);
		return registro_rubriche.get(rub_id).getRubrica();
	}
	
	public static RubricaTelefonica modAnnoCreazione(int rub_id, int new_anno) {
		isRubrica(rub_id);
		registro_rubriche.get(rub_id).getRubrica().setAnno_creazione(new_anno);;
		return registro_rubriche.get(rub_id).getRubrica();
	}
	
	/*
	 * 
	Funzionalità extra relative alle rubriche
	*
	*/
	
	public static RubricaPlusDTO getRubricaPlus(int rub_id) {
		isRubrica(rub_id);
		int num_contatti = registro_rubriche.get(rub_id).getContatti().values().size();
		return RubricaUtility.INRub_OUTRubPlusDTO(registro_rubriche.get(rub_id).getRubrica(), num_contatti);
	}
	
	/*
	 * 
	Funzionalità per una data rubrica
	*
	*/
	
	public static void addContatto(int rub_id, ContattoTelefonico con) {
		isRubrica(rub_id);
		registro_rubriche.get(rub_id).addContatto(con);
		HashMap<String, ArrayList<ContattoTelefonico>> gruppi_appartenenza = registro_rubriche.get(rub_id)
				.getGruppi_appartenenza();
		if (!gruppi_appartenenza.containsKey(con.getGruppo_appartenenza()))
		    gruppi_appartenenza.put(con.getGruppo_appartenenza(), new ArrayList<ContattoTelefonico>());

		gruppi_appartenenza.get(con.getGruppo_appartenenza()).add(con);

	}
	
	public static boolean removeContatto(int rub_id, String con_id) {
		isContatto(rub_id, con_id);
		ContattoTelefonico rem_con = registro_rubriche.get(rub_id).removeContatto(con_id);
		if (rem_con != null) {
			HashMap<String, ArrayList<ContattoTelefonico>> gruppi_appartenenza = registro_rubriche.get(rub_id).getGruppi_appartenenza();
			gruppi_appartenenza.get(rem_con.getGruppo_appartenenza()).removeIf(c -> c.equals(rem_con));
			return true;
		} return false;
	}
	
	public static ContattoTelefonico getContatto(int rub_id, String con_id) {
		isContatto(rub_id, con_id);
		return registro_rubriche.get(rub_id).getContatti().get(con_id);
	}
	
	public static ContattoTelefonico modNomeContatto(int rub_id, String con_id, String new_nome) {
		isContatto(rub_id, con_id);
		getContatto(rub_id, con_id).setNome(new_nome);
		return getContatto(rub_id, con_id);
	}

	public static ContattoTelefonico modCognomeContatto(int rub_id, String con_id, String new_cognome) {
		isContatto(rub_id, con_id);
		getContatto(rub_id, con_id).setCognome(new_cognome);
		return getContatto(rub_id, con_id);
	}

	public static ContattoTelefonico modNumeroContatto(int rub_id, String con_id, String new_numero) {
		isContatto(rub_id, con_id);
		getContatto(rub_id, con_id).setNumero(new_numero);
		return getContatto(rub_id, con_id);
	}

	public static ContattoTelefonico modGruppoContatto(int rub_id, String con_id, String new_gruppo) {
		isContatto(rub_id, con_id);
		String old_group = getContatto(rub_id, con_id).getGruppo_appartenenza();
		ContattoTelefonico mod_con = getContatto(rub_id, con_id);
		HashMap<String, ArrayList<ContattoTelefonico>> gruppi_appartenenza = registro_rubriche.get(rub_id)
				.getGruppi_appartenenza();

		gruppi_appartenenza.get(old_group).removeIf(c -> c.equals(mod_con));
		
		getContatto(rub_id, con_id).setGruppo_appartenenza(new_gruppo);
		if (!gruppi_appartenenza.containsKey(mod_con.getGruppo_appartenenza()))
			gruppi_appartenenza.put(mod_con.getGruppo_appartenenza(), new ArrayList<ContattoTelefonico>());

		gruppi_appartenenza.get(mod_con.getGruppo_appartenenza()).add(mod_con);
		return mod_con;
	}

	public static ContattoTelefonico modDataContatto(int rub_id, String con_id, LocalDate new_date) {
		isContatto(rub_id, con_id);
		getContatto(rub_id, con_id).setData_nascita(new_date);
		return getContatto(rub_id, con_id);
	}
	
	public static ContattoTelefonico modPrefContatto(int rub_id, String con_id, boolean pref) {
		isContatto(rub_id, con_id);
		getContatto(rub_id, con_id).setPreferito(pref);
		return getContatto(rub_id, con_id);
	}
	
	/*
	 * 
	Funzionalità extra per una data rubrica
	*
	*/
	
	public static List<ContattoTelefonicoDTO> getAllContatti(int rub_id) {
	    isRubrica(rub_id);
	    return registro_rubriche.get(rub_id)
	           .getContatti()
	           .values()
	           .stream()
	           .map(contatto -> RubricaUtility.INCon_OUTConDTO(contatto))
	           .collect(Collectors.toList());
	}
	
	public static int getNumeroContatti(int rub_id) {
		isRubrica(rub_id);
		return registro_rubriche.get(rub_id).getContatti().values().size();
	}
	
	public static ContattoTelefonicoDTO getContattoByNumero(int rub_id, String numero) {
		isRubrica(rub_id);
		Collection<ContattoTelefonico> lista_contatti = registro_rubriche.get(rub_id).getContatti().values();
		for (ContattoTelefonico contatto : lista_contatti) {
			if (contatto.getNumero().equals(numero))
				return RubricaUtility.INCon_OUTConDTO(contatto);
		} return null;
	}
	
	public static List<ContattoNomeCognomeDTO> getNomeCognomeGruppo(int rub_id, String gruppo) {
		isRubrica(rub_id);
		List<ContattoTelefonico> contatti_gruppo = 
		registro_rubriche.get(rub_id).getGruppi_appartenenza().get(gruppo);
		
		return contatti_gruppo.stream()
			   .map(contatto -> RubricaUtility.INCon_OUTNomeCognome(contatto))
			   .collect(Collectors.toList());
	}
	
	public static int getNumContattiInGruppo(int rub_id, String gruppo) {
		isRubrica(rub_id);
		List<ContattoTelefonico> contatti_gruppo = 
		registro_rubriche.get(rub_id).getGruppi_appartenenza().get(gruppo);
		return contatti_gruppo.size();
	}
	
	public static boolean destroyGroup(int rub_id, String gruppo) {
		isRubrica(rub_id);
		if (registro_rubriche.get(rub_id).getGruppi_appartenenza().containsKey(gruppo)) {
			List<ContattoTelefonico> contatti_gruppo = 
			registro_rubriche.get(rub_id).getGruppi_appartenenza().remove(gruppo);
			
			contatti_gruppo.forEach(contatto -> registro_rubriche.get(rub_id).removeContatto(contatto.getContact_id()));
			return true;
		} return false;
	}
	
	public static List<ContattoTelefonicoDTO> getPreferiti(int rub_id) {
		isRubrica(rub_id);
		Collection<ContattoTelefonico> tutti_contatti = registro_rubriche.get(rub_id).getContatti().values();
		return tutti_contatti.stream()
			   .filter(contatto -> contatto.isPreferito())
			   .map(contatto -> RubricaUtility.INCon_OUTConDTO(contatto))
			   .collect(Collectors.toList());
	}
}