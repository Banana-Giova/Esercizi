import { Component, Input } from '@angular/core';
import { Hero } from '../hero';
import { MessageService } from '../message-service';

@Component({ //componente figlio
  selector: 'app-hero-detail',
  standalone: false,
  templateUrl: './hero-detail.html',
  styleUrl: './hero-detail.css'
})

export class HeroDetail {
  constructor (private messageService: MessageService) {}

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
        this.messageService.add(`HeroDetailComponent: ${this.hero.name} has been rated ${Number(user_like)}`);
        // Funzione di conversione, non casting! 
    }
  }
}