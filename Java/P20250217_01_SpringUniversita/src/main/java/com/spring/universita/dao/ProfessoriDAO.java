package com.spring.universita.dao;
import com.spring.universita.entity.Professore;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProfessoriDAO {
	private Map<String, Professore> mappa = new HashMap<>();

	public boolean insert(Professore professore) {
		if (mappa.containsKey(professore.getId())) {
			return false;
		} else {
			mappa.put(professore.getId(), professore);
			return true;
		}
	}

	public List<Professore> selectAll() {
		return new ArrayList<>(mappa.values());
	}

	public Professore selectById(String idProf) {
		return mappa.get(idProf);
	}

	public Professore delete(String idProf) {
		if (mappa.containsKey(idProf)) {
			Professore professore = mappa.remove(idProf);
			return professore;
		} else {
			return null;
		}
	}
}