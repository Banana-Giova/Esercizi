package main;

import models.*;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		TrovaUtente truant = (lista_utenti) -> {
			ArrayList<Utente> output = new ArrayList<Utente>();
			for (Utente curr_user : lista_utenti) {
				if ((curr_user.getEta() > 40) && curr_user.getResidenza().equals("Roma")) {
					output.add(curr_user);
				}
			}
			return output;
		};
		@SuppressWarnings("serial")
		ArrayList<Utente> utenti = new ArrayList<Utente>() {
			{
				add(new Utente("Paolo", "Rossi", 39, "Roma", "test"));
				add(new Utente("Mario", "Rossi", 40, "Roma", "test"));
				add(new Utente("Antonio", "Di Girolamo", 23, "Roma", "test"));
				add(new Utente("Caterina", "Montefalco", 55, "Roma", "test"));
				add(new Utente("Valeria", "Natelli", 45, "Roma", "test"));
				add(new Utente("Giovanna", "D'Antonelli", 50, "Roma", "test"));
				add(new Utente("Paolo", "Pisani", 21, "Catanzaro", "test"));
				add(new Utente("Laura", "Gambaro", 19, "Roma", "test"));
				add(new Utente("Benedetto", "Satini", 38, "Roma", "test"));
			}
		};
		List<Utente> valid_users = truant.trovautente(utenti);
		Utente curr_user = null;
		for (int i = 0; i < valid_users.size(); i++) {
			curr_user = valid_users.get(i);
			System.out.println(curr_user.getNome() + ", " + curr_user.getCognome() + ", " + curr_user.getEta() + ", "
					+ curr_user.getResidenza() + ", " + curr_user.getTest() + "\n");
		}
	}
}