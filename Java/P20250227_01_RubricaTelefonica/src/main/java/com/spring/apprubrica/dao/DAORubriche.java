package com.spring.apprubrica.dao;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import com.spring.apprubrica.entity.RubricaTelefonica;

public interface DAORubriche extends JpaRepository<RubricaTelefonica, Integer> {
	
	public <S extends RubricaTelefonica> S save(S rubrica);
	public List<RubricaTelefonica> findById();
	public Optional<RubricaTelefonica> findAll(Integer rub_id);
	public void deleteById(Integer rub_id);
}
