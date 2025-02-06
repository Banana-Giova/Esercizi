package models;
import java.lang.reflect.*;

public class AnimalExtractor {
	public void animalExtractor() {
		Method[] costruttori = Animale.class.getDeclaredMethods();
		for (Method metodo : costruttori) { 
			System.out.println("Nome metodo: " + metodo.getName() 
							 + ", Modificatori metodo: " + metodo.getModifiers());
		}
		Field[] un_parametri = Animale.class.getFields();
		for (Field parametro : un_parametri) {
			System.out.println("Nome parametro non dichiarato: " + parametro.getName()
							 + ", Modificatori parametro: " + parametro.getModifiers());
		}
		Field[] de_parametri = Animale.class.getDeclaredFields();
		for (Field parametro : de_parametri) {
			System.out.println("Nome parametro dichiarato: " + parametro.getName()
							 + ", Modificatori parametro: " + parametro.getModifiers());
		}
	}
}
