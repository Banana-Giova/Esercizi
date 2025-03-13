package com.spring.apprubrica.service;

import java.time.LocalDate;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.apprubrica.dao.DAOContatti;
import com.spring.apprubrica.dto.ContattoNomeCognomeDTO;
import com.spring.apprubrica.dto.ContattoTelefonicoDTO;
import com.spring.apprubrica.entity.ContattoTelefonico;
import com.spring.apprubrica.utility.RegistroRubriche;
import com.spring.apprubrica.utility.RubricaUtility;

@Service
public class ContattoServiceImpl implements ContattoService {

	@Autowired
	private DAOContatti dao;
	@Autowired
	private RegistroRubriche reg_rub;
	
	/*
	 * 
	Funzionalità per una data rubrica
	*
	*/
	
	@Override
	public boolean addContatto(int rub_id, ContattoTelefonicoDTO con) {
		reg_rub.isRubrica(rub_id);
		ContattoTelefonico entity = RubricaUtility.INConDTO_OUTCon_NOID(con, reg_rub.getRubrica(rub_id));
		reg_rub.addContatto(rub_id, entity);
		dao.insert(entity);
		return true;
	}

	@Override
	public boolean removeContatto(int rub_id, String con_id) {
		reg_rub.removeContatto(rub_id, con_id);
		dao.delete(con_id);
		return true;
	}

	@Override
	public ContattoTelefonicoDTO getContatto(int rub_id, String con_id) {
		reg_rub.isContatto(rub_id, con_id);
		return RubricaUtility.INCon_OUTConDTO(dao.selectById(con_id));
	}

	@Override
	public ContattoTelefonicoDTO modNomeContatto(int rub_id, String con_id, String new_nome) {
		reg_rub.modNomeContatto(rub_id, con_id, new_nome);
		dao.selectById(con_id).setNome(new_nome);
		return getContatto(rub_id, con_id);
	}

	@Override
	public ContattoTelefonicoDTO modCognomeContatto(int rub_id, String con_id, String new_cognome) {
		reg_rub.modCognomeContatto(rub_id, con_id, new_cognome);
		dao.selectById(con_id).setCognome(new_cognome);
		return getContatto(rub_id, con_id);
	}

	@Override
	public ContattoTelefonicoDTO modNumeroContatto(int rub_id, String con_id, String new_numero) {
		reg_rub.modNumeroContatto(rub_id, con_id, new_numero);
		dao.selectById(con_id).setNumero(new_numero);
		return getContatto(rub_id, con_id);
	}

	@Override
	public ContattoTelefonicoDTO modGruppoContatto(int rub_id, String con_id, String new_gruppo) {
		reg_rub.modGruppoContatto(rub_id, con_id, new_gruppo);
		dao.selectById(con_id).setGruppo_appartenenza(new_gruppo);
		return getContatto(rub_id, con_id);
	}

	@Override
	public ContattoTelefonicoDTO modDataContatto(int rub_id, String con_id, LocalDate new_date) {
		reg_rub.modDataContatto(rub_id, con_id, new_date);
		dao.selectById(con_id).setData_nascita(new_date);
		return getContatto(rub_id, con_id);
	}

	@Override
	public ContattoTelefonicoDTO modPrefContatto(int rub_id, String con_id, boolean pref) {
		reg_rub.modPrefContatto(rub_id, con_id, pref);
		dao.selectById(con_id).setPreferito(pref);
		return getContatto(rub_id, con_id);
	}
	
	/*
	 * 
	Funzionalità extra per una data rubrica
	*
	*/
	
	@Override
	public List<ContattoTelefonicoDTO> getAllContatti(int rub_id) {
		return reg_rub.getAllContatti(rub_id);
	}

	@Override
	public int getNumeroContatti(int rub_id) {
		return reg_rub.getNumeroContatti(rub_id);
	}

	@Override
	public ContattoTelefonicoDTO getContattoByNumero(int rub_id, String numero) {
		return reg_rub.getContattoByNumero(rub_id, numero);
	}

	@Override
	public List<ContattoNomeCognomeDTO> getNomeCognomeGruppo(int rub_id, String gruppo) {
		return reg_rub.getNomeCognomeGruppo(rub_id, gruppo);
	}

	@Override
	public int getNumContattiInGruppo(int rub_id, String gruppo) {
		return reg_rub.getNumContattiInGruppo(rub_id, gruppo);
	}

	@Override
	public boolean destroyGroup(int rub_id, String gruppo) {
		return reg_rub.destroyGroup(rub_id, gruppo);
	}

	@Override
	public List<ContattoTelefonicoDTO> getPreferiti(int rub_id) {
		return reg_rub.getPreferiti(rub_id);
	}

}
