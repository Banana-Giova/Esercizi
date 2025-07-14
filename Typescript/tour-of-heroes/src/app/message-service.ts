import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class MessageService {
  private inbox = new BehaviorSubject<string[]>([]);
  get message$(): Observable<any> {
    return this.inbox.asObservable();
  }
  set message(value:string[]) {
    this.inbox.next(value);
  }

  /*
  add(new_msg:string): void {
    const current_messages = this.inbox.value;
    this.inbox.next([...current_messages, new_msg]);
  }
  */

  clear(): void {
    this.inbox.next([]);
  }
}