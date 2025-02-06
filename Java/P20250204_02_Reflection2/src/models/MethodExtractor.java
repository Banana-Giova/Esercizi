package models;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class MethodExtractor {
	public void methodExtractor(Persona to_extract) {
		try {
			Method method = Persona.class.getDeclaredMethod("printData", null);
			method.setAccessible(true);
			method.invoke(to_extract, null);
		} catch (Exception e) {
			System.out.println("Errore, estrazione fallita.\n" + e);
			System.out.println("ERROR");
		}
	}
}
