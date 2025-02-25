package com.spring.universita.utility;
import java.util.List;
import java.util.stream.Collectors;

import com.spring.universita.entity.*;
import com.spring.universita.dto.*;

public class UniversitaUtility {
	
	public static StudenteDTO fromStudentetoStudenteDTO(Studente stud) {
		return new StudenteDTO(stud.getMatricola(), stud.getNome(),
							   stud.getCognome(), stud.getIndirizzo(),
							   stud.getAnno_nascita(), stud.getAnno_immatricolazione());
	}
	
	public static Studente fromStudenteDTOtoStudente(StudenteDTO stud) {
		return new Studente(stud.getMatricola(), stud.getNome(),
							stud.getCognome(), stud.getIndirizzo(),
							stud.getAnno_nascita(), stud.getAnno_immatricolazione());

	}
	
	public static ProfessoreDTO fromProfessoretoProfessoreDTO(Professore prof) {
		return new ProfessoreDTO(prof.getId(), prof.getNome(),
								 prof.getCognome(), prof.getMateria_inse());	
	}
	
	public static Professore fromProfessoreDTOtoProfessore(ProfessoreDTO prof) {
		return new Professore(prof.getId(), prof.getNome(),
								 prof.getCognome(), prof.getMateria_inse());	
	}
	
	public static List<StudenteDTO> daListaStudentiaListaStudentiDTO(List<Studente> studente_list) {
		List<StudenteDTO> dto_list = studente_list.stream()
											      .map(studente -> UniversitaUtility.fromStudentetoStudenteDTO(studente))
											      .collect(Collectors.toList());
		return dto_list;
	}
	
	public static List<ProfessoreDTO> daListaProfessoriaListaProfessoriDTO(List<Professore> prof_list) {
		List<ProfessoreDTO> dto_list = prof_list.stream()
											      .map(prof -> UniversitaUtility.fromProfessoretoProfessoreDTO(prof))
											      .collect(Collectors.toList());
		return dto_list;
	}
}
