Utente(
    __nome__:varchar,
    iscrizione:timestamp
);

Video(
    __id__:serial,
    titolo:varchar,
    descrizione:TEXT,
    autore:varchar,
    istante_caricamento:timestamp,
    file_video:File,
    cat:varchar
)
FOREIGN KEY (cat) REFERENCES Categoria(nome)
FOREIGN KEY (autore) REFERENCES Utente(__nome__);

VideoCensurato(
    __video__:integer,
    motivo:varchar,
    istante:timestamp
)
FOREIGN KEY (__video__) REFERENCES Video(__id__);

Categoria(
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
);

Tag(
    __nome__:varchar
);

Visualizzazione(
    __id__:serial,
    istante_view:timestamp,
    utente:varchar,
    video:integer
)
FOREIGN KEY (utente) REFERENCES Utente(__nome__)
FOREIGN KEY (video) REFERENCES Video(__id__);

Valutazione(
    __id__:serial,
    valore:Voto,
    utente:varchar,
    video:integer
)
FOREIGN KEY (utente) REFERENCES Utente(__nome__)
FOREIGN KEY (video) REFERENCES Video(__id__);

Commento(
    __id__:serial,
    testo:varchar,
    istante_commento:timestamp,
    utente:varchar,
    video:integer
)
FOREIGN KEY (utente) REFERENCES Utente(__nome__)
FOREIGN KEY (video) REFERENCES Video(__id__);

Playlist(
    __id__:serial,
    utente:varchar,
    nome:varchar,
    tipo:TipoPlaylist,
    istante_creazione:timestamp
)
FOREIGN KEY (utente) REFERENCES Utente(__nome__);