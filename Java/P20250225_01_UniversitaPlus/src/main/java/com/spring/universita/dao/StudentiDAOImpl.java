package com.spring.universita.dao;
import com.spring.universita.entity.Studente;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class StudentiDAOImpl implements StudentiDAO {
	private Map<String, Studente> mappa = new HashMap<>();

	@Override
	public boolean insert(Studente studente) {
		if (mappa.containsKey(studente.getMatricola())) {
			return false;
		} else {
			mappa.put(studente.getMatricola(), studente);
			return true;
		}
	}

	@Override
	public List<Studente> selectAll() {
		return new ArrayList<>(mappa.values());
	}

	@Override
	public Studente selectById(String matricola) {
		return mappa.get(matricola);
	}

	@Override
	public Studente delete(String matricola) {
		if (mappa.containsKey(matricola)) {
			Studente studente = mappa.remove(matricola);
			return studente;
		} else {
			return null;
		}
	}
}