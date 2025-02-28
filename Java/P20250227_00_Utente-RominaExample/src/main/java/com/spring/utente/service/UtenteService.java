package com.spring.utente.service;

import java.util.List;

import com.spring.utente.dto.NomeCognomeDTO;
import com.spring.utente.dto.UtenteDTO;

public interface UtenteService {
	
	public boolean registra(UtenteDTO dto);
	public UtenteDTO cercaPerId(int id);
	public NomeCognomeDTO getNomeCognome(int id);
	public List<UtenteDTO> mostraTutti();
	public UtenteDTO updatePassword(int idUtente, String password) ;
	public UtenteDTO cancella(int idUtente);

}
