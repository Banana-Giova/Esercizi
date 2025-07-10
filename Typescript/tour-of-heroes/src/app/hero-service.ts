import { Injectable } from '@angular/core';
import { Hero } from './hero';
import { MOCKHEROES } from './mock-heroes';
import { MessageService } from './message-service';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

/*
 Questo decoratore indica ad Angular che la classe 
 HeroService è un servizio che può essere iniettato 
 in altri componenti o servizi. 
*/
@Injectable({
  providedIn: 'root'
})
/*
 Questa configurazione specifica che il servizio 
 deve essere fornito a livello di applicazione. 
 In altre parole, Angular crea una singola istanza di 
 HeroService e la rende disponibile in tutta l'applicazione.
*/

export class HeroService {
  constructor(
    private http: HttpClient,
    private messageService: MessageService
  ) { }

  private heroesUrl = 'mock_heroes.json';

  private log(message: string) {
  this.messageService.add(`HeroService: ${message}`);
  }

  getObsHero(id: number): Observable<Hero> {
    const hero = MOCKHEROES.find(h => h.id === id)!;
    /*
     Il punto esclamativo alla fine è un operatore:
     "non- null assertion". Forza TypeScript a credere
     che il risultato esiste.
    */
    this.log(`fetched hero id=${id}`);
    return of(hero);
  }

  getObsHeroes(): Observable<Hero[]> {
    console.log(this.http.get(this.heroesUrl).subscribe())
    const heroes$ = of(MOCKHEROES);
    /*
     La funzione 'of()' crea un osservabile che
     emette i valori passati come argomenti.
    */
    this.log('fetched heroes')
    return heroes$;
    }
  }
  /*
 - Un Osservabile è un flusso di dati asincrono che
   emette un'array di oggetti Hero.
 - Si utilizza per convenzione il dollaro a fine nome
   per indicare che il metodo ritorna un Osservabile.

  - Quando si dice che un osservabile "emette" 
    un valore, significa che:
    - L'osservabile fornisce un dato agli osservatori sottoscritti.
    - Gli osservatori ricevono e possono reagire a questi dati.

    Questo processo è simile a un flusso continuo di informazioni 
    che gli osservatori possono ascoltare e/o gestire.
*/
