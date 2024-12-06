package main;

/*
 Realizzare un progetto che simuli
 - un'agenza di viaggi con le funzionalità di prenotazione volo e cancellazione volo
 - un insieme di compagnie aeree dove ognuna esporta i servizi di
 - prenotazione volo
 - cancellazione volo
 verso le agenzie
 e verso gli aeroporti le funzioni di
 - imbarco (implica che i voli non sono più prenotabili)
 - decollo (ora del decollo di uno specifico aereo della compagnia dall'aeroporto che sta inserendo i dati di decollo)
 - atterraggio (ora di atterraggio di un aereo della compagnia dall'aeroporto che sta inserendo i dati di atterraggio)
 
  NB:
   - è sufficiente una sola agenzia
   - le compagnie aeree hanno un menu particolare che gli consente di aggiungere e eliminare aerei (numero di posti)
 Un esempio di sessione di lavoro la seguente:
 Menu Generale
 Menu per agenzia
	 prenotazione
	 disdetta
	 Menu per aeroporto
	 imbarco
	 decollo
	 atterraggio
	 Menu per compagnia aerea
	 crea aereo
	 elimina aereo
 ovviamente la compagnia aerea predispone una lista di voli (da, a, orario, nome aereo) utilizzabile per le prenotazioni e per gli imbarchi, e i voli
 Abbiamo quindi N compagnie aeree e M aeroporti
 Inoltre il menu prevede un comando di termine lavoro che salva su file 
 la situazione globale del sistema (le compagnie aeree con gli aerei, e lo stato delle prenotazioni, decolli, atterraggi e imbarchi)
 All'avvio il programma recupera da file tutti i dati.
 Al termine di un volo, atterraggio, i dati sono archiviati in una lista qassociata ad ogni aeroporto
   
 */

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
