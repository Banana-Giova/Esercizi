package com.spring.utente.service;
import java.util.List;
import java.util.stream.Collectors;

import org.springframework.stereotype.Service;

import com.spring.utente.dao.DAOUtenteMappa;
import com.spring.utente.dto.*;
import com.spring.utente.entity.Utente;
import com.spring.utente.utility.UtenteUtility;

@Service
public class UtenteService {
	private DAOUtenteMappa dao = new DAOUtenteMappa();
	
	public boolean  registra(UtenteDTO dto) {
		Utente entity = UtenteUtility.daUtenteDTOaUtente(dto);
		return dao.insert(entity);
	}

	public UtenteDTO cercaPerId(int idUtente) {
		Utente utente = dao.selectById(idUtente);
		if (utente != null)
			return UtenteUtility.daUtenteaUtenteDTO(utente);
		return null;
	}
	
	public List<UtenteDTO> mostraTutti() {
		List<Utente> utente_list = dao.selectAll();
		List<UtenteDTO> dto_list = utente_list.stream()
											  .map(utente -> UtenteUtility.daUtenteaUtenteDTO(utente))
											  .collect(Collectors.toList());
		return dto_list;
	}
	
	public UtenteDTO elimina(Integer idUtente) {
		Utente utente = dao.delete(idUtente);
		if (utente != null)
			return UtenteUtility.daUtenteaUtenteDTO(utente);
		return null;
	}
	
	public boolean modificaPassword(Integer idUtente, String new_password) {
		Utente utente = dao.selectById(idUtente);
		if (utente == null)
			return false;
		utente.setPassword(new_password);
		return true;
	}
	
	public NomeCognomeDTO getNomeCognome(int idUtente) {
		Utente utente = dao.selectById(idUtente);
		if (utente != null)
			return UtenteUtility.daUtenteaNomeCognomeDTO(utente);
		return null;
	}
	
	public ListaNCDTO tuttiNomiCognomi() {
		List<Utente> utente_list = dao.selectAll();
		List<NomeCognomeDTO> ncdto_list = utente_list.stream()
											       .map(utente -> UtenteUtility.daUtenteaNomeCognomeDTO(utente))
											       .collect(Collectors.toList());
		return new ListaNCDTO(dao.selectAll().size(), ncdto_list);
	}
}
