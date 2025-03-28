package com.spring.ecommerce.exception;

public class VenditoreNotFoundException extends RuntimeException {

    private static final long serialVersionUID = 1L;

	public VenditoreNotFoundException(String message) {
        super(message);
    }
}
