package com.spring.ecommerce.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

public class PasswordDTO {

	@NotNull(message = "La password del venditore non può essere nulla.")
    @NotBlank(message = "La password del venditore non può essere vuota.")
    @Size(min = 8, max = 63, message = "La password deve essere lunga almeno 8 caratteri.")
    public String password;
	
	public PasswordDTO() {
	}

	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}

	public PasswordDTO(String password) {
		super();
		this.password = password;
	}
}
