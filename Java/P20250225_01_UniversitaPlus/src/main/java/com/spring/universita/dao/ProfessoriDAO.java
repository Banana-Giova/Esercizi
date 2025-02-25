package com.spring.universita.dao;

import java.util.List;

import com.spring.universita.entity.Professore;

public interface ProfessoriDAO {
	public boolean insert(Professore professore);

	public List<Professore> selectAll();

	public Professore selectById(String idProf);

	public Professore delete(String idProf);
}
