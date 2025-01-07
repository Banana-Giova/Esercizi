CREATE TYPE stato_enum AS ENUM ('LIBERO', 'OCCUPATO');
CREATE TYPE tipo_affitto_enum AS ENUM ('PARZIALE', 'TOTALE');

---

CREATE TABLE Filiali (
    partita_iva VARCHAR(50) PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    indirizzo_sede VARCHAR(255) NOT NULL,
    civico INT NOT NULL,
    telefono VARCHAR(20) NOT NULL
);

CREATE TABLE Utenti (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50)
);

CREATE TABLE Case_in_vendita (
    catastale VARCHAR(50) PRIMARY KEY,
    id VARCHAR(13) UNIQUE,
    indirizzo VARCHAR(255) NOT NULL,
    civico INT NOT NULL,
    piano INT NOT NULL,
    metri FLOAT NOT NULL,
    vani INT NOT NULL,
    prezzo INT NOT NULL,
    stato stato_enum NOT NULL,
    filiale_proponente VARCHAR(50) NOT NULL,
    venduta BOOLEAN NOT NULL,
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva)
);

CREATE TABLE Case_in_affitto (
    catastale VARCHAR(50) PRIMARY KEY,
    id VARCHAR(13) UNIQUE,
    indirizzo VARCHAR(255) NOT NULL,
    civico INT NOT NULL,
    tipo_affitto tipo_affitto_enum NOT NULL,
    bagno_personale BOOLEAN NOT NULL,
    prezzo_mensile INT NOT NULL,
    filiale_proponente VARCHAR(50) NOT NULL,
    affittata BOOLEAN NOT NULL,
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva)
);

CREATE TABLE Vendite_casa (
    catastale VARCHAR(50) NOT NULL,
    data_vendita DATE NOT NULL,
    filiale_proponente VARCHAR(50) NOT NULL,
    filiale_venditrice VARCHAR(50) NOT NULL,
    prezzo_vendita INT NOT NULL,
    acquirente VARCHAR(50) NOT NULL,
    PRIMARY KEY (catastale, data_vendita),
    FOREIGN KEY (catastale) REFERENCES case_in_vendita(catastale),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva),
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva),
    FOREIGN KEY (acquirente) REFERENCES utenti(username)
);

CREATE TABLE Affitti_casa (
    catastale VARCHAR(50) NOT NULL,
    data_affitto DATE NOT NULL,
    filiale_proponente VARCHAR(50) NOT NULL,
    filiale_venditrice VARCHAR(50) NOT NULL,
    prezzo_affitto INT NOT NULL,
    durata_contratto VARCHAR(50) NOT NULL,
    acquirente VARCHAR(50) NOT NULL,
    PRIMARY KEY (catastale, data_affitto),
    FOREIGN KEY (catastale) REFERENCES case_in_affitto(catastale),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva),
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva),
    FOREIGN KEY (acquirente) REFERENCES utenti(username)
);
