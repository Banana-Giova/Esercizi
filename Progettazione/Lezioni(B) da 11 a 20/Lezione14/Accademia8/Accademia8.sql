--1. Quali sono le persone (id, nome e cognome) 
--che hanno avuto assenze solo nei giorni in cui
--non avevano alcuna attività (progettuali o non progettuali)?

SELECT DISTINCT p.id AS id,
				p.nome AS nome,
				p.cognome AS cognome
FROM Persona p
	FULL OUTER JOIN AttivitaProgetto attprog
		ON p.id = attprog.persona
	FULL OUTER JOIN AttivitaNonProgettuale attnon
		ON p.id = attnon.persona
	FULL OUTER JOIN Assenza asse
		ON p.id = asse.persona
GROUP BY p.id
EXCEPT
SELECT DISTINCT p.id AS id,
				p.nome AS nome,
				p.cognome AS cognome
FROM Persona p
	FULL OUTER JOIN AttivitaProgetto attprog
		ON p.id = attprog.persona
	FULL OUTER JOIN AttivitaNonProgettuale attnon
		ON p.id = attnon.persona
	FULL OUTER JOIN Assenza asse
		ON p.id = asse.persona
WHERE asse.id IS NOT NULL
  AND (asse.giorno = attprog.giorno OR asse.giorno = attnon.giorno)
GROUP BY p.id
HAVING COUNT(attprog.id) > 0
   AND COUNT(attnon.id) > 0
ORDER BY id ASC;

--2. Quali sono le persone (id, nome e cognome) 
--che non hanno mai partecipato ad alcun progetto 
--durante la durata del progetto “Pegasus”?

/*
The one that for some reason does not work

WITH pegasus AS (
    SELECT nome, inizio, fine
    FROM Progetto
    WHERE nome = 'Pegasus'
)
SELECT DISTINCT p.id AS id,
				p.nome AS nome,
				p.cognome AS cognome
FROM Pegasus pega,
     Persona p
    FULL OUTER JOIN AttivitaProgetto attprog 
        ON p.id = attprog.persona
WHERE p.id IS NOT NULL
  AND attprog.giorno NOT BETWEEN pega.inizio AND pega.fine
GROUP BY p.id;
*/

WITH pegasus AS (
    SELECT nome, inizio, fine
    FROM Progetto
    WHERE nome = 'Pegasus'
)
SELECT DISTINCT p.id AS id,
				p.nome AS nome,
				p.cognome AS cognome
FROM Persona p
    FULL OUTER JOIN AttivitaProgetto attprog 
        ON p.id = attprog.persona
WHERE p.id IS NOT NULL
GROUP BY p.id
EXCEPT
SELECT DISTINCT p.id AS id,
				p.nome AS nome,
				p.cognome AS cognome
FROM Pegasus pega,
	 Persona p
    FULL OUTER JOIN AttivitaProgetto attprog 
        ON p.id = attprog.persona
WHERE attprog.giorno BETWEEN pega.inizio AND pega.fine
GROUP BY p.id
ORDER BY id ASC;

--3. Quali sono id, nome, cognome e stipendio dei ricercatori con 
--stipendio maggiore di tutti i professori (associati e ordinari)?

WITH prof_asso AS (
    SELECT MAX(stipendio) AS stimax
    FROM Persona
    WHERE posizione = 'Professore Associato'
), prof_ordi AS (
    SELECT MAX(stipendio) AS stimax
    FROM Persona
    WHERE posizione = 'Professore Ordinario'
)
SELECT p.id AS id,
       p.nome AS nome,
       p.cognome AS cognome,
       p.stipendio AS stipendio
FROM Persona p,
     prof_asso asso,
     prof_ordi ordi
WHERE p.posizione = 'Ricercatore'
  AND p.stipendio > asso.stimax
  AND p.stipendio > ordi.stimax
GROUP BY p.id;

--4. Quali sono le persone che hanno lavorato su progetti 
--con un budget superiore alla media dei budget di tutti i progetti?

WITH prog_med AS (
    SELECT AVG(budget) AS media
    FROM Progetto
)
SELECT p.id AS id,
       p.nome AS nome,
       p.cognome AS cognome
FROM prog_med promed,
     Persona p
    JOIN AttivitaProgetto attprog
        ON p.id = attprog.persona
    JOIN Progetto prog
        ON attprog.progetto = prog.id
WHERE prog.budget > promed.media;

--5. Quali sono i progetti con un budget inferiore alla media, 
--ma con un numero complessivo di ore dedicate 
--alle attività di ricerca sopra la media?

WITH prog_analysis AS (
	SELECT prog.nome AS nome,
           SUM(attprog.oreDurata) AS totale,
           prog.budget AS budget
    FROM Progetto prog
        JOIN AttivitaProgetto attprog
            ON prog.id = attprog.progetto
    WHERE tipo = 'Ricerca e Sviluppo'
	GROUP BY prog.nome, prog.budget
), ore_ricerca AS (
    SELECT AVG(totale) AS media
    FROM prog_analysis
), media_budget AS (
    SELECT AVG(budget) AS budmed
    FROM Progetto
)
SELECT progsys.nome AS nome
FROM prog_analysis progsys,
     ore_ricerca oricerca,
     media_budget medbud
WHERE progsys.totale > oricerca.media
  AND progsys.budget < medbud.budmed;