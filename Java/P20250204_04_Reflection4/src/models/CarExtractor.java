package models;

import java.lang.reflect.Method;

public class CarExtractor {
	public void carExtractor() {
		Method[] metodi = Automobile.class.getDeclaredMethods();
		for (Method metodo : metodi) { 
			System.out.println("Nome metodo: " + metodo.getName() 
							 + ", Modificatori metodo: " + metodo.getModifiers());
		}
	}
}
