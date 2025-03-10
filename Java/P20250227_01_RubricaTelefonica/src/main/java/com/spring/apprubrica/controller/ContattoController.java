package com.spring.apprubrica.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import com.spring.apprubrica.dto.*;
import com.spring.apprubrica.service.ContattoService;
import com.spring.apprubrica.utility.RubricaUtility;

import jakarta.validation.Valid;

@RestController
@RequestMapping(path="/contatti")
public class ContattoController {

	@Autowired
	private ContattoService service;
	
	/*
	 * 
	Funzionalità per una data rubrica
	*
	*/
	
	@PostMapping(path="/{rub_id}", consumes = "application/json")
	public boolean addContatto(@Valid @PathVariable int rub_id, @RequestBody ContattoTelefonicoDTO con) {
		RubricaUtility.checkContactIntegrity(con, rub_id);
		return service.addContatto(rub_id, con);
	}
	
	@DeleteMapping(path="/{rub_id}/{con_id}")
	public boolean removeContatto(@PathVariable int rub_id, @PathVariable String con_id) {
		return service.removeContatto(rub_id, con_id);
	}
	
	@GetMapping(path="/{rub_id}/{con_id}", produces = MediaType.APPLICATION_JSON_VALUE)
	public ContattoTelefonicoDTO getContatto(@PathVariable int rub_id, @PathVariable String con_id) {
		return service.getContatto(rub_id, con_id);
	}
	
	@PutMapping(path = "/{rub_id}/{con_id}", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
	public ContattoTelefonicoDTO modificaContatto(
								 @PathVariable int rub_id,
								 @PathVariable String con_id,
								 @RequestBody ModificaContattoRequest request) {
		ContattoTelefonicoDTO contatto = service.getContatto(rub_id, con_id);
		
		boolean modificato = false;
		
	    if (request.getNew_nome() != null) {
	        contatto = service.modNomeContatto(rub_id, con_id, request.getNew_nome());
	        modificato = true;
	    }
	    if (request.getNew_cognome() != null) {
	    	contatto = service.modCognomeContatto(rub_id, con_id, request.getNew_cognome());
	    	modificato = true;
	    }
	    if (request.getNew_numero() != null) {
	    	contatto = service.modNumeroContatto(rub_id, con_id, request.getNew_numero());
	    	modificato = true;
	    }
	    if (request.getNew_gruppo() != null) {
	    	contatto = service.modGruppoContatto(rub_id, con_id, request.getNew_gruppo());
	    	modificato = true;
	    }
	    if (request.getNew_date() != null) {
	    	contatto = service.modDataContatto(rub_id, con_id, request.getNew_date());
	    	modificato = true;
	    }
	    if (request.getPref() != null) {
	    	contatto = service.modPrefContatto(rub_id, con_id, request.getPref());
	    	modificato = true;
	    }

	    if (!modificato) {
	        throw new IllegalArgumentException("Nessun campo valido fornito per la modifica!");
	    }

	    return contatto;
	}
	
	/*
	 * 
	Funzionalità extra per una data rubrica
	*
	*/
	
	@GetMapping(path="/{rub_id}/tutti_contatti", produces = MediaType.APPLICATION_JSON_VALUE)
	public List<ContattoTelefonicoDTO> getAllContatti(@PathVariable int rub_id) {
		return service.getAllContatti(rub_id);
	}
	
	@GetMapping(path="/{rub_id}/numero_contatti", produces = MediaType.APPLICATION_JSON_VALUE)
	public int getNumeroContatti(@PathVariable int rub_id) {
		return service.getNumeroContatti(rub_id);
	}
	
	@GetMapping(path="/{rub_id}/contatto_by_numero", produces = MediaType.APPLICATION_JSON_VALUE)
	public ContattoTelefonicoDTO getContattoByNumero(@PathVariable int rub_id, 
													 @RequestParam String numero) {
		return service.getContattoByNumero(rub_id, numero);
	}
	
	@GetMapping(path="/{rub_id}/gruppo_nome_cognome", produces = MediaType.APPLICATION_JSON_VALUE)
	public List<ContattoNomeCognomeDTO> getNomeCognomeGruppo(@PathVariable int rub_id, 
			 												 @RequestParam String gruppo) {
		return service.getNomeCognomeGruppo(rub_id, gruppo);
	}
	
	@GetMapping(path="/{rub_id}/num_contatti_gruppo", produces = MediaType.APPLICATION_JSON_VALUE)
	public int getNumContattiInGruppo(@PathVariable int rub_id, 
			 						  @RequestParam String gruppo) {
		return service.getNumContattiInGruppo(rub_id, gruppo);
	}
	
	@GetMapping(path="/{rub_id}/elimina_gruppo", produces = MediaType.APPLICATION_JSON_VALUE)
	public boolean destroyGroup(@PathVariable int rub_id, 
			  					@RequestParam String gruppo) {
		return service.destroyGroup(rub_id, gruppo);
	}
	
	@GetMapping(path="/{rub_id}/preferiti", produces = MediaType.APPLICATION_JSON_VALUE)
	public List<ContattoTelefonicoDTO> getPreferiti(@PathVariable int rub_id) {
		return service.getPreferiti(rub_id);
	}
}
