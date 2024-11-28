BEGIN TRANSACTION;

CREATE DOMAIN StringaM AS VARCHAR(100);

CREATE DOMAIN CF AS VARCHAR(16);

CREATE DOMAIN Targa AS VARCHAR(7);

----------------------------------------------

CREATE TABLE Utente (
    cf CF NOT NULL,
    nome StringaM NOT NULL,
    cognome StringaM NOT NULL,
    PRIMARY KEY (cf)
);

CREATE TABLE Veicolo (
    targa Targa NOT NULL,
    PRIMARY KEY (targa)
);

CREATE TABLE Noleggio (
    id SERIAL NOT NULL,
    utente CF NOT NULL,
    veicolo Targa NOT NULL,
    inizio TIMESTAMP NOT NULL,
    is_terminato BOOLEAN NOT NULL,
    fine TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (utente) REFERENCES Utente(cf) DEFERRABLE,
    FOREIGN KEY (veicolo) REFERENCES Veicolo(targa) DEFERRABLE,
    CHECK(
        (is_terminato IS False AND fine IS NULL) OR
        (is_terminato IS True AND fine > inizio)
    )
);

CREATE TABLE Sinistro (
    id SERIAL NOT NULL,
    istante TIMESTAMP NOT NULL,
    veicolo Targa NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (veicolo) REFERENCES Veicolo(targa) DEFERRABLE
);

----------------------------------------------

REVOKE UPDATE (id) ON Noleggio FROM PUBLIC;
REVOKE UPDATE (id) ON Sinistro FROM PUBLIC;

COMMIT;