package com.spring.universita.dto;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import com.spring.universita.entity.Professore;

public class MaterieDTO {
	private Map<String, List<Professore>> mappa_materie;
	private List<String> lista_cognomi;
	
	public List<String> getLista_cognomi() {
		return lista_cognomi;
	}

	public Map<String, List<Professore>> getMappa_materie() {
		return mappa_materie;
	}

	public MaterieDTO() {
		this.mappa_materie = new HashMap<String, List<Professore>>();
		this.lista_cognomi = new ArrayList<String>();
	}
	
	public void updateMaterie(Professore prof) {
		this.lista_cognomi.add(prof.getCognome());
		if (this.mappa_materie.containsKey(prof.getMateria_inse())) {
			this.mappa_materie.get(prof.getMateria_inse()).add(prof);
		} else {
			ArrayList<Professore> temp_list = new ArrayList<Professore>();
			temp_list.add(prof);
			this.mappa_materie.put(prof.getMateria_inse(), temp_list);
		}
	}
	
	public void eliminaProf(Professore prof) {
		;
	}
	
	public boolean isMateriaPresent(String materia) {
		if (this.mappa_materie.get(materia) != null)
			return true;
		return false;
	}
}
