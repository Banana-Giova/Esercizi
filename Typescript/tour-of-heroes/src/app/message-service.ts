import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class MessageService {
  messages: string[] = [];

  add(message: string) {
    this.messages.push(message);
    /*
     'push()' è una funzione semplice per inserire qualcosa
     dentro un'array. Ha una complessità computazionale di O(1),
     dunque è molto efficiente.
     Ottimo per aggiungere nuovi messaggi in coda con rapidità.
    */
  }

  clear() {
    this.messages = [];
  }
}