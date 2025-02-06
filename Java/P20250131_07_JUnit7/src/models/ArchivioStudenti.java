package models;
import java.util.*;

public class ArchivioStudenti {
	private List<Studente> archivio_studenti = new ArrayList<Studente>();

	public void addStudente(String nome, String cognome, int age, String matricola) {
		boolean error = false;
		Iterator<Studente> iteratore = this.archivio_studenti.iterator();
		
		while (iteratore.hasNext()) {
			Studente studente = iteratore.next();
			if (studente.getMatricola().equals(matricola)) {
				error = true;
				break;
			}
		}
		
		if (!error) {
			this.archivio_studenti.add(new Studente(nome, cognome, age, matricola));
			System.out.printf("Studente a matricola %s aggiunto!\n", matricola);
		} else {
			System.out.println("Nessuna operazione eseguita!\nEsiste gia' uno studente con tale numero di matricola nell'archivio!");
		}
	}

	public void removeStudente(String matricola) {
		boolean found = false;
		Iterator<Studente> iteratore = this.archivio_studenti.iterator();
		
		while (iteratore.hasNext()) {
			Studente studente = iteratore.next();
			if (studente.getMatricola().equals(matricola)) {
				iteratore.remove();
				System.out.printf("Studente a matricola %s rimosso!\n", matricola);
				found = true;
				break;
			}
		}
        if (!found) {
            System.out.println("Nessuna operazione eseguita!\nNon esistono studenti a tale matricola nell'archivio!");
        }
	}
	
	public void clearStudenti() {
		this.archivio_studenti.clear();
		System.out.println("Tutti gli studenti sono stati eliminati dall'archivio!");
	}
	
	public int numStudenti() {
		return this.archivio_studenti.size();
	}
}
