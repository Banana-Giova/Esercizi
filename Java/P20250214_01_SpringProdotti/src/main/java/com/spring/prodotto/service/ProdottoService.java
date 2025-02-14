package com.spring.prodotto.service;
import java.util.List;
import java.util.stream.Collectors;
import com.spring.prodotto.dao.DAOProdottoMappa;
import com.spring.prodotto.dto.*;
import com.spring.prodotto.entity.Prodotto;
import com.spring.prodotto.utility.ProdottoUtility;

public class ProdottoService {
	private DAOProdottoMappa dao = new DAOProdottoMappa();
	private ReportDTO report = new ReportDTO();
	
	public boolean carica(ProdottoNoIdDTO dto) {
		Prodotto entity = ProdottoUtility.daProdottoNoIdDTOaProdotto(dto);
		report.updateReport(entity);
		return dao.insert(entity);
	}

	public ProdottoDTO cercaPerId(int idProdotto) {
		Prodotto prodotto = dao.selectById(idProdotto);
		if (prodotto != null)
			return ProdottoUtility.daProdottoaProdottoDTO(prodotto);
		return null;
	}
	
	public List<ProdottoNoIdDTO> mostraTutti() {
		List<Prodotto> prodotto_list = dao.selectAll();
		List<ProdottoNoIdDTO> dto_list = prodotto_list.stream()
											      .map(prodotto -> ProdottoUtility.daProdottoaProdottoNoIdDTO(prodotto))
											      .collect(Collectors.toList());
		return dto_list;
	}
	
	public ReportDTO visualizzaReport() {
		return report;
	}
}
