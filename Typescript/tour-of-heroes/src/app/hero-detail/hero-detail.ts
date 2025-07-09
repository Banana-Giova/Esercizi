import { Component, Input } from '@angular/core';
import { Hero } from '../hero';

@Component({ //componente figlio
  selector: 'app-hero-detail',
  standalone: false,
  templateUrl: './hero-detail.html',
  styleUrl: './hero-detail.css'
})

export class HeroDetail {
  @Input() hero?: Hero;
}
