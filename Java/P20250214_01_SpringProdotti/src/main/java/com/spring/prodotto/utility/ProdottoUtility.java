package com.spring.prodotto.utility;
import java.util.ArrayList;
import java.util.List;

import com.spring.prodotto.dto.ProdottoDTO;
import com.spring.prodotto.dto.ProdottoNoIdDTO;
import com.spring.prodotto.entity.Prodotto;

public class ProdottoUtility {
	private static List<Integer> id_list = new ArrayList<Integer>();
	
	public static boolean validateID(Integer new_id) {
		if (id_list.contains(new_id)) {
			return false;
		} else {
			id_list.add(new_id);
			return true;
		}
	}
	
	public static ProdottoDTO daProdottoaProdottoDTO(Prodotto prodotto) {
		return new ProdottoDTO(prodotto.getId(), prodotto.getMarca(), prodotto.getModello(),
							   prodotto.getDescrizione(), prodotto.getCategoria(),
							   prodotto.getPrezzo_max(), prodotto.getPrezzo_sugg(),
							   prodotto.getQuantita());
	}
	
	public static ProdottoNoIdDTO daProdottoaProdottoNoIdDTO(Prodotto prodotto) {
		return new ProdottoNoIdDTO(prodotto.getMarca(), prodotto.getModello(),
							   prodotto.getDescrizione(), prodotto.getCategoria(),
							   prodotto.getPrezzo_max(), prodotto.getPrezzo_sugg(),
							   prodotto.getQuantita());
	}

	public static Prodotto daProdottoDTOaProdotto(ProdottoDTO prodotto, boolean old_id) {
		Prodotto new_prod = new Prodotto(prodotto.getMarca(), prodotto.getModello(),
							prodotto.getDescrizione(), prodotto.getCategoria(),
							prodotto.getPrezzo_max(), prodotto.getPrezzo_sugg(),
							prodotto.getQuantita());
		if (old_id) {
			new_prod.setId(prodotto.getId());
		}
		return new_prod;
	}
	
	public static Prodotto daProdottoNoIdDTOaProdotto(ProdottoNoIdDTO prodotto) {
		Prodotto new_prod = new Prodotto(prodotto.getMarca(), prodotto.getModello(),
							prodotto.getDescrizione(), prodotto.getCategoria(),
							prodotto.getPrezzo_max(), prodotto.getPrezzo_sugg(),
							prodotto.getQuantita());
		return new_prod;
	}
}