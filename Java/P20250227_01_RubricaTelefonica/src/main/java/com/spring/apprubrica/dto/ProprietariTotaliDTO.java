package com.spring.apprubrica.dto;

import java.util.List;

public class ProprietariTotaliDTO {
	private List<String> proprietari;
	private int prop_totali;
	
	public List<String> getProprietari() {
		return proprietari;
	}
	public void setProprietari(List<String> proprietari) {
		this.proprietari = proprietari;
	}
	public int getProp_totali() {
		return prop_totali;
	}
	public void setProp_totali(int prop_totali) {
		this.prop_totali = prop_totali;
	}
	public ProprietariTotaliDTO(List<String> proprietari, int prop_totali) {
		super();
		this.proprietari = proprietari;
		this.prop_totali = prop_totali;
	}
}
