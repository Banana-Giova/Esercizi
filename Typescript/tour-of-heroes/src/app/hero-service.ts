import { Injectable } from '@angular/core';
import { Hero } from './hero';
import { MessageService } from './message-service';
import { Observable, catchError, of, map, tap } from 'rxjs';
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

  private heroesUrl = 'http://localhost:2400/heroes';
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  private log(message: string) {
    this.messageService.message = [`HeroService: ${message}`];
  }

  private errorLogger(operation = 'operation', error:string) {
      console.error(error);
      this.log(`${operation} failed: ${error}`);
  }

  private handleError<T>(operation = 'operation', result?: T) {
  /*
   "operation" definisce su quale operazione è avvenuto l'errore

   "result" è un fallback in caso di errore, che permette alla 
   funzione proprio di catturare e gestire tali errori 
  */ 
  return (error: any): Observable<T> => {
  /*
   Qui RxJS si aspetta che l'Osservabile emetta un errore
   e quando ciò avviene esso viene catturato, messo come
   parametro della "closure", ovvero questa funzione interna,
   e procede con l'esecuzione della suddetta
  */
    console.error(error);
    // Logga l'errore nella console
    this.log(`${operation} failed: ${error.message}`);
    // Logga l'errore nel Message Service
    return of(result as T);
    // Ritorna un osservabile. Errore soppresso, nuovo osservabile
  };
}

  getObsHeroes(): Observable<Hero[]> {
    const heroes$ = this.http.get<Hero[]>(this.heroesUrl)
    .pipe(catchError(this.handleError<Hero[]>('getHeroes', [])),
    tap(_ => this.log('fetched heroes')));
    /*
     La funzione 'of()' crea un osservabile che
     emette i valori passati come argomenti.
    */
    return heroes$;
    }

  getObsHero(id: number): Observable<Hero> {
    const hero$ = this.http.get<Hero>(`${this.heroesUrl}/${id}`).pipe(
      tap(_ => this.log(`fetched hero id=${id}`)),
      catchError(this.handleError<Hero>(`getHero id=${id}`))
    );
    /*
     Il punto esclamativo alla fine è un operatore:
     "non- null assertion". Forza TypeScript a credere
     che il risultato esiste.

     Il resto è tipo un ciclo:
        Per ogni H, vedi se h.id = id
    */
    return hero$;
  }

  updateHero(hero: Hero): Observable<any> {
    return this.http.put(`${this.heroesUrl}/${hero.id}`, hero, this.httpOptions).pipe(
      tap(_ => this.log(`updated hero id=${hero.id}`)),
      catchError(this.handleError<any>('updateHero'))
    );
  }

  deleteHero(hero: Hero): Observable<any> {
    return this.http.delete(`${this.heroesUrl}/${hero.id}`).pipe(
      tap(_ => this.log(`deleted hero id=${hero.id}`)),
      catchError(this.handleError<any>('deleteHero'))
    );
  }

  addHero(name: string): void {
    let new_name = name.trim();
    if (!new_name) {
      this.errorLogger("Add Hero", "The hero's name can't be undefined!")
      return;
    }

    let lastId:String = '';
    this.getObsHeroes().subscribe(heroes => {
      lastId = String(Number(heroes[heroes.length - 1].id) + 1)
      let new_hero = {
      "id": lastId,
      "name": new_name,
      "likes": 0
      }
      if (lastId == '')
        this.errorLogger("Add Hero", "Error while calculating new ID!")
      this.http.post(this.heroesUrl, new_hero, this.httpOptions)
      .pipe(catchError(this.handleError<any>('addHero')))
      .subscribe(() => {
        window.location.reload();
      });
    });
  }

  searchHeroes(term: string): Observable<Hero[]> {
    if (!term.trim()) {
      return of([]);
    }
    return this.http.get<Hero[]>(`${this.heroesUrl}/?name=${term}`).pipe(
      tap(search_result => search_result.length ?
        this.log(`found heroes matching "${term}"`) :
        this.log(`no heroes matching "${term}"`)),
      catchError(this.handleError<Hero[]>('searchHeroes', []))
    );
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