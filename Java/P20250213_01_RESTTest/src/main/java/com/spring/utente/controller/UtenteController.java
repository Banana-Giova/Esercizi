package com.spring.utente.controller;
import com.spring.utente.dto.*;
import com.spring.utente.service.UtenteService;
import java.util.List;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path="/utenti")
public class UtenteController {
	private UtenteService service = new UtenteService();
	
	@PostMapping(path="/registra", consumes="application/json")
	public boolean registra(@RequestBody UtenteDTO dto) {
		return service.registra(dto);
	}
	
	@GetMapping(path="/cerca/{idUtente}", produces="application/json")
	public UtenteDTO cercaPerId(@PathVariable int idUtente) {
		return service.cercaPerId(idUtente);
	}
	
	@GetMapping(path="/nomeCognome/{idUtente}", produces="application/json")
	public NomeCognomeDTO cercaNomCognome(@PathVariable int idUtente) {
		return service.getNomeCognome(idUtente);
	}
	
	@GetMapping(path="/cerca/tutti", produces="application/json")
	public List<UtenteDTO> mostraTutti() {
		return service.mostraTutti();
	}
	
	@DeleteMapping(path="/elimina/{idUtente}", produces="application/json")
	public UtenteDTO elimina(@PathVariable int idUtente) {
		return service.elimina(idUtente);
	}
	
	@PatchMapping(path="/modifica_password/{idUtente}")
	public boolean elimina(@PathVariable int idUtente, String new_password) {
		return service.modificaPassword(idUtente, new_password);
	}
}