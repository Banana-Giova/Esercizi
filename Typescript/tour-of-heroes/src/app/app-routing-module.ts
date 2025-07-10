import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Heroes } from './heroes/heroes';

const routes: Routes = [
  { path: 'heroes', component: Heroes }
];
/*
 Una route serve a definire la mappatura tra
 un percorso URL ed uno specifico componente dell'applicazione.
 In base a dove naviga l'utente, il Router utilizza 
 questa configurazione per determinare quale 
 componente renderizzare.

 Le singole route sono raccolte nell'array inizializzato
 qui sopra: Routes. Esso viene poi passato al modulo
 RouterModule tramite forRoot().
*/

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }