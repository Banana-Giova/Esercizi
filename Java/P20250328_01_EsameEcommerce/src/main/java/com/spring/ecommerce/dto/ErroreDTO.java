package com.spring.ecommerce.dto;

import java.util.Map;

public class ErroreDTO {

	private int status_code;
	private String timestamp, message, error_type, stack_trace;
	private Map<String, String> multiple_errors;
	
	public ErroreDTO() {
		
	}
	
	public int getStatus_code() {
		return status_code;
	}
	public void setStatus_code(int status_code) {
		this.status_code = status_code;
	}
	public String getTimestamp() {
		return timestamp;
	}
	public void setTimestamp(String timestamp) {
		this.timestamp = timestamp;
	}
	public String getMessage() {
		return message;
	}
	public void setMessage(String message) {
		this.message = message;
	}
	public String getError_type() {
		return error_type;
	}
	public void setError_type(String error_type) {
		this.error_type = error_type;
	}
	public String getPath() {
		return stack_trace;
	}
	public void setPath(String path) {
		this.stack_trace = path;
	}
	public Map<String, String> getMultiple_errors() {
		return multiple_errors;
	}
	public void setMultiple_errors(Map<String, String> multiple_errors) {
		this.multiple_errors = multiple_errors;
	}

	public ErroreDTO(int status_code, String timestamp, String message, String error_type, String path) {
		super();
		this.status_code = status_code;
		this.timestamp = timestamp;
		this.message = message;
		this.error_type = error_type;
		this.stack_trace = path;
	}
	
	public ErroreDTO(int status_code, String timestamp, String message, String error_type, String stack_trace, Map<String, String> multiple_errors) {
		super();
		this.status_code = status_code;
		this.timestamp = timestamp;
		this.message = message;
		this.error_type = error_type;
		this.stack_trace = stack_trace;
		this.multiple_errors = multiple_errors;
	}
}
