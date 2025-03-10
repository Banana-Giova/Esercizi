package com.spring.apprubrica.exception;

public class ContattoIntegrityErrorException extends RuntimeException {
    private static final long serialVersionUID = 1L;

	public ContattoIntegrityErrorException(String message) {
        super(message);
    }
}