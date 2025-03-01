package com.spring.apprubrica.dao;

import java.util.List;
import com.spring.apprubrica.entity.ContattoTelefonico;

public interface DAOContatti {

	public boolean insert(ContattoTelefonico contatto);
	public List<ContattoTelefonico> selectAll();
	public ContattoTelefonico selectById(String con_id);
	public boolean delete(String con_id);
}
