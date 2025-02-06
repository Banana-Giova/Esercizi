package main;

import models.MethodExtractor;
import models.Persona;

public class Main {

	public static void main(String[] args) {
		Persona mario = new Persona();
		MethodExtractor namex = new MethodExtractor();
		namex.methodExtractor(mario);
	}

}
