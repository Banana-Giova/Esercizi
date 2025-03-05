package com.spring.apprubrica.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import com.spring.apprubrica.dto.*;
import com.spring.apprubrica.service.RubricaService;

import jakarta.validation.Valid;

@RestController
@RequestMapping(path="/rubriche")
public class RubricaController {

	@Autowired
	private RubricaService service;
	
	/*
	 * 
	Funzionalità relative alle rubriche
	*
	*/

	@PostMapping(path="", consumes = "application/json")
	public boolean addRubrica(@Valid @RequestBody RubricaTelefonicaDTO rub) {
		return service.addRubrica(rub);
	}
	
	@DeleteMapping(path="/{rub_id}")
	public boolean removeRubrica(@PathVariable int rub_id) {
		return service.removeRubrica(rub_id);
	}
	
	@GetMapping(path="/{rub_id}", produces = MediaType.APPLICATION_JSON_VALUE)
	public RubricaTelefonicaDTO getRubrica(@PathVariable int rub_id) {
		return service.getRubrica(rub_id);
	}
	
	@GetMapping(path="", produces = MediaType.APPLICATION_JSON_VALUE)
	public List<RubricaTelefonicaDTO> getAllRubriche() {
		return service.getAllRubriche();
	}
	
	@PutMapping(path = "/{rub_id}", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
	public RubricaTelefonicaDTO modificaRubrica(
								@PathVariable int rub_id, 
								@Valid @RequestBody ModificaRubricaRequest request) {
	    RubricaTelefonicaDTO rubrica = service.getRubrica(rub_id); // Recupera la rubrica prima di modificarla

	    boolean modificato = false;

	    if (request.getNew_proprietario() != null && !request.getNew_proprietario().isBlank()) {
	        rubrica = service.modProprietario(rub_id, request.getNew_proprietario());
	        modificato = true;
	    }
	    if (request.getNew_anno() != null && request.getNew_anno() != 0) {
	        rubrica = service.modAnnoCreazione(rub_id, request.getNew_anno());
	        modificato = true;
	    }

	    if (!modificato) {
	        throw new IllegalArgumentException("Nessun campo valido fornito per la modifica!");
	    }

	    return rubrica;
	}
	
	/*
	 * 
	Funzionalità extra relative alle rubriche
	*
	*/
	
	@GetMapping(path="/proprietari_totali", produces = MediaType.APPLICATION_JSON_VALUE)
	public ProprietariTotaliDTO getProprietariTotali() {
		return service.getProprietariTotali();
	}
	
	@GetMapping(path="/piu_vecchia", produces = MediaType.APPLICATION_JSON_VALUE)
	public RubricaTelefonicaDTO getOldestRubrica() {
		return service.getOldestRubrica();
	}
	
	@GetMapping(path="/anni_creazione", produces = MediaType.APPLICATION_JSON_VALUE)
	public List<Integer> anniCreazioneCres() {
		return service.anniCreazioneCres();
	}
	
	@GetMapping(path="/{rub_id}/plus", produces = MediaType.APPLICATION_JSON_VALUE)
	public RubricaPlusDTO getRubricaPlus(@PathVariable int rub_id) {
		return service.getRubricaPlus(rub_id);
	}
}
