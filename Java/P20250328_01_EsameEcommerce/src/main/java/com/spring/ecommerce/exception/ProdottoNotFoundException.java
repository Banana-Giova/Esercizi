package com.spring.ecommerce.exception;

public class ProdottoNotFoundException extends RuntimeException {

    private static final long serialVersionUID = 1L;

	public ProdottoNotFoundException(String message) {
        super(message);
    }
}
