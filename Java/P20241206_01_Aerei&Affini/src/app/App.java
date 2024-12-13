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
	
	private Agenzia selectAgenzia() {
		System.out.println("Selezionare il nome della propria agenzia.");
		this.showAgenzie();
		String user_selection = InputChecker.input_reader.nextLine();
		if (this.le_agenzie.containsKey(user_selection)) {
			return this.le_agenzie.get(user_selection);
		} else {
			System.out.println("L'agenzia selezionata non esiste, ritorno al menu principale.");
			return null;
		}
	}
	
	private Aeroporto selectAeroporto() {
		System.out.println("Selezionare il nome del proprio aeroporto.");
		this.showAeroporti();
		String user_selection = InputChecker.input_reader.nextLine();
		if (this.gli_aeroporti.containsKey(user_selection)) {
			return this.gli_aeroporti.get(user_selection);
		} else {
			System.out.println("L'aeroporto selezionato non esiste, ritorno al menu principale.");
			return null;
		}
	}
	
	private CompagniaAerea selectCompagnia() {
		System.out.println("Selezionare il nome della propria compagnia aerea.");
		this.showCompagnie();
		String user_selection = InputChecker.input_reader.nextLine();
		if (this.le_compagnie.containsKey(user_selection)) {
			return this.le_compagnie.get(user_selection);
		} else {
			System.out.println("La compagnia aerea selezionato non esiste, ritorno al menu principale.");
			return null;
		}
	}
	
	private void mainMenu() throws Exception {
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
				 		 + "├──────────────────┴─────────────────┐\n"
						 + "│ 8-9-10-11) Menu per le Interazioni │\n"
				 		 + "├──────────────────────────┬─────────┘\n"
						 + "│ 8) Compagnia + Aeroporto │\n"
				 		 + "│ 9) Compagnia - Aeroporto │\n"
				 		 + "│ 10) Agenzia + Compagnia  │\n"
				 		 + "│ 11) Agenzia - Compagnia  │\n "
				 		 + "├─────────┬────────────────┘\n"
						 + "│ 0) Esci │\n"
				 		 + "└─────────┘");
		int user_choice = InputChecker.intInputWCheck(0,1,2,3,4,5,6,7,8,9,10,11);
		Agenzia curr_agenzia = null;
		Aeroporto curr_aeroporto = null;
		CompagniaAerea curr_compagnia = null;
		switch (user_choice) {
			case 1:
			case 2:
				curr_agenzia = this.selectAgenzia();
				if (curr_agenzia == null) {
					return;
				}
			case 3:
			case 4:
			case 5:
				curr_aeroporto = this.selectAeroporto();
				if (curr_aeroporto == null) {
					return;
				}
			case 6:
			case 7:
				curr_compagnia = this.selectCompagnia();
				if (curr_compagnia == null) {
					return;
				}
			case 8:
			case 9:
				curr_compagnia = this.selectCompagnia();
				if (curr_compagnia == null) {
					return;
				}
				curr_aeroporto = this.selectAeroporto();
				if (curr_aeroporto == null) {
					return;
				}
			case 10:
			case 11:
				curr_agenzia = this.selectAgenzia();
				if (curr_agenzia == null) {
					return;
				}
				curr_compagnia = this.selectCompagnia();
				if (curr_compagnia == null) {
					return;
				}
		}
		try {
			switch (user_choice) {
				case 1:
					ItemCreator.invokeMethodWithInput(curr_agenzia, "prenota_volo");
					return;
				case 2:
					ItemCreator.invokeMethodWithInput(curr_agenzia, "cancella_prenotazione");
					return;
				case 3:
					ItemCreator.invokeMethodWithInput(curr_aeroporto, "imbarcoVolo");
					return;
				case 4:
					ItemCreator.invokeMethodWithInput(curr_aeroporto, "decolloVolo");
					return;
				case 5:
					ItemCreator.invokeMethodWithInput(curr_aeroporto, "atterraggioVolo");
					return;
				case 6:
					ItemCreator.invokeMethodWithInput(curr_compagnia, "crea_aereo");
					return;
				case 7:
					ItemCreator.invokeMethodWithInput(curr_compagnia, "elimina_aereo");
					return;
			}
		} catch (Exception e) {
			System.out.println("Gli input dati hanno ritornato la seguente eccezione:\n " + e + "\nRitorno al menu principale.");
			return;
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
	
	private void creationMenu() throws Exception {
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
				Agenzia curr_agenzia = (Agenzia) ItemCreator.createInstanceFromFields(Agenzia.class);
				this.le_agenzie.put(curr_agenzia.getNome(), curr_agenzia);
			case 2:
				CompagniaAerea curr_comp = (CompagniaAerea) ItemCreator.createInstanceFromFields(CompagniaAerea.class);
				this.le_compagnie.put(curr_comp.getNome(), curr_comp);
			case 3:
				Aeroporto curr_aero = (Aeroporto) ItemCreator.createInstanceFromFields(Aeroporto.class);
				this.gli_aeroporti.put(curr_aero.getNome(), curr_aero);
			case 0:
				return;
		}
	}
	
	public void databaseMenu() throws Exception {
		System.out.println("Si è pregati di selezionare cosa si vuole creare fra le seguenti:\n"
				 		 + "┌──────────────────────────┐\n"
						 + "│ 1-2) Menu per le Agenzie │\n"
				 		 + "├──────────────────────────┴────┐\n"
						 + "│ 1) Mostra Compagnie           │\n"
				 		 + "│ 2) Mostra Prenotazioni Utente │\n"
				 		 + "├───────────────────────────────┴┐\n"
						 + "│ 3-4-5-6) Menu per le Compagnie │\n"
				 		 + "├────────────────────────┬───────┘\n"
						 + "│ 3) Mostra Voli         │\n"
				 		 + "│ 4) Mostra Aeroporti    │\n"
						 + "│ 5) Mostra Aerei        │\n"
				 		 + "│ 6) Mostra Prenotazioni │"
				 		 + "├─────────┬──────────────┘\n"
						 + "│ 0) Esci │\n"
				 		 + "└─────────┘");
		int user_choice = InputChecker.intInputWCheck(0,1,2);
		Agenzia curr_agenzia = null;
		CompagniaAerea curr_compagnia = null;
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
			case 6:
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
		try {
			switch (user_choice) {
				case 1:
					curr_agenzia.mostra_compagnie();
					return;
				case 2:
					ItemCreator.invokeMethodWithInput(curr_agenzia, "mostra_prenotazioni");
					return;
				case 3:
					curr_compagnia.mostra_voli();
					return;
				case 4:
					curr_compagnia.mostra_aeroporti();
					return;
				case 5:
					curr_compagnia.mostra_aerei();
					return;
				case 6:
					curr_compagnia.mostra_tutte_prenotazioni();
					return;
			}
		} catch (Exception e) {
			System.out.println("Gli input dati hanno ritornato la seguente eccezione:\n " + e + "\nRitorno al menu principale.");
			return;
		}
	}
	
	
	public void mainApp() throws Exception {
		System.out.println("Salve, diamo il benvenuto nel servizio gestionale 'Aerei & Affini'!");
		while (true) {
			System.out.println("Si è pregati di selezionare una modalità fra le seguenti:\n"
					 		 + "┌──────────────────┐\n"
							 + "│ 1) Menu Generale │\n"
					 		 + "├──────────────────┴───┐\n"
							 + "│ 2) Menu di Creazione │\n"
					 		 + "├──────────────────────┤\n"
							 + "│ 3) Menu del Database │\n"
					 		 + "├─────────┬────────────┘\n"
							 + "│ 0) Esci │\n"
					 		 + "└─────────┘");
			int user_choice = InputChecker.intInputWCheck(0,1,2);
			switch (user_choice) {
				case 1:
					System.out.println("Apertura del menu generale in corso...\n------------------------\n");
					mainMenu();
				case 2:
					System.out.println("Apertura del menu di creazione in corso...\n------------------------\n");
					creationMenu();
				case 3:
					System.out.println("Apertura del menu del database in corso...\n------------------------\n");
					databaseMenu();
				case 0:
					System.out.println("Grazie per aver scelto Aerei & Affini!");
					InputChecker.closeScanner();
					System.exit(0);
					break;
			}
		}
	}
}
