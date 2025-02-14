package com.spring.prodotto.dto;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import com.spring.prodotto.entity.Prodotto;

public class ReportDTO {
	
	private List<String> desc_prodotti, nomi_out_of_stock;
	private int pezzi_totali, out_of_stock, pezzi_unici;
	private double prezzo_tutti_prod, media_prezzi;
	private Map<String, List<Integer>> id_per_categoria;

	public List<String> getDesc_prodotti() {
		return desc_prodotti;
	}

	public int getPezzi_unici() {
		return pezzi_unici;
	}

	public double getPrezzo_tutti_prod() {
		return prezzo_tutti_prod;
	}

	public List<String> getNomi_out_of_stock() {
		return nomi_out_of_stock;
	}

	public int getPezzi_totali() {
		return pezzi_totali;
	}

	public int getOut_of_stock() {
		return out_of_stock;
	}

	public double getMedia_prezzi() {
		return media_prezzi;
	}

	public Map<String, List<Integer>> getId_per_categoria() {
		return id_per_categoria;
	}
	
	public ReportDTO() {
		this.desc_prodotti = new ArrayList<String>();
		this.nomi_out_of_stock = new ArrayList<String>();
		this.pezzi_totali = 0;
		this.out_of_stock = 0;
		this.prezzo_tutti_prod = 0.0;
		this.media_prezzi = 0.0;
		this.id_per_categoria = new HashMap<String, List<Integer>>();
	}
	
	public void updateReport(Prodotto prodotto) {
		this.pezzi_unici++;
		this.pezzi_totali += prodotto.getQuantita();
		this.prezzo_tutti_prod += prodotto.getPrezzo_sugg();
		this.media_prezzi = this.prezzo_tutti_prod/this.pezzi_unici;
		this.desc_prodotti.add(prodotto.getDescrizione());
		
		if (prodotto.getQuantita() == 0) {
			this.nomi_out_of_stock.add(prodotto.getModello());
			this.out_of_stock++;
		}
		
		if (!this.id_per_categoria.containsKey(prodotto.getCategoria())) {
			List<Integer> temp_list = new ArrayList<Integer>();
			temp_list.add(prodotto.getId());
			this.id_per_categoria.put(prodotto.getCategoria(), temp_list);
		} else {
			this.id_per_categoria.get(prodotto.getCategoria()).add(prodotto.getId());
		}
	}
}
