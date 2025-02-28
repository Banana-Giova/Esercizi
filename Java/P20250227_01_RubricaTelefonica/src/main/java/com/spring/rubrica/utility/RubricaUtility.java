package com.spring.rubrica.utility;

import com.spring.rubrica.entity.*;
import com.spring.rubrica.dto.*;

public class RubricaUtility {
	public static int reg_key = 0;
	public static int contact_count = 0;

	public static synchronized int generateRegKey() {
		reg_key++;
		return reg_key;
	}
	
	public static synchronized int generateNewContact() {
		contact_count++;
		return contact_count;
	}
	
	public static RubricaTelefonica fromRubricaDTOtoRubrica(RubricaTelefonicaDTO dto) {
		return new RubricaTelefonica(dto.getId(), dto.getProprietario(), dto.getAnno_creazione());
	}
	
	public static RubricaTelefonicaDTO fromRubricatoRubricaDTO(RubricaTelefonica rub) {
		return new RubricaTelefonicaDTO(rub.getId(), rub.getProprietario(), rub.getAnno_creazione());
	}
	
	public static ContattoTelefonico fromContattoDTOtoContatto(ContattoTelefonicoDTO dto) {
		return new ContattoTelefonico(dto.getNome(), dto.getCognome(), dto.getNumero(), dto.getGruppo_appartenza(), dto.getData_nascita(), dto.isPreferito());
	}
	
	public static ContattoTelefonicoDTO fromContattotoContattoDTO(ContattoTelefonico con) {
		return new ContattoTelefonicoDTO(con.getNome(), con.getCognome(), con.getNumero(), con.getGruppo_appartenza(), con.getData_nascita(), con.isPreferito());
	}
	
	public static ContattoNomeCognomeDTO fromContattotoNomeCognomeDTO(ContattoTelefonico con) {
		return new ContattoNomeCognomeDTO(con.getNome(), con.getCognome());
	}
}
