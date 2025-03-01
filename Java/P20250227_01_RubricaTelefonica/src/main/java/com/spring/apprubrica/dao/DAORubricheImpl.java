package com.spring.apprubrica.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.spring.apprubrica.entity.RubricaTelefonica;

@Repository
public class DAORubricheImpl implements DAORubriche {
	
	private Map<Integer, RubricaTelefonica> mappa = new HashMap<>();
	
	@Override
	public boolean insert(RubricaTelefonica rubrica) {
		mappa.put(rubrica.getId(), rubrica);
		return true;
	}

	@Override
	public List<RubricaTelefonica> selectAll() {
		return new ArrayList<>(mappa.values());
	}

	@Override
	public RubricaTelefonica selectById(Integer rub_id) {
		return mappa.get(rub_id);
	}

	@Override
	public boolean delete(Integer rub_id) {
		mappa.remove(rub_id);
		return true;
	}

}
