package com.spring.utente.utility;
import com.spring.utente.dto.*;
import com.spring.utente.entity.Utente;

public class UtenteUtility {
	
	public static Utente daUtenteDTOaUtente(UtenteDTO dto) {
		return new Utente(dto.getId(), dto.getNome(), dto.getCognome(), dto.getUsername(), dto.getPassword());
	}

	public static UtenteDTO daUtenteaUtenteDTO(Utente user) {
		return new UtenteDTO(user.getId(), user.getNome(), user.getCognome(), user.getUsername(), user.getPassword());
	}
	
	public static NomeCognomeDTO daUtenteaNomeCognomeDTO(Utente user) {
		return new NomeCognomeDTO(user.getNome(), user.getCognome());
	}
}