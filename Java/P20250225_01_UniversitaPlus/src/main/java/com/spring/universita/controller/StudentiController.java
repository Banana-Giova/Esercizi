package com.spring.universita.controller;	
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.universita.dto.CognomeAnnoDTO;
import com.spring.universita.dto.StudenteDTO;
import com.spring.universita.service.StudentiService;
import jakarta.validation.Valid;

@RestController
@RequestMapping(path="/studenti")
public class StudentiController {

	@Autowired
	private StudentiService service = new StudentiService();
	
	@PostMapping(path="/iscrivi", consumes="application/json")
	public boolean iscrivi(@Valid @RequestBody StudenteDTO dto) {
		return service.iscrivi(dto);
	}
	
	@GetMapping(path="/cerca/{matricola}", produces="application/json")
	public StudenteDTO cercaPerId(@PathVariable String matricola) {
		return service.cercaPerId(matricola);
	}
	
	@GetMapping(path="/cerca/tutti", produces="application/json")
	public List<StudenteDTO> mostraTutti() {
		return service.mostraTutti();
	}
	
	@DeleteMapping(path="/elimina/{matricola}", produces="application/json")
	public StudenteDTO elimina(@PathVariable String matricola) {
		return service.elimina(matricola);
	}
	
	@PatchMapping(path="/modifica_indirizzo/{matricola}")
		public boolean modifica_indirizzo(@PathVariable String matricola, String new_address) {
			return service.modificaIndirizzo(matricola, new_address);
	}
	
	//Avanzate
	@GetMapping(path="/cerca/lista_nomi", produces="application/json")
	public List<String> mostraNomi() {
		return service.tuttiNomiStudenti();
	}
	
	@GetMapping(path="/cerca/studente_piu_giovane", produces="application/json")
	public CognomeAnnoDTO mostraGiovane() {
		return service.studenteGiovane();
	}
	
	@GetMapping(path="/cerca/studente_iscritto_da_piu_tempo", produces="application/json")
	public CognomeAnnoDTO mostraAntico() {
		return service.iscrittoAntico();
	}
	
}
