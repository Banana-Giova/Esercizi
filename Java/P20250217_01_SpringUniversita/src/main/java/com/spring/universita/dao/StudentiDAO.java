package com.spring.universita.dao;
import com.spring.universita.entity.Studente;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class StudentiDAO {
	private Map<String, Studente> mappa = new HashMap<>();

	public boolean insert(Studente studente) {
		if (mappa.containsKey(studente.getMatricola())) {
			return false;
		} else {
			mappa.put(studente.getMatricola(), studente);
			return true;
		}
	}

	public List<Studente> selectAll() {
		return new ArrayList<>(mappa.values());
	}

	public Studente selectById(String matricola) {
		return mappa.get(matricola);
	}

	public Studente delete(String matricola) {
		if (mappa.containsKey(matricola)) {
			Studente studente = mappa.remove(matricola);
			return studente;
		} else {
			return null;
		}
	}
}