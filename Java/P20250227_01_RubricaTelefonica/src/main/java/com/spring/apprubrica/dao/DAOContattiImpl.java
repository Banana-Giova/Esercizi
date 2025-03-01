package com.spring.apprubrica.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.spring.apprubrica.entity.ContattoTelefonico;

@Repository
public class DAOContattiImpl implements DAOContatti {

	private Map<String, ContattoTelefonico> mappa = new HashMap<>();
	
	@Override
	public boolean insert(ContattoTelefonico contatto) {
		mappa.put(contatto.getContact_id(), contatto);
		return true;
	}

	@Override
	public List<ContattoTelefonico> selectAll() {
		return new ArrayList<>(mappa.values());
	}

	@Override
	public ContattoTelefonico selectById(String con_id) {
		return mappa.get(con_id);
	}

	@Override
	public boolean delete(String con_id) {
		mappa.remove(con_id);
		return true;
	}

}
