package com.spring.apprubrica.service;

import java.util.List;

import com.spring.apprubrica.dto.*;

public interface RubricaService {
	
	/*
	 * 
	Funzionalità relative alle rubriche
	*
	*/

	public boolean addRubrica(RubricaTelefonicaDTO rub);
	public boolean removeRubrica(int rub_id);
	public RubricaTelefonicaDTO getRubrica(int rub_id);
	public List<RubricaTelefonicaDTO> getAllRubriche();
	public RubricaTelefonicaDTO modProprietario(int rub_id, String new_proprietario);
	public RubricaTelefonicaDTO modAnnoCreazione(int rub_id, int new_anno);
	
	/*
	 * 
	Funzionalità extra relative alle rubriche
	*
	*/
	
	public ProprietariTotaliDTO getProprietariTotali();
	public RubricaTelefonicaDTO getOldestRubrica();
	public List<Integer> anniCreazioneCres();
	public RubricaPlusDTO getRubricaPlus(int rub_id);
}
