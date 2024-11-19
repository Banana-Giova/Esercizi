CREATE DOMAIN StringaM AS VARCHAR(255);

CREATE DOMAIN LongString AS TEXT;

CREATE DOMAIN IntMagZ AS INTEGER
    CHECK (VALUE > 0);

CREATE DOMAIN IntEqZ AS INTEGER
    CHECK (VALUE >= 0);

CREATE DOMAIN Prezzo AS NUMERIC(10, 2)
    CHECK (VALUE >= 0);

CREATE DOMAIN CF AS CHAR(16)
    CHECK (
        VALUE ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z0-9]{4}[A-Z0-9]$'
    )

CREATE TYPE Indirizzo AS (
    via VARCHAR(255),
    numero VARCHAR(10),
    CAP VARCHAR(10)
);

CREATE TYPE TipoSpettacolo AS ENUM(
    'Concerto',
    'Performance',
    'Rappresentazione Teatrale'.
    'Film'
);