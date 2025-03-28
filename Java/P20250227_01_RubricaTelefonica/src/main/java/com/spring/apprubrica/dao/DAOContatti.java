package com.spring.apprubrica.dao;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import com.spring.apprubrica.entity.ContattoTelefonico;

public interface DAOContatti extends JpaRepository<ContattoTelefonico, Integer> {

	public <S extends ContattoTelefonico> S save(S contatto);
	public List<ContattoTelefonico> findAll();
	public Optional<ContattoTelefonico> findById(String con_id);
	public boolean deleteById(String con_id); //should be void
}
