package com.spring.ecommerce.dao;

import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.spring.ecommerce.entity.Venditore;

@Repository
public interface DAOVenditore extends JpaRepository<Venditore, Integer> {
	
	public <S extends Venditore> S save(S venditore);
	public Optional<Venditore> findById(int vend_id);
}