package com.spring.apprubrica.service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.spring.apprubrica.dao.DAORubriche;
import com.spring.apprubrica.dto.*;
import com.spring.apprubrica.entity.RubricaTelefonica;
import com.spring.apprubrica.exception.RubricaNotFoundException;
import com.spring.apprubrica.utility.RegistroRubriche;
import com.spring.apprubrica.utility.RubricaUtility;

@Service
@Transactional
public class RubricaServiceImpl implements RubricaService {

	@Autowired
	private DAORubriche dao;
	@Autowired
	private RegistroRubriche reg_rub;
	
	/*
	 * 
	Funzionalità relative alle rubriche
	*
	*/

	@Override
	public boolean addRubrica(RubricaTelefonicaDTO rub) {
		RubricaTelefonica entity = RubricaUtility.INRubDTO_OUTRub_NOID(rub);
		reg_rub.addRubrica(entity);
		dao.save(entity);
		return true;
	}

	@Override
	public boolean removeRubrica(int rub_id) {
		reg_rub.removeRubrica(rub_id);
		dao.deleteById(rub_id);
		return true;
	}

	@Override
	public RubricaTelefonicaDTO getRubrica(int rub_id) {
		
		Optional<RubricaTelefonica> opt = dao.findAll(rub_id);
		if (opt.isEmpty())
			throw new RubricaNotFoundException("Contatto non presente nel database");
		
		return RubricaUtility.INRub_OUTRubDTO(opt.get());
	}
	
	public List<RubricaTelefonicaDTO> getAllRubriche() {
		return dao.findById()
				  .stream()
				  .map(rubrica -> RubricaUtility.INRub_OUTRubDTO(rubrica))
				  .collect(Collectors.toList());
	}

	@Override
	public RubricaTelefonicaDTO modProprietario(int rub_id, String new_proprietario) {
		reg_rub.modProprietario(rub_id, new_proprietario);
		
		Optional<RubricaTelefonica> opt = dao.findAll(rub_id);
		if (opt.isEmpty())
			throw new RubricaNotFoundException("Contatto non presente nel database");
		opt.get().setProprietario(new_proprietario);
		return getRubrica(rub_id);
	}

	@Override
	public RubricaTelefonicaDTO modAnnoCreazione(int rub_id, int new_anno) {
		reg_rub.modAnnoCreazione(rub_id, new_anno);
		
		Optional<RubricaTelefonica> opt = dao.findAll(rub_id);
		if (opt.isEmpty())
			throw new RubricaNotFoundException("Contatto non presente nel database");
		opt.get().setAnno_creazione(new_anno);
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
		dao.findById().forEach(rubrica -> proprietari.add(rubrica.getProprietario()));
		return new ProprietariTotaliDTO(proprietari, proprietari.size());
	}

	@Override
	public RubricaTelefonicaDTO getOldestRubrica() {
		int old_num = Integer.MAX_VALUE;
		RubricaTelefonica old_rubrica = null;
		for (RubricaTelefonica rubrica : dao.findById()) {
			if (rubrica.getAnno_creazione() < old_num) {
				old_num = rubrica.getAnno_creazione();
				old_rubrica = rubrica;
			}
		}
		return RubricaUtility.INRub_OUTRubDTO(old_rubrica);
	}

	@Override
	public List<Integer> anniCreazioneCres() {
		return dao.findById().stream()
				  .map(RubricaTelefonica::getAnno_creazione)
				  .sorted()
				  .collect(Collectors.toList());
	}

	@Override
	public RubricaPlusDTO getRubricaPlus(int rub_id) {
		return reg_rub.getRubricaPlus(rub_id);
	}

}
