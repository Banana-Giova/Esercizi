package com.spring.universita.service;
import java.util.List;
import java.util.stream.Collectors;

import com.spring.universita.dto.*;
import com.spring.universita.entity.*;
import com.spring.universita.utility.UniversitaUtility;
import com.spring.universita.dao.StudentiDAO;

public class StudentiService {
	private StudentiDAO dao = new StudentiDAO();
	
	public boolean iscrivi(StudenteDTO dto) {
		Studente entity = UniversitaUtility.fromStudenteDTOtoStudente(dto);
		return dao.insert(entity);
	}

	public StudenteDTO cercaPerId(String matricola) {
		Studente studente = dao.selectById(matricola);
		if (studente != null)
			return UniversitaUtility.fromStudentetoStudenteDTO(studente);
		return null;
	}
	
	public List<StudenteDTO> mostraTutti() {
		return UniversitaUtility.daListaStudentiaListaStudentiDTO(dao.selectAll());
	}
	
	public boolean modificaIndirizzo(String matricola, String new_address) {
		Studente studente = dao.selectById(matricola);
		if (studente == null)
			return false;
		studente.setIndirizzo(new_address);
		return true;
	}
	
	public StudenteDTO elimina(String matricola) {
		Studente studente = dao.delete(matricola);
		if (studente != null)
			return UniversitaUtility.fromStudentetoStudenteDTO(studente);
		return null;
	}
	
	//Avanzate
	
	public List<String> tuttiNomiStudenti() {
		List<Studente> student_list = dao.selectAll();
		List<String> names_list = student_list.stream()
									      	  .map(studente -> studente.getNome())
									      	  .collect(Collectors.toList());
		return names_list;
	}
	
	public CognomeAnnoDTO studenteGiovane() {
		CognomeAnnoDTO giovane = new CognomeAnnoDTO("", 0, 0);
		for (Studente studente : dao.selectAll()) {
			if (studente.getAnno_nascita() > giovane.getAnno_nascita())
				giovane.setAll(studente.getCognome(), studente.getAnno_nascita(), studente.getAnno_immatricolazione());
		}
		return giovane;
	}
	
	public CognomeAnnoDTO iscrittoAntico() {
		CognomeAnnoDTO antico = new CognomeAnnoDTO("", 0, 3000);
		for (Studente studente : dao.selectAll()) {
			if (studente.getAnno_immatricolazione() < antico.getAnno_nascita())
				antico.setAll(studente.getCognome(), studente.getAnno_nascita(), studente.getAnno_immatricolazione());
		}
		return antico;
	}
}
