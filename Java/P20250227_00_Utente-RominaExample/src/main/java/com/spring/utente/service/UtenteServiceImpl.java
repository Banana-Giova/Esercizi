package com.spring.utente.service;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.utente.dao.DAOUtente;
import com.spring.utente.dto.NomeCognomeDTO;
import com.spring.utente.dto.UtenteDTO;
import com.spring.utente.entity.Utente;
import com.spring.utente.utility.Conversioni;

@Service
public class UtenteServiceImpl implements UtenteService{
	
	@Autowired
	private DAOUtente dao;
	
	public boolean registra(UtenteDTO dto) {
		// 1. trasformo il dto in entity
		Utente entity = Conversioni.daUtenteDTOAUtente(dto);
		
		// 2. inserisco l'entity attraverso il dao
		return dao.insert(entity);
	}

	public UtenteDTO cercaPerId(int id) {
		// 1. chiamo il dao
		Utente utente = dao.selectById(id);
		
		if(utente != null) {
			// 2. trasformo
			UtenteDTO dto = Conversioni.daUtenteAUtenteDTO(utente);
			return dto;
		}
		return null;
	}
	
	public NomeCognomeDTO getNomeCognome(int id) {
		Utente utente = dao.selectById(id);
		if(utente != null) {
			return new NomeCognomeDTO(utente.getNome(), utente.getCognome());
		}
		return null;
	}

	public List<UtenteDTO> mostraTutti() {
		List<Utente> lista = dao.selectAll();
		List<UtenteDTO> listaDto = new ArrayList<>();
		for (Utente utente : lista) {
			listaDto.add(Conversioni.daUtenteAUtenteDTO(utente));
		}
		return listaDto;
	}

	public UtenteDTO updatePassword(int idUtente, String password) {
		Utente utente = dao.selectById(idUtente);
		if(utente != null) {
			utente.setPassword(password);
			return Conversioni.daUtenteAUtenteDTO(utente);
		}
		return null;
	}

	public UtenteDTO cancella(int idUtente) {
		Utente utente = dao.selectById(idUtente);
		if(utente != null) {
			dao.delete(idUtente);
			return Conversioni.daUtenteAUtenteDTO(utente);
		}
		return null;
	}
}
