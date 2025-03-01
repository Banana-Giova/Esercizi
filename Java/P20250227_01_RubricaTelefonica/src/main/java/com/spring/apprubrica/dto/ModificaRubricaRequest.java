package com.spring.apprubrica.dto;

import java.time.Year;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.PositiveOrZero;
import jakarta.validation.constraints.Size;

public class ModificaRubricaRequest {
	
    @Size(max = 50, message = "Il proprietario non può superare i 50 caratteri")
    private String new_proprietario;
	
	@Min(value = 1900, message = "L'anno di creazione deve essere almeno 1900")
	@PositiveOrZero(message = "L'anno deve essere positivo")
    private Integer new_anno;

    public ModificaRubricaRequest() {}

    public String getNew_proprietario() {
        return new_proprietario;
    }

    public void setNew_proprietario(String new_proprietario) {
        this.new_proprietario = new_proprietario;
    }

    public Integer getNew_anno() {
        return new_anno;
    }

    public void setNew_anno(Integer new_anno) {
        if (new_anno != null && new_anno > Year.now().getValue()) {
            throw new IllegalArgumentException("L'anno non può essere maggiore di quello attuale");
        }
        this.new_anno = new_anno;
    }
}
