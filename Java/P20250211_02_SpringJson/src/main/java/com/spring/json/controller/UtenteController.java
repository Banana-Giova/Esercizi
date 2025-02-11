package com.spring.json.controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.spring.json.entity.Utente;

@RestController
@RequestMapping(path="/utenti")
public class UtenteController {
	
	@PostMapping(path="/registra", consumes="application/json")
	public boolean registra(@RequestBody Utente utente) {
		//Fake method for testing purposes
		System.out.printf("Utente registrato con successo!\n\n%s", utente.toString());
		return true;
	}
	
	@GetMapping(path="/cerca/{id}", produces="application/json")
	public Utente cercaPerId(@PathVariable int id) {
		//Fake method for testing purposes
		return new Utente(id, "Lorenzo", "Faggi", "Lorenzina", "passwork");
	}
}
