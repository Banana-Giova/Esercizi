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
				 		 + "└──────────────────────────┘\n"
						 + "1) Prenotazione\n"
				 		 + "2) Disdetta\n"
				 		 + "┌───────────────────────────────┐\n"
						 + "│ 3-4-5) Menu per gli Aeroporti │\n"
				 		 + "└───────────────────────────────┘\n"
						 + "3) Imbarco\n"
				 		 + "4) Decollo\n"
						 + "5) Atterraggio\n"
				 		 + "┌────────────────────────────┐\n"
						 + "│ 6-7) Menu per le Compagnie │\n"
				 		 + "└────────────────────────────┘\n"
						 + "6) Crea Aereo\n"
				 		 + "7) Elimina Aereo\n"
				 		 + "┌─────────┐\n"
						 + "│ 0) Esci │\n"
				 		 + "└─────────┘");
		int user_choice = InputChecker.intInputWCheck(0,1,2);
		switch (user_choice) {
			case 1:
			case 2:
				return; //select agenzia
			case 3:
			case 4:
			case 5:
				return; //select aeroporto
			case 6:
			case 7:
				return;	//select compagnia
			case 0:
				return;
		}
	}

	private void creationMenu() {
		System.out.println("Si è pregati di selezionare cosa si vuole creare fra le seguenti:\n"
				 		 + "1) Agenzia\n"
				 		 + "2) Compagnia Aerea\n"
				 		 + "3) Aeroporto\n"
				 		 + "0) Esci");
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
							 + "1) Menu generale di gestione con sottomenu\n"
							 + "2) Menu creazione di un'agenzia, una compagnia aerea o un aeroporto\n"
							 + "0) Esci");
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
