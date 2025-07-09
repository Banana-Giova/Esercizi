import { Component } from '@angular/core';
import { Hero } from '../hero';
import { MockHeroes } from '../mock-heroes';

@Component({
  selector: 'app-heroes',
  standalone: false,
  templateUrl: './heroes.html',
  styleUrl: './heroes.css'
})

export class Heroes {
  heroes = MockHeroes;
}
