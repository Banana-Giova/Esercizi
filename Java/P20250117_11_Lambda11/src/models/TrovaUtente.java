package models;

import java.util.List;

@FunctionalInterface
public interface TrovaUtente {
	List<Utente> trovautente(List<Utente> lista_utenti);
}
