package com.spring.ecommerce.service;

import com.spring.ecommerce.dto.ProdottoDTO;
import com.spring.ecommerce.dto.SuccessDTO;
import com.spring.ecommerce.dto.VenditoreBaseDTO;
import com.spring.ecommerce.dto.VenditoreDTO;

public interface VenditoreService {

	public SuccessDTO insertVend(VenditoreDTO new_vend);
	public VenditoreDTO getVend(int vend_id);
	public VenditoreBaseDTO getBasicVend(int vend_id);
	public void modifyPassword(int vend_id, String new_password);
	public SuccessDTO addProd(int vend_id, ProdottoDTO new_prod);
	public void modProdQuant(int vend_id, int prod_id, int quantita);
}
