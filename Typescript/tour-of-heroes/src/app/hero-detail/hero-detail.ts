import { Component, Input } from '@angular/core';
import { Hero } from '../hero';
import { HeroService } from '../hero-service';
import { MessageService } from '../message-service';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { tap } from 'rxjs';

@Component({ //componente figlio
  selector: 'app-hero-detail',
  standalone: false,
  templateUrl: './hero-detail.html',
  styleUrl: './hero-detail.css'
})

export class HeroDetail {
  constructor(
    private route: ActivatedRoute,
    private heroService: HeroService,
    private messageService: MessageService,
    private location: Location
  ) {}

  ngOnInit(): void {
    this.getHero();
  }

  getHero(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.heroService.getObsHero(id).pipe(
    tap(hero => this.hero = hero)
    ).subscribe();
  }
  /*
    this.route:
    - Serve per accedere alle informazioni sulla route corrente, 
      inclusi i parametri, la query string, ecc.
    snapshot:
    - È un oggetto che rappresenta lo stato attuale della route 
      in un dato momento (uno "scatto").
    - È utile quando non vuoi reagire ai cambiamenti, 
      ma solo leggere una volta il valore del parametro.
    param.get('id':
    - paramMap è una mappa di tutti i parametri della route 
      definiti nel tuo routing.
    - Ad esempio, se hai questa configurazione nel tuo app.routes.ts
  */

  @Input() hero?: Hero;
  /*
    Questo è un decoratore Angular.
    Indica che la proprietà hero può ricevere un valore 
    da un componente genitore.

    Serve per stabilire un data binding da parent a child.
    In questo caso si fa uso di Property Binding.

    Il componente padre costruisce il componente figlio
    e decide cosa ascoltare. Dunque passa delle proprietà
    al figlio ed ascolta degli eventi.

    Il figlio può notificare un cambiamento, ma non
    modificare direttamente il dato.
  */

    on_like(user_like:string) {
      if (this.hero) {
        this.hero.likes = Number(user_like);
        this.messageService.message = [`HeroDetailComponent: ${this.hero.name} has been rated ${Number(user_like)}`];
        this.save();
        // Funzione di conversione, non casting! 
        /*
        Quel $ dentro la stringa è una template literal 
        di JavaScript/TypeScript, ed è usato per inserire 
        espressioni dinamiche dentro una stringa in modo 
        semplice e leggibile.
        */
    }
  }

  save(): void {
    if (this.hero) {
      this.heroService.updateHero(this.hero)
        .subscribe(() => window.location.reload())
    }
  }

  delete(): void {
    if (this.hero) {
      this.heroService.deleteHero(this.hero)
        .subscribe(() => this.location.back())
    }
  }


  goBack(): void {
    this.location.back();
  }
}