--1. Quali sono il nome, la data di inizio e 
--la data di fine dei WP del progetto di nome ‘Pegasus’?

SELECT wp.nome AS nome,
       wp.inizio AS data_di_inizio,
       wp.fine AS data_di_fine
FROM WP wp, Progetto prog
WHERE prog.id = wp.progetto
  AND prog.nome = 'Pegasus';

--2. Quali sono il nome, il cognome e la posizione degli 
--strutturati che hanno almeno una attività nel progetto ‘Pegasus’, 
--ordinati per cognome decrescente?

SELECT DISTINCT pers.nome AS nome_strutturato,
                pers.cognome AS cognome_strutturato,
                pers.posizione AS posizione
FROM Persona pers,
     AttivitaProgetto attprog,
     Progetto prog
WHERE attprog.persona = pers.id
  AND attprog.progetto = prog.id
  AND prog.nome = 'Pegasus'
ORDER BY cognome_strutturato DESC;

--3. Quali sono il nome, il cognome e la posizione degli 
--strutturati che hanno più di una attività nel progetto ‘Pegasus’?

SELECT DISTINCT pers.nome AS nome_strutturato,
                pers.cognome AS cognome_strutturato,
                pers.posizione AS posizione
FROM Persona pers, 
     AttivitaProgetto attprog1,
     AttivitaProgetto attprog2,
     Progetto prog
WHERE attprog1.persona = pers.id
  AND attprog2.persona = pers.id
  AND attprog1.progetto = prog.id
  AND attprog2.progetto = prog.id
  AND attprog1.id <> attprog2.id
  AND prog.nome = 'Pegasus';

--4. Quali sono il nome, il cognome e la posizione dei 
--Professori Ordinari che hanno fatto almeno una assenza per malattia?

SELECT DISTINCT pers.nome AS nome_strutturato,
                pers.cognome AS cognome_strutturato,
                pers.posizione AS posizione
FROM Persona pers,
      Assenza asse
WHERE pers.posizone = 'Professore Ordinario'
  AND asse.persona = pers.id
  AND asse.tipo = 'Malattia'

--5. Quali sono il nome, il cognome e la posizione dei 
--Professori Ordinari che hanno fatto più di una assenza per malattia?

SELECT DISTINCT pers.nome AS nome_strutturato,
                pers.cognome AS cognome_strutturato,
                pers.posizione AS posizione
FROM Persona pers, 
     Assenza asse1,
     Assenza asse2
WHERE asse1.persona = pers.id
  AND asse2.persona = pers.id
  AND asse1.tipo = 'Malattia'
  AND asse2.tipo = 'Malattia'
  AND asse1.id <> asse2.id;

--6. Quali sono il nome, il cognome e la posizione dei 
--Ricercatori che hanno almeno un impegno per didattica?

SELECT DISTINCT pers.nome AS nome_strutturato,
                pers.cognome AS cognome_strutturato,
                pers.posizione AS posizione
FROM Persona pers
    JOIN AttivitaNonProgettuale attnon
        ON attnon.persona = pers.id
WHERE attnon.tipo = 'Didattica'
  AND pers.posizione = 'Ricercatore';

--7. Quali sono il nome, il cognome e la posizione dei
--Ricercatori che hanno più di un impegno per didattica?

SELECT DISTINCT pers.nome AS nome_strutturato,
                pers.cognome AS cognome_strutturato,
                pers.posizione AS posizione
FROM Persona pers
    JOIN AttivitaNonProgettuale attnon1
        ON attnon1.persona = pers.id
    JOIN AttivitaNonProgettuale attnon2
        ON attnon2.persona = pers.id
WHERE attnon1.tipo = 'Didattica'
  AND attnon2.tipo = 'Didattica'
  AND asse1.id <> asse2.id
  AND pers.posizione = 'Ricercatore';

--8. Quali sono il nome e il cognome degli strutturati 
--che nello stesso giorno hanno sia attività progettuali 
--che attività non progettuali?

SELECT DISTINCT pers.nome AS nome_strutturato,
                pers.cognome AS cognome_strutturato
FROM Persona pers
    JOIN AttivitaProgetto attprog
        ON attprog.persona = pers.id
    JOIN AttivitaNonProgettuale attnon
        ON attnon.persona = pers.id
WHERE attprog.giorno = attnon.giorno;

--9. Quali sono il nome e il cognome degli strutturati 
--che nello stesso giorno hanno sia attività progettuali 
--che attività non progettuali? Si richiede anche di proiettare 
--il giorno, il nome del progetto, il tipo di attività non progettuali 
--e la durata in ore di entrambe le attività.

SELECT pers.nome AS nome_strutturato,
       pers.cognome AS cognome_strutturato,
       attprog.giorno AS giorno_attivita,
       prog.nome AS nome_progetto,
       attnon.tipo AS tipo_attnon,
       attprog.oreDurata AS durata_attprog,
       attnon.oreDurata AS durata_attnon
FROM Persona pers
    JOIN AttivitaProgetto attprog
        ON attprog.persona = pers.id
    JOIN AttivitaNonProgettuale attnon
        ON attnon.persona = pers.id
    JOIN Progetto prog
        ON attprog.progetto = prog.id
WHERE attprog.giorno = attnon.giorno;



--10. Quali sono il nome e il cognome degli strutturati 
-- che nello stesso giorno sono assenti e hanno attività progettuali?

SELECT DISTINCT pers.nome AS nome_strutturato,
       pers.cognome AS cognome_strutturato
FROM Persona pers
    JOIN Assenza asse
        ON asse.persona = pers.id
    JOIN AttivitaProgetto attprog
        ON attprog.persona = pers.id
WHERE asse.giorno = attprog.giorno;

--11. Quali sono il nome e il cognome degli strutturati 
--che nello stesso giorno sono assenti e hanno attività progettuali? 
--Si richiede anche di proiettare il giorno, il nome del progetto, 
--la causa di assenza e la durata in ore della attività progettuale.

SELECT pers.nome AS nome_strutturato,
       pers.cognome AS cognome_strutturato,
       attprog.giorno AS giorno_attivita,
       asse.tipo AS tipo_attnon,
       attprog.oreDurata AS durata_attprog
FROM Persona pers
    JOIN Assenza asse
        ON asse.persona = pers.id
    JOIN AttivitaProgetto attprog
        ON attprog.persona = pers.id
WHERE asse.giorno = attprog.giorno;

--12. Quali sono i WP che hanno lo stesso nome, 
--ma appartengono a progetti diversi?

SELECT DISTINCT wp.nome AS nome
FROM WP wp1
    JOIN WP wp2
        ON wp1.nome = wp2.nome
WHERE wp1.progetto <> wp2.progetto;