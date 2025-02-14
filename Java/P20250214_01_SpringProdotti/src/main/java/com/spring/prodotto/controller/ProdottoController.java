package com.spring.prodotto.controller;
import com.spring.prodotto.dto.*;
import com.spring.prodotto.service.ProdottoService;
import java.util.List;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path="/prodotti")
public class ProdottoController {
	private ProdottoService service = new ProdottoService();
	
	@PostMapping(path="/registra", consumes="application/json")
	public boolean registra(@RequestBody ProdottoNoIdDTO dto) {
		return service.carica(dto);
	}
	
	@GetMapping(path="/cerca/{idProdotto}", produces="application/json")
	public ProdottoDTO cercaPerId(@PathVariable int idProdotto) {
		return service.cercaPerId(idProdotto);
	}
	
	@GetMapping(path="/cerca/tutti", produces="application/json")
	public List<ProdottoNoIdDTO> mostraTutti() {
		return service.mostraTutti();
	}
	
	@GetMapping(path="/report", produces="application/json")
	public ReportDTO visualizzaReport() {
		return service.visualizzaReport();
	}
}