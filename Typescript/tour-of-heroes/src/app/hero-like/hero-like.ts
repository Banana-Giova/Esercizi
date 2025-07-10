import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-hero-like',
  standalone: false,
  templateUrl: './hero-like.html',
  styleUrl: './hero-like.css'
})
export class HeroLike {
  user_like:string = '';

  @Input() hero_name?: string;
  @Output() emettiLike = new EventEmitter<string>();
  /*
   Questo è un decoratore in Angular che si usa per emettere 
   eventi da un componente figlio verso un componente padre. 
   In pratica, serve a far comunicare un componente figlio 
   con il suo genitore, trasmettendo dati o notifiche 
   quando succede qualcosa.

   ATTENZIONE: Un figlio non deve mandare comandi al padre,
               deve solo notificarlo con dei dati, che poi
               il padre saprà come gestire.
  */

  hero_like() {
    if (Number(this.user_like) < 1) {
      this.user_like = '0';
    }
    if (Number(this.user_like) > 10) {
      this.user_like = '10';
    }
    this.emettiLike.emit(this.user_like);
    /*
     Un evento rappresenta un’azione o un cambiamento 
     di stato che può interessare il programma.

     Può essere generato da diverse sorgenti: 
     - Un utente (click, pressione tasti); 
     - Il sistema (caricamento pagina, timer); 
     - Il programma stesso (terminata un’elaborazione, 
       cambiato un dato).

      Si usano per comunicare verso l'alto, così che
      il figlio possa informare il genitore.
      
      L'EventEmitter ci permette di creare eventi personalizzati.
    */
  }
}
