package com.spring.ecommerce.dto;

public class SuccessDTO {

	public String msg, status_code;
	
	public SuccessDTO() {
	}

	public String getMsg() {
		return msg;
	}
	public void setMsg(String msg) {
		this.msg = msg;
	}
	public String getStatus_code() {
		return status_code;
	}
	public void setStatus_code(String status_code) {
		this.status_code = status_code;
	}

	public SuccessDTO(String msg) {
		super();
		this.msg = msg;
		this.status_code = "201";
	}
}
