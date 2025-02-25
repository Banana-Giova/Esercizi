package com.spring.universita.dao;

import java.util.List;

import com.spring.universita.entity.Studente;

public interface StudentiDAO {
	public boolean insert(Studente studente);

	public List<Studente> selectAll();

	public Studente selectById(String matricola);

	public Studente delete(String matricola);
}
