package com.spring.ecommerce.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.RestController;

import com.spring.ecommerce.dto.ErroreDTO;

import java.sql.Timestamp;
import java.util.Arrays;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Logger;

@ControllerAdvice
@RestController
public class GlobalExceptionHandler {

    private static final Logger logger = Logger.getLogger(GlobalExceptionHandler.class.getName());

    private String getCurrentTimestamp() {
        return new Timestamp(System.currentTimeMillis()).toString();
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErroreDTO> handleValidationException(MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(error -> 
            errors.put(error.getField(), error.getDefaultMessage()));
        logger.warning("Errore di validazione: " + ex.getMessage());

        ErroreDTO error_response = new ErroreDTO(
            HttpStatus.BAD_REQUEST.value(),
            getCurrentTimestamp(),
            ex.getMessage(),
            "VALIDATION_ERROR",
            Arrays.toString(ex.getStackTrace()),
            errors
        );
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error_response);
    }

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<ErroreDTO> handleIllegalArgumentException(IllegalArgumentException ex) {
        logger.warning("Parametro illegale: " + ex.getMessage());
        ErroreDTO error_response = new ErroreDTO(
            HttpStatus.BAD_REQUEST.value(),
            getCurrentTimestamp(),
            ex.getMessage(),
            "INVALID_ARGUMENT",
            Arrays.toString(ex.getStackTrace())
        );
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error_response);
    }

    @ExceptionHandler(VenditoreNotFoundException.class)
    public ResponseEntity<ErroreDTO> handleVenditoreaNotFoundException(VenditoreNotFoundException ex) {
        logger.warning("Venditore non trovato: " + ex.getMessage());
        ErroreDTO error_response = new ErroreDTO(
            HttpStatus.NOT_FOUND.value(),
            getCurrentTimestamp(),
            ex.getMessage(),
            "VENDITORE_NOT_FOUND",
            Arrays.toString(ex.getStackTrace())
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error_response);
    }

    @ExceptionHandler(ProdottoNotFoundException.class)
    public ResponseEntity<ErroreDTO> handleProdottooNotFoundException(ProdottoNotFoundException ex) {
        logger.warning("Prodotto non trovato: " + ex.getMessage());
        ErroreDTO error_response = new ErroreDTO(
            HttpStatus.NOT_FOUND.value(),
            getCurrentTimestamp(),
            ex.getMessage(),
            "PRODOTTO_NOT_FOUND",
            Arrays.toString(ex.getStackTrace())
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error_response);
    }

    @ExceptionHandler(NullPointerException.class)
    public ResponseEntity<ErroreDTO> handleNullPointerException(NullPointerException ex) {
        logger.severe("NullPointerException: " + ex.getMessage());
        ErroreDTO error_response = new ErroreDTO(
            HttpStatus.INTERNAL_SERVER_ERROR.value(),
            getCurrentTimestamp(),
            ex.getMessage(),
            "NULL_POINTER",
            Arrays.toString(ex.getStackTrace())
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error_response);
    }

    @ExceptionHandler(IOException.class)
    public ResponseEntity<ErroreDTO> handleIOException(IOException ex) {
        logger.severe("Errore di I/O: " + ex.getMessage());
        ErroreDTO error_response = new ErroreDTO(
            HttpStatus.INTERNAL_SERVER_ERROR.value(),
            getCurrentTimestamp(),
            ex.getMessage(),
            "IO_ERROR",
            Arrays.toString(ex.getStackTrace())
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error_response);
    }

    @ExceptionHandler(RuntimeException.class)
    public ResponseEntity<ErroreDTO> handleRuntimeException(RuntimeException ex) {
        logger.severe("Errore di runtime: " + ex.getMessage());
        ErroreDTO error_response = new ErroreDTO(
            HttpStatus.INTERNAL_SERVER_ERROR.value(),
            getCurrentTimestamp(),
            ex.getMessage(),
            "RUNTIME_ERROR",
            Arrays.toString(ex.getStackTrace())
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error_response);
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErroreDTO> handleGenericException(Exception ex) {
        logger.severe("Errore interno: " + ex.getMessage());
        ErroreDTO error_response = new ErroreDTO(
            HttpStatus.INTERNAL_SERVER_ERROR.value(),
            getCurrentTimestamp(),
            ex.getMessage(),
            "INTERNAL_SERVER_ERROR",
            Arrays.toString(ex.getStackTrace())
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error_response);
    }
}
