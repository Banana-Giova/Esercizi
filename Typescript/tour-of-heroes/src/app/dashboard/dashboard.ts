import { Component, OnInit } from '@angular/core';
import { Hero } from '../hero';
import { HeroService } from '../hero-service';
import { tap } from 'rxjs';

@Component({
  selector: 'app-dashboard',
  standalone: false,
  templateUrl: './dashboard.html',
  styleUrls: [ './dashboard.css' ]
})
export class Dashboard implements OnInit {
  heroes: Hero[] = [];
  top_heroes: Hero[] = [];

  constructor(
    private heroService: HeroService
  ) { };

  ngOnInit(): void {
    this.getHeroes();
    this.getTopHeroes();
  };

  getHeroes(): void {
    this.heroService.getObsHeroes().pipe(
    tap(heroes => this.heroes = heroes)
    ).subscribe();
  };

  getTopHeroes(): void {
    let sortemp: Hero[] = this.heroes.sort(
    (a, b) => b.likes - a.likes);
    this.top_heroes = sortemp.slice(0, 4);
  };

  refreshHeroes(): void {
    window.location.reload()
  }
}