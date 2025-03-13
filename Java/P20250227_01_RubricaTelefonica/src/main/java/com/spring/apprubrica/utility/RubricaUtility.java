package com.spring.apprubrica.utility;

import java.util.Random;

import com.spring.apprubrica.dto.*;
import com.spring.apprubrica.entity.*;
import com.spring.apprubrica.exception.*;

public class RubricaUtility {

	public static synchronized String generateNewContact() {
		Random rng = new Random();
		Integer contact_int = rng.nextInt(9999);
		StringBuilder contact_num = new StringBuilder(((Integer)contact_int).toString());
		while (contact_num.length() < 4) {
			contact_num.insert(0, "0");
		}
		
		return contact_num.toString();
	}
	
	public static RubricaTelefonica INRubDTO_OUTRub(RubricaTelefonicaDTO dto) {
		return new RubricaTelefonica(dto.getId(), dto.getProprietario(), dto.getAnno_creazione());
	}
	
	public static RubricaTelefonica INRubDTO_OUTRub_NOID(RubricaTelefonicaDTO dto) {
		return new RubricaTelefonica(dto.getProprietario(), dto.getAnno_creazione());
	}
	
	public static RubricaTelefonicaDTO INRub_OUTRubDTO(RubricaTelefonica rub) {
		return new RubricaTelefonicaDTO(rub.getId(), rub.getProprietario(), rub.getAnno_creazione());
	}
	
	public static ContattoTelefonico INConDTO_OUTCon_NOID(ContattoTelefonicoDTO dto, RubricaTelefonica rubrica) {
		return new ContattoTelefonico(rubrica, dto.getNome(), dto.getCognome(), dto.getNumero(), dto.getGruppo_appartenenza(), dto.getData_nascita(), dto.isPreferito());
	}
	
	public static ContattoTelefonicoDTO INCon_OUTConDTO(ContattoTelefonico con) {
		return new ContattoTelefonicoDTO(con.getRubrica().getId(), con.getContact_id(), con.getNome(), con.getCognome(), con.getNumero(), con.getGruppo_appartenenza(), con.getData_nascita(), con.isPreferito());
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
