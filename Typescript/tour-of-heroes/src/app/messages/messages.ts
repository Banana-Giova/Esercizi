import { Component } from '@angular/core';
import { MessageService } from '../message-service';

@Component({
  selector: 'app-messages',
  standalone: false,
  templateUrl: './messages.html',
  styleUrl: './messages.css'
})
export class Messages {
  constructor(public messageService: MessageService) {}
}
