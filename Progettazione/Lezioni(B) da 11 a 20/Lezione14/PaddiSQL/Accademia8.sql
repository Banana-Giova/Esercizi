--Query No.1)

SELECT DISTINCT p.id, 
                p.nome, 
                p.cognome
FROM persona AS p
    JOIN Assenza  AS asse
        ON asse.persona = p.id
    FULL OUTER JOIN Attivitaonprogettuale AS attprog1 
        ON attprog1.giorno = asse.giorno 
    FULL OUTER JOIN AttivitaProgetto AS attprog2
        ON attprog2.giorno = asse.giorno 
GROUP BY p.id
HAVING COUNT(attprog1.giorno) = 0
AND COUNT(attprog2.giorno) = 0;

--Query No.2)

SELECT p.id, 
       p.nome, 
       p.cognome
FROM Persona AS p
    LEFT OUTER JOIN AttivitaProgetto AS attprog 
        ON p.id = attprog.persona
    LEFT OUTER JOIN Progetto AS prog 
        ON prog.id = attprog.progetto 
AND prog.nome = 'Pegasus'
GROUP BY p.id
HAVING COUNT(attprog.progetto) = 0;

--Query No.3)

  WITH tot_sti AS (
    SELECT MAX(stipendio) AS max_sti
    FROM Persona p
    WHERE (p.posizione = 'Professore Associato' 
           OR p.posizione = 'Professore Ordinario')
)
SELECT p.id, 
       p.nome, 
       p.cognome, 
       p.stipendio
FROM persona AS p, 
     tot_sti AS tot
WHERE p.posizione = 'Ricercatore'
  AND tot.max_sti < p.stipendio
GROUP BY p.id

--Query No.4)

WITH bdg_tot AS (
    SELECT AVG(pr.budget) AS max_bdg
    FROM progetto AS prog
)
	
SELECT p.id,
       p.nome,
       p.cognome
FROM persona AS p, 
     progetto AS prog, 
     AttivitaProgetto AS attprog, 
     bdg_tot AS bdg
WHERE prog.id = attprog.progetto
AND p.id = attprog.persona
AND bdg.max_bdg < prog.budget
GROUP BY p.id;