package main;

import models.NameExtractor;
import models.Persona;

public class Main {

	public static void main(String[] args) {
		Persona mario = new Persona();
		NameExtractor namex = new NameExtractor();
		System.out.println(namex.nameExtractor(mario));
	}

}
