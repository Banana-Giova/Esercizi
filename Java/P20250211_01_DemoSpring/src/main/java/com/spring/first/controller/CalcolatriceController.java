package com.spring.first.controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController //Indica a Spring che dovrà istanziare e gestire questa classe
@RequestMapping(path="/calcolatrice")
public class CalcolatriceController {
	
	@GetMapping(path="/sum")
	public int somma(int n1, int n2) {
		return n1 + n2;
	}
	
	@GetMapping(path="/subtract")
	public int sottrazione(int n1, int n2) {
		return n1 - n2;
	}
	
	@GetMapping(path="/multiply")
	public int moltiplicazione(int n1, int n2) {
		return n1 * n2;
	}
	
	@GetMapping(path="/divide")
	public double divisione(int n1, int n2) {
		return (double)n1 / (double)n2;
	}
}
