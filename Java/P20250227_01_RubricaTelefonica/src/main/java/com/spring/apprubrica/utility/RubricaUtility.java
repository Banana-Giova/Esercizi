package com.spring.apprubrica.utility;

import com.spring.apprubrica.dto.*;
import com.spring.apprubrica.entity.*;
import com.spring.apprubrica.exception.*;

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
	
	public static RubricaTelefonica INRubDTO_OUTRub(RubricaTelefonicaDTO dto) {
		return new RubricaTelefonica(dto.getId(), dto.getProprietario(), dto.getAnno_creazione());
	}
	
	public static RubricaTelefonica INRubDTO_OUTRub_NOID(RubricaTelefonicaDTO dto) {
		return new RubricaTelefonica(RubricaUtility.generateRegKey(), dto.getProprietario(), dto.getAnno_creazione());
	}
	
	public static RubricaTelefonicaDTO INRub_OUTRubDTO(RubricaTelefonica rub) {
		return new RubricaTelefonicaDTO(rub.getId(), rub.getProprietario(), rub.getAnno_creazione());
	}
	
	public static ContattoTelefonico INConDTO_OUTCon_NOID(ContattoTelefonicoDTO dto) {
		return new ContattoTelefonico(RubricaUtility.generateNewContact(), dto.getRub_id(), dto.getNome(), dto.getCognome(), dto.getNumero(), dto.getGruppo_appartenenza(), dto.getData_nascita(), dto.isPreferito());
	}
	
	public static ContattoTelefonicoDTO INCon_OUTConDTO(ContattoTelefonico con) {
		return new ContattoTelefonicoDTO(con.getRub_id(), con.getContact_id(), con.getNome(), con.getCognome(), con.getNumero(), con.getGruppo_appartenenza(), con.getData_nascita(), con.isPreferito());
	}
	
	public static ContattoNomeCognomeDTO INCon_OUTNomeCognome(ContattoTelefonico con) {
		return new ContattoNomeCognomeDTO(con.getNome(), con.getCognome());
	}
	
	public static RubricaPlusDTO INRub_OUTRubPlusDTO(RubricaTelefonica rub, int num_contatti) {
		return new RubricaPlusDTO(rub.getProprietario(), rub.getAnno_creazione(), num_contatti);
	}
	
	public static void checkContactIntegrity(ContattoTelefonicoDTO dto, int rub_id) {
		if (dto.getRub_id() != rub_id)
			throw new ContattoIntegrityErrorException("Il contatto inviato ha un ID pari a " + dto.getRub_id() + " che differeisce dall'ID dato nell'URL, ovvero " + rub_id);
	}
}
