package com.spring.ecommerce.utility;

import com.spring.ecommerce.dto.ProdottoDTO;
import com.spring.ecommerce.dto.VenditoreBaseDTO;
import com.spring.ecommerce.dto.VenditoreDTO;
import com.spring.ecommerce.entity.Prodotto;
import com.spring.ecommerce.entity.Venditore;

public class EcommerceUtility {

	public static Venditore INVendDTO_OutVend(VenditoreDTO dto) {
		return new Venditore(dto.getNome(), dto.getCognome(), dto.getUsername(), dto.getPassword(), dto.getVia(), dto.getCitta());
	}
	public static VenditoreDTO INVend_OutVendDTO(Venditore vend) {
		return new VenditoreDTO(vend.getId(), vend.getNome(), vend.getCognome(), vend.getUsername(), vend.getPassword(), vend.getVia(), vend.getCitta(), vend.getProdotti());
	}
	public static VenditoreBaseDTO INVend_OutBasicVendDTO(Venditore vend) {
		return new VenditoreBaseDTO(vend.getId(), vend.getNome(), vend.getCognome(), vend.getUsername(), vend.getPassword(), vend.getVia(), vend.getCitta());
	}
	
	public static Prodotto INProdDTO_OutProd(ProdottoDTO dto, Venditore vend) {
	    return new Prodotto(dto.getDescrizione(), dto.getQuantita(), dto.getPrezzo(), dto.getSconto(), dto.getCategoria(), vend);
	}
	public static ProdottoDTO INProd_OutProdDTO(Prodotto prod) {
	    return new ProdottoDTO(prod.getId(), prod.getDescrizione(), prod.getQuantita(), prod.getPrezzo(), prod.getSconto(), prod.getCategoria(), prod.getVenditore().getId());
	}

	
}
