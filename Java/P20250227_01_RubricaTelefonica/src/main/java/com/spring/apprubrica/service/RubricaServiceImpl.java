package com.spring.apprubrica.service;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.apprubrica.dao.DAORubriche;
import com.spring.apprubrica.dto.*;
import com.spring.apprubrica.entity.RubricaTelefonica;
import com.spring.apprubrica.utility.RegistroRubriche;
import com.spring.apprubrica.utility.RubricaUtility;

@Service
public class RubricaServiceImpl implements RubricaService {

	@Autowired
	private DAORubriche dao;
	
	/*
	 * 
	Funzionalità relative alle rubriche
	*
	*/

	@Override
	public boolean addRubrica(RubricaTelefonicaDTO rub) {
		RubricaTelefonica entity = RubricaUtility.INRubDTO_OUTRub_NOID(rub);
		RegistroRubriche.addRubrica(entity);
		dao.insert(entity);
		return true;
	}

	@Override
	public boolean removeRubrica(int rub_id) {
		RegistroRubriche.removeRubrica(rub_id);
		dao.delete(rub_id);
		return true;
	}

	@Override
	public RubricaTelefonicaDTO getRubrica(int rub_id) {
		return RubricaUtility.INRub_OUTRubDTO(dao.selectById(rub_id));
	}
	
	public List<RubricaTelefonicaDTO> getAllRubriche() {
		return dao.selectAll()
				  .stream()
				  .map(rubrica -> RubricaUtility.INRub_OUTRubDTO(rubrica))
				  .collect(Collectors.toList());
	}

	@Override
	public RubricaTelefonicaDTO modProprietario(int rub_id, String new_proprietario) {
		RegistroRubriche.modProprietario(rub_id, new_proprietario);
		dao.selectById(rub_id).setProprietario(new_proprietario);
		return getRubrica(rub_id);
	}

	@Override
	public RubricaTelefonicaDTO modAnnoCreazione(int rub_id, int new_anno) {
		RegistroRubriche.modAnnoCreazione(rub_id, new_anno);
		dao.selectById(rub_id).setAnno_creazione(new_anno);
		return getRubrica(rub_id);
	}

	/*
	 * 
	Funzionalità extra relative alle rubriche
	*
	*/
	
	@Override
	public ProprietariTotaliDTO getProprietariTotali() {
		List<String> proprietari = new ArrayList<String>();
		dao.selectAll().forEach(rubrica -> proprietari.add(rubrica.getProprietario()));
		return new ProprietariTotaliDTO(proprietari, proprietari.size());
	}

	@Override
	public RubricaTelefonicaDTO getOldestRubrica() {
		int old_num = Integer.MAX_VALUE;
		RubricaTelefonica old_rubrica = null;
		for (RubricaTelefonica rubrica : dao.selectAll()) {
			if (rubrica.getAnno_creazione() < old_num) {
				old_num = rubrica.getAnno_creazione();
				old_rubrica = rubrica;
			}
		}
		return RubricaUtility.INRub_OUTRubDTO(old_rubrica);
	}

	@Override
	public List<Integer> anniCreazioneCres() {
		return dao.selectAll().stream()
				  .map(RubricaTelefonica::getAnno_creazione)
				  .sorted()
				  .collect(Collectors.toList());
	}

	@Override
	public RubricaPlusDTO getRubricaPlus(int rub_id) {
		return RegistroRubriche.getRubricaPlus(rub_id);
	}

}
