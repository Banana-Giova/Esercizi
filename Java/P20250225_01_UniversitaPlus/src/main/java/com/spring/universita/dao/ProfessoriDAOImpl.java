package com.spring.universita.dao;
import com.spring.universita.entity.Professore;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProfessoriDAOImpl implements ProfessoriDAO {
	private Map<String, Professore> mappa = new HashMap<>();

	@Override
	public boolean insert(Professore professore) {
		if (mappa.containsKey(professore.getId())) {
			return false;
		} else {
			mappa.put(professore.getId(), professore);
			return true;
		}
	}

	@Override
	public List<Professore> selectAll() {
		return new ArrayList<>(mappa.values());
	}

	@Override
	public Professore selectById(String idProf) {
		return mappa.get(idProf);
	}

	@Override
	public Professore delete(String idProf) {
		if (mappa.containsKey(idProf)) {
			Professore professore = mappa.remove(idProf);
			return professore;
		} else {
			return null;
		}
	}
}