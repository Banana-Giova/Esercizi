package com.spring.apprubrica.exception;

public class ContattoNotFoundException extends RuntimeException {
    private static final long serialVersionUID = 1L;

	public ContattoNotFoundException(String message) {
        super(message);
    }
}

