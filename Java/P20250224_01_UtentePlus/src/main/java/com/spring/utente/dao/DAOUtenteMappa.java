package com.spring.utente.dao;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.spring.utente.entity.Utente;

@Repository
public class DAOUtenteMappa {
	private Map<Integer, Utente> mappa = new HashMap<>();

	public boolean insert(Utente utente) {
		if (mappa.containsKey(utente.getId())) {
			return false;
		} else {
			mappa.put(utente.getId(), utente);
			return true;
		}
	}

	public List<Utente> selectAll() {
		return new ArrayList<>(mappa.values());
	}

	public Utente selectById(Integer matricola) {
		return mappa.get(matricola);
	}

	public Utente delete(Integer matricola) {
		if (mappa.containsKey(matricola)) {
			Utente utente = mappa.remove(matricola);
			return utente;
		} else {
			return null;
		}
	}

}