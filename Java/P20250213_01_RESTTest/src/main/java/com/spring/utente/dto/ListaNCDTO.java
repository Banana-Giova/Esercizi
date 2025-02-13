package com.spring.utente.dto;
import java.util.List;

public class ListaNCDTO {
	
	private Integer num_ennuple;
	private List<NomeCognomeDTO> ncdto_list;
	
	public ListaNCDTO() {
	}

	public ListaNCDTO(Integer num_ennuple, List<NomeCognomeDTO> ncdto_list) {
		super();
		this.num_ennuple = num_ennuple;
		this.ncdto_list = ncdto_list;
	}

	public Integer getNum_ennuple() {
		return num_ennuple;
	}

	public void setNum_ennuple(Integer num_ennuple) {
		this.num_ennuple = num_ennuple;
	}

	public List<NomeCognomeDTO> getNcdto_list() {
		return ncdto_list;
	}

	public void setNcdto_list(List<NomeCognomeDTO> ncdto_list) {
		this.ncdto_list = ncdto_list;
	}
}
