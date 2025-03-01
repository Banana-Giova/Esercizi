package com.spring.apprubrica.dao;

import java.util.List;

import com.spring.apprubrica.entity.RubricaTelefonica;

public interface DAORubriche {
	public boolean insert(RubricaTelefonica rubrica);
	public List<RubricaTelefonica> selectAll();
	public RubricaTelefonica selectById(Integer rub_id);
	public boolean delete(Integer rub_id);
}
