import { NgModule, provideBrowserGlobalErrorListeners } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { provideHttpClient, withInterceptorsFromDi } from '@angular/common/http';

import { AppRoutingModule } from './app-routing-module';
import { App } from './app';
import { Heroes } from './heroes/heroes';
import { HeroDetail } from './hero-detail/hero-detail';
import { Messages } from './messages/messages';
import { HeroLike } from './hero-like/hero-like';
import { Dashboard } from './dashboard/dashboard';

/*
 Un modulo in Angular è una struttura fondamentale 
 che serve a organizzare e raggruppare insieme 
 componenti, direttive, pipe e servizi correlati, 
 in modo da costruire applicazioni modulari e manutenibili.

 Più tecnicamente, un modulo è una classe decorata con @NgModule, 
 che definisce un contesto di esecuzione per un insieme 
 di funzionalità correlate. I moduli aiutano a:

  - Organizzare il codice in blocchi logici.
  - Gestire le dipendenze tra componenti e servizi.
  - Caricare funzionalità in modo modulare 
    (ad esempio lazy loading).
  - Condividere funzionalità tra diverse parti dell’app 
    tramite l’import/export.
*/

@NgModule({
  declarations: [
    App,
    Heroes,
    HeroDetail,
    Messages,
    HeroLike,
    Dashboard
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideHttpClient(withInterceptorsFromDi())
  ],
  bootstrap: [ App ]
})
export class AppModule { }