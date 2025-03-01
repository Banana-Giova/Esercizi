package com.spring.apprubrica.exception;

public class RubricaNotFoundException extends RuntimeException {
    private static final long serialVersionUID = 1L;

	public RubricaNotFoundException(String message) {
        super(message);
    }
}

