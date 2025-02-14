package com.spring.prodotto.dao;
import com.spring.prodotto.entity.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DAOProdottoMappa {
	private Map<Integer, Prodotto> mappa = new HashMap<>();

	public boolean insert(Prodotto prodotto) {
		if (mappa.containsKey(prodotto.getId())) {
			return false;
		} else {
			mappa.put(prodotto.getId(), prodotto);
			return true;
		}
	}

	public List<Prodotto> selectAll() {
		return new ArrayList<>(mappa.values());
	}

	public Prodotto selectById(Integer idProdotto) {
		return mappa.get(idProdotto);
	}

}