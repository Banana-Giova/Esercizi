package com.spring.ecommerce.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import com.spring.ecommerce.dto.*;
import com.spring.ecommerce.service.VenditoreService;

import jakarta.validation.Valid;
import jakarta.validation.constraints.Min;

@RestController
@RequestMapping(path="/venditori")
public class EcommerceController {

	@Autowired
	private VenditoreService service;

	@PostMapping(path="", consumes = "application/json", produces = "application/json")
	public SuccessDTO insertVend(@Valid @RequestBody VenditoreDTO vend) {
		return service.insertVend(vend);
	}
	
	@GetMapping(path="/{vend_id}", produces = MediaType.APPLICATION_JSON_VALUE)
	public VenditoreDTO getVend(@PathVariable int vend_id) {
		return service.getVend(vend_id);
	}
	
	@GetMapping(path="/{vend_id}/basic", produces = MediaType.APPLICATION_JSON_VALUE)
	public VenditoreBaseDTO getBasicVend(@PathVariable int vend_id) {
		return service.getBasicVend(vend_id);
	}
	
	@PatchMapping(path="/{vend_id}", consumes = MediaType.APPLICATION_JSON_VALUE)
	public void modifyPassword(@PathVariable int vend_id, @Valid @RequestBody PasswordDTO new_pass) {
		service.modifyPassword(vend_id, new_pass.getPassword());
	}
	
	@PostMapping(path="/{vend_id}/new_prod", consumes = MediaType.APPLICATION_JSON_VALUE)
	public SuccessDTO addProd(@PathVariable int vend_id, @Valid @RequestBody ProdottoDTO new_prod) {
		return service.addProd(vend_id, new_prod);
	}
	
	@PatchMapping(path="/{vend_id}/{prod_id}")
	public void modProdQuant(@PathVariable int vend_id, @PathVariable int prod_id, @RequestParam @Min(1) int new_quantity) {
		service.modProdQuant(vend_id, prod_id, new_quantity);
	}
}
