-- Rimuove eventuali trigger e funzioni preesistenti
DROP TRIGGER IF EXISTS trigger_aggiorna_timestamp ON utenti;
DROP FUNCTION IF EXISTS aggiorna_timestamp;

-- Funzione per aggiornare il campo updated_at
CREATE OR REPLACE FUNCTION aggiorna_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger per aggiornare il campo updated_at prima di un UPDATE
CREATE TRIGGER trigger_aggiorna_timestamp
BEFORE UPDATE ON utenti
FOR EACH ROW
EXECUTE FUNCTION aggiorna_timestamp();

-- Test per verificare il funzionamento del trigger
-- Nota: da eseguire solo in un ambiente di test
-- INSERT INTO utenti (nome, email) VALUES ('Mario', 'mario@example.com');
-- UPDATE utenti SET email = 'mario.rossi@example.com' WHERE nome = 'Mario';
-- SELECT * FROM utenti WHERE nome = 'Mario';



--Slide Remake

-- Funzione associata al trigger
CREATE OR REPLACE FUNCTION V_Persona_gen_compl_1()
RETURNS TRIGGER AS $V_Persona_gen_compl_1$
DECLARE
    isError BOOLEAN := FALSE; -- Variabile per verificare l'errore
BEGIN
    -- Controlla se la nuova persona (NEW.id) non esiste in entrambe le tabelle Studente e Docente
    isError := NOT EXISTS (
        SELECT persona FROM Studente WHERE persona = NEW.id
        UNION ALL
        SELECT persona FROM Docente WHERE persona = NEW.id
    );

    -- Se isError è TRUE, lancia un'eccezione
    IF isError THEN
        RAISE EXCEPTION 'Vincolo V_Persona_gen_compl_1 violato (persona.id=%)', NEW.id;
    END IF;

    -- Restituisce la riga nuova; importante per i trigger BEFORE, ignorato per AFTER
    RETURN NEW;
END;
$V_Persona_gen_compl_1$ LANGUAGE plpgsql;

-- Creazione del trigger
CREATE CONSTRAINT TRIGGER V_Persona_gen_compl_1_persona
AFTER INSERT ON Persona -- Attivato dopo ogni inserimento nella tabella Persona
DEFERRABLE -- Il vincolo può essere differito al termine della transazione
FOR EACH ROW -- Il trigger agisce su ogni riga
EXECUTE PROCEDURE V_Persona_gen_compl_1();





-- Funzione del trigger: V_Persona_gen_compl_2
CREATE OR REPLACE FUNCTION V_Persona_gen_compl_2()
RETURNS TRIGGER AS $V_Persona_gen_compl_2$
-- La funzione vedrà 'OLD' come argomento
DECLARE 
    isError BOOLEAN := false;
BEGIN
    -- Controlla se la persona eliminata non ha più nessun riferimento in Studente o Docente
    isError := EXISTS(
        SELECT * 
        FROM (Persona p 
              LEFT OUTER JOIN Studente s ON p.id = s.persona) 
             LEFT OUTER JOIN Docente d ON p.id = d.persona
        WHERE p.id = OLD.persona 
          AND s.persona IS NULL 
          AND d.persona IS NULL
    );

    -- Se isError è vero, lancia un'eccezione
    IF (isError) THEN 
        RAISE EXCEPTION 'Vincolo V_Persona_isa_compl_2 violato (persona=%)', OLD.persona;
    END IF;

    RETURN OLD; -- Il valore di ritorno nei trigger AFTER è ignorato
END;
$V_Persona_gen_compl_2$ LANGUAGE plpgsql;

-- Trigger per DELETE su Studente
CREATE CONSTRAINT TRIGGER V_Persona_gen_compl_2_studente
AFTER DELETE ON Studente
DEFERRABLE FOR EACH ROW 
EXECUTE FUNCTION V_Persona_gen_compl_2();

-- Trigger per DELETE su Docente
CREATE CONSTRAINT TRIGGER V_Persona_gen_compl_2_docente
AFTER DELETE ON Docente
DEFERRABLE FOR EACH ROW 
EXECUTE FUNCTION V_Persona_gen_compl_2();