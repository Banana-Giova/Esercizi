package com.spring.ecommerce.service;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.spring.ecommerce.dao.DAOVenditore;
import com.spring.ecommerce.dto.ProdottoDTO;
import com.spring.ecommerce.dto.SuccessDTO;
import com.spring.ecommerce.dto.VenditoreBaseDTO;
import com.spring.ecommerce.dto.VenditoreDTO;
import com.spring.ecommerce.entity.Prodotto;
import com.spring.ecommerce.entity.Venditore;
import com.spring.ecommerce.exception.ProdottoNotFoundException;
import com.spring.ecommerce.exception.VenditoreNotFoundException;
import com.spring.ecommerce.utility.EcommerceUtility;

@Service
@Transactional
public class VenditoreServiceImpl implements VenditoreService {

	@Autowired
	private DAOVenditore dao;
	
	public SuccessDTO insertVend(VenditoreDTO new_vend) {
		Venditore entity = EcommerceUtility.INVendDTO_OutVend(new_vend);
		dao.save(entity);
		String msg = "Venditore creato con successo con ID: " + entity.getId();
		return new SuccessDTO(msg);
	}

	@Override
	public VenditoreDTO getVend(int vend_id) {
		Optional<Venditore> opt = dao.findById(vend_id);
		if (opt.isEmpty())
			throw new VenditoreNotFoundException("Venditore non presente nel database.");
		return EcommerceUtility.INVend_OutVendDTO(opt.get());
	}

	@Override
	public VenditoreBaseDTO getBasicVend(int vend_id) {
		Optional<Venditore> opt = dao.findById(vend_id);
		if (opt.isEmpty())
			throw new VenditoreNotFoundException("Venditore non presente nel database.");
		return EcommerceUtility.INVend_OutBasicVendDTO(opt.get());
	}

	@Override
	public void modifyPassword(int vend_id, String new_password) {
		Optional<Venditore> opt = dao.findById(vend_id);
		if (opt.isEmpty())
			throw new VenditoreNotFoundException("Venditore non presente nel database.");
		opt.get().setPassword(new_password);
	}

	@Override
	public SuccessDTO addProd(int vend_id, ProdottoDTO new_prod) {
		Optional<Venditore> opt = dao.findById(vend_id);
		if (opt.isEmpty())
			throw new VenditoreNotFoundException("Venditore non presente nel database.");
		opt.get().addProdotto(EcommerceUtility.INProdDTO_OutProd(new_prod, opt.get()));
		
		String msg = "Prodotto aggiunto con successo ai prodotti del venditore a ID: " + opt.get().getId();
		return new SuccessDTO(msg);
	}

	@Override
	public void modProdQuant(int vend_id, int prod_id, int quantita) {
		Optional<Venditore> opt_vend = dao.findById(vend_id);
		if (opt_vend.isEmpty())
			throw new VenditoreNotFoundException("Venditore non presente nel database.");
		
		Optional<Prodotto> opt_prod = opt_vend.get().getProdotto(prod_id);
		if (opt_prod.isEmpty())
			throw new ProdottoNotFoundException("Prodotto non presente nel database.");
		
		opt_prod.get().setQuantita(quantita);
	}

}
