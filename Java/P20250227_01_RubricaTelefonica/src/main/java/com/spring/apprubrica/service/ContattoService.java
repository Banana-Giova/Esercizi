package com.spring.apprubrica.service;

import java.time.LocalDate;
import java.util.List;

import com.spring.apprubrica.dto.ContattoNomeCognomeDTO;
import com.spring.apprubrica.dto.ContattoTelefonicoDTO;

public interface ContattoService {
	
	/*
	 * 
	Funzionalità per una data rubrica
	*
	*/
	
	public boolean addContatto(int rub_id, ContattoTelefonicoDTO con);
	public boolean removeContatto(int rub_id, String con_id);
	public ContattoTelefonicoDTO getContatto(int rub_id, String con_id);
	public ContattoTelefonicoDTO modNomeContatto(int rub_id, String con_id, String new_nome);
	public ContattoTelefonicoDTO modCognomeContatto(int rub_id, String con_id, String new_cognome);
	public ContattoTelefonicoDTO modNumeroContatto(int rub_id, String con_id, String new_numero);
	public ContattoTelefonicoDTO modGruppoContatto(int rub_id, String con_id, String new_gruppo);
	public ContattoTelefonicoDTO modDataContatto(int rub_id, String con_id, LocalDate new_date);
	public ContattoTelefonicoDTO modPrefContatto(int rub_id, String con_id, boolean pref);
	
	/*
	 * 
	Funzionalità extra per una data rubrica
	*
	*/
	
	public List<ContattoTelefonicoDTO> getAllContatti(int rub_id);
	public int getNumeroContatti(int rub_id);
	public ContattoTelefonicoDTO getContattoByNumero(int rub_id, String numero);
	public List<ContattoNomeCognomeDTO> getNomeCognomeGruppo(int rub_id, String gruppo);
	public int getNumContattiInGruppo(int rub_id, String gruppo);
	public boolean destroyGroup(int rub_id, String gruppo);
	public List<ContattoTelefonicoDTO> getPreferiti(int rub_id);
}
