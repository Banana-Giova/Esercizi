package app;
import java.util.*;
import models.*;

public class App implements InputChecker, ItemCreator {

	private Map<String, Agenzia> le_agenzie;
	private Map<String, CompagniaAerea> le_compagnie;
	private Map<String, Aeroporto> gli_aeroporti;
	
	public App() {
		super();
		this.le_agenzie = new HashMap<>();
		this.le_compagnie = new HashMap<>();
		this.gli_aeroporti = new HashMap<>();
	}
	
	private void mainMenu() {
		System.out.println("Si è pregati di selezionare cosa si vuole creare fra le seguenti:\n"
				 		 + "┌──────────────────────────┐\n"
						 + "│ 1-2) Menu per le Agenzie │\n"
				 		 + "├─────────────────┬────────┘\n"
						 + "│ 1) Prenotazione │\n"
				 		 + "│ 2) Disdetta     │\n"
				 		 + "├─────────────────┴─────────────┐\n"
						 + "│ 3-4-5) Menu per gli Aeroporti │\n"
				 		 + "├────────────────┬──────────────┘\n"
						 + "│ 3) Imbarco     │\n"
				 		 + "│ 4) Decollo     │\n"
						 + "│ 5) Atterraggio │\n"
				 		 + "├────────────────┴───────────┐\n"
						 + "│ 6-7) Menu per le Compagnie │\n"
				 		 + "├──────────────────┬─────────┘\n"
						 + "│ 6) Crea Aereo    │\n"
				 		 + "│ 7) Elimina Aereo │\n"
				 		 + "├─────────┬────────┘\n"
						 + "│ 0) Esci │\n"
				 		 + "└─────────┘");
		int user_choice = InputChecker.intInputWCheck(0,1,2);
		Agenzia curr_agenzia;
		Aeroporto curr_aeroporto;
		CompagniaAerea curr_compagnia;
		String user_selection;
		switch (user_choice) {
			case 1:
			case 2:
				System.out.println("Selezionare il nome della propria agenzia.");
				this.showAgenzie();
				user_selection = InputChecker.input_reader.nextLine();
				if (this.le_agenzie.containsKey(user_selection)) {
					curr_agenzia = this.le_agenzie.get(user_selection);
				} else {
					System.out.println("L'agenzia selezionata non esiste, ritorno al menu principale.");
					return;
				}
			case 3:
			case 4:
			case 5:
				System.out.println("Selezionare il nome del proprio aeroporto.");
				this.showAeroporti();
				user_selection = InputChecker.input_reader.nextLine();
				if (this.gli_aeroporti.containsKey(user_selection)) {
					curr_aeroporto = this.gli_aeroporti.get(user_selection);
				} else {
					System.out.println("L'aeroporto selezionato non esiste, ritorno al menu principale.");
					return;
				}
			case 6:
			case 7:
				System.out.println("Selezionare il nome della propria compagnia aerea.");
				this.showCompagnie();
				user_selection = InputChecker.input_reader.nextLine();
				if (this.le_compagnie.containsKey(user_selection)) {
					curr_compagnia = this.le_compagnie.get(user_selection);
				} else {
					System.out.println("La compagnia aerea selezionato non esiste, ritorno al menu principale.");
					return;
				}
			case 0:
				return;
		}
		
		switch (user_choice) {
			case 1:
				return; //prenotazione
			case 2:
				return; //disdetta
			case 3:
				return; //imbarco
			case 4:
				return; //decollo
			case 5:
				return; //atterraggio
			case 6:
				return; //crea aereo
			case 7:
				return; //elimina aereo
		}
	}

	private void showAgenzie() {
		System.out.println("Nomi delle aziende disponibili:");
		for (Map.Entry<String, Agenzia> entry : this.le_agenzie.entrySet()) {
			String ki = entry.getKey();
			System.out.println(" - " + ki);
		}
	}
	
	private void showAeroporti() {
		System.out.println("Nomi degli aeroporti disponibili:");
		for (Map.Entry<String, Aeroporto> entry : this.gli_aeroporti.entrySet()) {
			String ki = entry.getKey();
			System.out.println(" - " + ki);
		}
	}
	
	private void showCompagnie() {
		System.out.println("Nomi delle compagnie disponibili:");
		for (Map.Entry<String, CompagniaAerea> entry : this.le_compagnie.entrySet()) {
			String ki = entry.getKey();
			System.out.println(" - " + ki);
		}
	}
	
	private void creationMenu() {
		System.out.println("Si è pregati di selezionare cosa si vuole creare fra le seguenti:\n"
				 		 + "┌────────────┐\n"
						 + "│ 1) Agenzia │\n"
				 		 + "├────────────┴───────┐\n"
						 + "│ 2) Compagnia Aerea │\n"
				 		 + "├──────────────┬─────┘\n"
						 + "│ 3) Aeroporto │\n"
				 		 + "├─────────┬────┘\n"
						 + "│ 0) Esci │\n"
				 		 + "└─────────┘");
		int user_choice = InputChecker.intInputWCheck(0,1,2,3);
		switch (user_choice) {
			case 1:
				Agenzia curr_agenzia = ItemCreator.createAgenzia();
				this.le_agenzie.put(curr_agenzia.getNome(), curr_agenzia);
			case 2:
				CompagniaAerea curr_comp = ItemCreator.createCompagnia();
				this.le_compagnie.put(curr_comp.getNome(), curr_comp);
			case 3:
				Aeroporto curr_aero = ItemCreator.createAeroporto();
				this.gli_aeroporti.put(curr_aero.getNome(), curr_aero);
			case 0:
				return;
		}
	}
	
	
	public void mainApp() {
		System.out.println("Salve, diamo il benvenuto nel servizio gestionale 'Aerei & Affini'!");
		while (true) {
			System.out.println("Si è pregati di selezionare una modalità fra le seguenti:\n"
					 		 + "┌──────────────────┐\n"
							 + "│ 1) Menu Generale │\n"
					 		 + "├──────────────────┴───┐\n"
							 + "│ 2) Menu di Creazione │\n"
					 		 + "├─────────┬────────────┘\n"
							 + "│ 0) Esci │\n"
					 		 + "└─────────┘");
			int user_choice = InputChecker.intInputWCheck(0,1,2);
			switch (user_choice) {
				case 1:
					mainMenu();
				case 2:
					System.out.println("Apertura del menu di creazione in corso...\n------------------------\n");
					creationMenu();
				case 0:
					System.out.println("Grazie per aver scelto Aerei & Affini!");
					System.exit(0);
					break;
			}
		}
	}
}
