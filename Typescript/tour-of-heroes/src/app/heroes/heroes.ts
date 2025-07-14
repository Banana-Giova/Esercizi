import { Component, OnInit } from '@angular/core';
import { Hero } from '../hero';
import { HeroService } from '../hero-service';
import { tap } from 'rxjs';

@Component({ // componente padre di hero-details
  selector: 'app-heroes',
    // Selector => Identificatore del componente
  standalone: false,
  templateUrl: './heroes.html',
  styleUrl: './heroes.css'
})

export class Heroes implements OnInit {
  heroes: Hero[] = [];
  constructor(private heroService: HeroService) {}
  /*
   - Il costruttore è responsabile dell'atto di creazione
     dell'istanza del componente.
   - E' anche responsabile dell'iniezione delle dipendenze
     in questo caso le istanze del servizio eroi e messaggi.
  */
  
  ngOnInit(): void {
    this.getHeroes();
  }
  /*
   Questo è un hook del ciclo di vita del componente:
    - Un hook del ciclo di vita è una funzione speciale che viene
      chiamata automaticamente da Angular in momenti specifici
      durante la vita di un componente o di una direttiva.
    - Uno di questi hook è 'ngOnInit', chiamato da Angular
      UNA SOLA VOLTA, subito dopo che il componente è stato
      inizializzato assieme alle sue proprietà basilari.
  */

  getHeroes(): void {
    this.heroService.getObsHeroes().pipe(
    /*
     pipe() è un metodo che permette di concatenare uno o più 
     operatori RxJS, creando una catena di trasformazioni 
     su uno stream di dati (Observable).
     - Entra un flusso RAW e ne esce uno rifinito.
    */
    tap(heroes => this.heroes = heroes)
    /*
     tap() si occupa di side-effects:
     - Debug
     - Logging
     - Aggiornare status
     - Assegnazioni
     Non modifica i valori di per sé, quello spetta
     a funzioni come map() e filter().

     In questo caso gestisce un'arrow function per
     assegnare l'Observable ricevuto.
    */
    ).subscribe();
    /*
     subscribe() è utilizzato per avviare l'esecuzione
     di un Observable. Ha anche parametri per definire
     cosa fare all'emissione di nuovi valori, quando
     segnala errori e quando termina l'emissione.
     
     Gli Osservabili in RxJS sono naturalmente pigri,
     un flusso d'acqua con un rubinetto chiuso,
     quindi non emettono valori finché non vengono
     sottoscritti, aprendo il flusso.
     Ogni volta che lo si chiama viene aperto un nuovo
     contesto ed un nuovo event listener.
    */
  }

  add(name:string): void {
    this.heroService.addHero(name);
  }
}