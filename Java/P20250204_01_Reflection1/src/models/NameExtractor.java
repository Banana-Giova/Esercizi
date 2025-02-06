package models;

import java.lang.reflect.Field;

public class NameExtractor {
	public String nameExtractor(Persona to_extract) {
		try {
			Field field = Persona.class.getDeclaredField("nome");
			field.setAccessible(true);
			Object output = field.get(to_extract);
			return (String)output;
		} catch (Exception e) {
			System.out.println("Errore, estrazione fallita.\n" + e);
			return "ERROR";
		}
	}
}
