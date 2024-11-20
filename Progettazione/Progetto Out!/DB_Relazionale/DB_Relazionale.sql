Sede(
    __id__:SERIAL PRIMARY KEY,
    nome:StringaM,
    indirizzo:Indirizzo,
    città:INTEGER
)
FOREIGN KEY (città) REFERENCES Città(__id__);

Città(
    __id__:SERIAL PRIMARY KEY,
    nome:StringaM
);

Sala(
    __numero__: IntMagZ PRIMARY KEY,
    sede:INTEGER
)
FOREIGN KEY (sede) REFERENCES Sede(__id__);

Settore(
    __id__: SERIAL PRIMARY KEY,
    nome: StringaM,
    sala: INTEGER
)
FOREIGN KEY (sala) REFERENCES Sala(__id__);

Posto(
   __id__:SERIAL PRIMARY KEY,
   num_posto: NumPosto,
   settore: INTEGER
)
FOREIGN KEY (settore) REFERENCES Sttore(__id__);

Spettacolo(
    __id__: SERIAL PRIMARY KEY,
    titolo: StringaM,
    tipo: TipoSpettacolo,
    genere: StringaM
);

Evento(
    __id__:INTEGER PRIMARY KEY,
    spettacolo: INTEGER,
    sala: INTEGER,
    data_ora: DATETIME,
    prezzo_pieno: Prezzo,
    prezzo_ridotto: Prezzo
)
FOREIGN KEY (spettacolo) REFERENCES Spettacolo(__id__)
FOREIGN KEY (sala) REFERENCES Sala(__id__);

Artista(
    __id__:SERIAL PRIMARY KEY,
    artist_name: StringaM
);

Utente(
    __cf__:CF PRIMARY KEY,
    nome:StringaM,
    cognome:StringaM
);

Prenotazione(
    __id__:SERIAL,
    utente:CF,
    posto_pren: INTEGER,
    evento: INTEGER,
    istante_pren: timestamp
    prezzo: Prezzo
)
FOREIGN KEY (utente) REFERENCES Utente(__cf__)
FOREIGN KEY (posto_pren) REFERENCES Posto(__id__)
FOREIGN KEY (evento) REFERENCES Evento(__id__);