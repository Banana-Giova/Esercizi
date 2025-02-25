package com.spring.universita.service;
import java.util.Comparator;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;

import com.spring.universita.dto.*;
import com.spring.universita.entity.*;
import com.spring.universita.utility.UniversitaUtility;
import com.spring.universita.dao.ProfessoriDAOImpl;

public class ProfessoriService {
	
	@Autowired
	private ProfessoriDAOImpl dao = new ProfessoriDAOImpl();
	@Autowired
	private MaterieDTO materieDTO = new MaterieDTO();
	
	public boolean iscrivi(ProfessoreDTO dto) {
		Professore entity = UniversitaUtility.fromProfessoreDTOtoProfessore(dto);
		materieDTO.updateMaterie(entity);
		return dao.insert(entity);
	}

	public ProfessoreDTO cercaPerId(String idProf) {
		Professore prof = dao.selectById(idProf);
		if (prof != null)
			return UniversitaUtility.fromProfessoretoProfessoreDTO(prof);
		return null;
	}
	
	public List<ProfessoreDTO> mostraTutti() {
		return UniversitaUtility.daListaProfessoriaListaProfessoriDTO(dao.selectAll());
	}
	
	public boolean modificaIndirizzo(String idProf, String new_materia) {
		Professore prof = dao.selectById(idProf);
		if (prof == null)
			return false;
		prof.setMateria_inse(new_materia);
		return true;
	}
	
	public ProfessoreDTO elimina(String idProf) {
		Professore prof = dao.delete(idProf);
		if (prof != null)
			return UniversitaUtility.fromProfessoretoProfessoreDTO(prof);
		return null;
	}
	
	//Avanzate
	
	public List<ProfessoreDTO> profMateria(String materia) {
		List<Professore> out_list;
		if (materieDTO.isMateriaPresent(materia)) {
			out_list = this.materieDTO.getMappa_materie().get(materia);
			return UniversitaUtility.daListaProfessoriaListaProfessoriDTO(out_list);
		}
		return null;
	}
	
	public List<String> cognomiOrdinati() {
		List<String> out_list = materieDTO.getLista_cognomi();
		out_list.sort(Comparator.naturalOrder());
		return out_list;
	}
	
	@SuppressWarnings("unchecked")
	public List<String> materieInsegnate() {
		return (List<String>) materieDTO.getMappa_materie().keySet();
	}
}
