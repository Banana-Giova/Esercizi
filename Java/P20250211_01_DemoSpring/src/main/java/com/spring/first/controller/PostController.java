package com.spring.first.controller;
import java.time.LocalDate;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController //Indica a Spring che dovrà istanziare e gestire questa classe
@RequestMapping(path="/calcolatrice")
public class PostController {
	
	@PostMapping(path="/post_sum")
	public int somma(int n1, int n2) {
		return n1 + n2;
	}
	
	@PostMapping(path="/post_subtract")
	public int sottrazione(int n1, int n2) {
		return n1 - n2;
	}
	
	@PostMapping(path="/post_multiply")
	public int moltiplicazione(int n1, int n2) {
		return n1 * n2;
	}
	
	@PostMapping(path="/post_divide")
	public double divisione(int n1, int n2) {
		return (double)n1 / (double)n2;
	}
	
	@PostMapping(path="/post_lint")
	public int[] divisione(int n1) {
		int[] output = {n1,n1*2,n1*3,n1*4,n1*5};
		return output;
	}
	
	@PostMapping(path="/post_ciora")
	public String divisione(String choice) {
		if (choice.equals("Saluti")) {
			return "Ciao bello de casa";
		} else if (choice.equals("Orario")) {
			return LocalDate.now().toString();
		} else {
			return "Selezione invalida.";
		}
	}
}
