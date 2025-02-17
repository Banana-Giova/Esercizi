package com.spring.universita.controller;	
import java.util.List;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.spring.universita.dto.ProfessoreDTO;
import com.spring.universita.service.ProfessoriService;
import jakarta.validation.Valid;

@RestController
@RequestMapping(path="/professori")
public class ProfessoriController {

	private ProfessoriService service = new ProfessoriService();
	
	@PostMapping(path="/iscrivi", consumes="application/json")
	public boolean iscrivi(@Valid @RequestBody ProfessoreDTO dto) {
		return service.iscrivi(dto);
	}
	
	@GetMapping(path="/cerca/{idProf}", produces="application/json")
	public ProfessoreDTO cercaPerId(@PathVariable String idProf) {
		return service.cercaPerId(idProf);
	}
	
	@GetMapping(path="/cerca/tutti", produces="application/json")
	public List<ProfessoreDTO> mostraTutti() {
		return service.mostraTutti();
	}
	
	@DeleteMapping(path="/elimina/{idProf}", produces="application/json")
	public ProfessoreDTO elimina(@PathVariable String idProf) {
		return service.elimina(idProf);
	}
	
	@PatchMapping(path="/modifica_indirizzo/{idProf}")
		public boolean modifica_indirizzo(@PathVariable String idProf, String new_materia) {
			return service.modificaIndirizzo(idProf, new_materia);
	}
	
	//Avanzate
	@GetMapping(path="/cerca/prof_materia/{materia}", produces="application/json")
	public List<ProfessoreDTO> profMateria(@PathVariable String materia) {
		return service.profMateria(materia);
	}
	
	@GetMapping(path="/cerca/cognomi_ordinati", produces="application/json")
	public List<String> cognomiOrdinati() {
		return service.cognomiOrdinati();
	}
	
	@GetMapping(path="/cerca/materie_insegnate", produces="application/json")
	public List<String> listaMaterie() {
		return service.materieInsegnate();
	}
	
	
}
