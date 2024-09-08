create type Strutturato as enum (
    'Ricercatore', 'Professore Associato', 'Professore Ordinario'
);

create type LavoroProgetto as enum (
    'Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro'
);

create type LavoroNonProgettuale as enum (
    'Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro'
);

create type CausaAssenza as enum (
    'Chiusura Universitaria', 'Maternita', 'Malattia'
);

create domain PosInteger as integer 
    check ( value >= 0 );

create domain StringaM as varchar(
    100
);

create domain NumeroOre as integer
    check ( value >=0 and value <= 8 );

create domain Denaro as real
    check ( value >= 0 );


---------------------------------------


create table Persona (
    id PosInteger PRIMARY KEY NOT NULL,
    nome StringaM NOT NULL,
    cognome StringaM NOT NULL,
    posizione Strutturato NOT NULL,
    stipendio Denaro NOT NULL
);

create table Progetto (
    id PosInteger PRIMARY KEY NOT NULL,
    nome StringaM NOT NULL,
    inizio date NOT NULL,
    fine date NOT NULL,
    budget Denaro NOT NULL,
        UNIQUE ( nome ),
        check ( inizio < fine )
);

create table WP (
    progetto PosInteger NOT NULL,
    id PosInteger PRIMARY KEY NOT NULL,
    nome StringaM NOT NULL,
    inizio date,
    fine date NOT NULL,
        check ( inizio < fine),
        UNIQUE ( progetto, id ),
        foreign key (progetto) references Progetto(id)
);

create table AttivitaProgetto (
    id PosInteger PRIMARY KEY NOT NULL,
    persona PosInteger NOT NULL,
    progetto PosInteger NOT NULL,
    wp PosInteger NOT NULL,
    giorno date NOT NULL,
    tipo LavoroProgetto NOT NULL,
    oreDurata NumeroOre NOT NULL,
        foreign key (persona) references Persona(id),
        foreign key (progetto, WP) references WP(progetto, id)
);

create table AttivitaNonProgettuale (
    id PosInteger PRIMARY KEY NOT NULL,
    persona PosInteger NOT NULL,
    tipo LavoroNonProgettuale NOT NULL,
    giorno date NOT NULL,
    oreDurata NumeroOre NOT NULL,
        foreign key (persona) references Persona(id)
);

create table Assenza (
    id PosInteger PRIMARY KEY NOT NULL,
    persona PosInteger NOT NULL,
    tipo CausaAssenza NOT NULL,
    giorno date NOT NULL,
        UNIQUE ( persona, giorno ),
        foreign key (persona) references Persona(id)
);