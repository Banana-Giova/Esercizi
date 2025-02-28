package com.spring.utente.utility;

import com.spring.utente.dto.UtenteDTO;
import com.spring.utente.entity.Utente;

public class Conversioni {

	public static Utente daUtenteDTOAUtente(UtenteDTO dto) {
		return new Utente(dto.getId(), dto.getNome(), dto.getCognome(), dto.getUsername(), dto.getPassword());
	}
	
	public static UtenteDTO daUtenteAUtenteDTO(Utente entity) {
		return new UtenteDTO(entity.getId(), entity.getNome(), entity.getCognome(), entity.getUsername(), entity.getPassword());
	}
}
