--1. Qual è media e deviazione standard degli stipendi 
--per ogni categoria di strutturati?

SELECT pers.posizione AS posizione,
       AVG(pers.stipendio) AS stipendio_medio,
       STDDEV(pers.stipendio) AS deviazione_stipendio
FROM Persona pers
WHERE TRUE
GROUP BY posizione;

--2. Quali sono i ricercatori (tutti gli attributi) 
--con uno stipendio superiore alla media della loro categoria?

SELECT pers.id AS id,
       pers.nome AS nome,
       pers.cognome AS cognome,
       pers.posizione AS posizione,
       pers.stipendio AS stipendio
FROM Persona pers
WHERE pers.posizione = 'Ricercatore'
  AND pers.stipendio > (
        SELECT AVG(pers.stipendio)
        FROM Persona pers
        WHERE pers.posizione = 'Ricercatore'; 
  )
GROUP BY pers.id;

--3. Per ogni categoria di strutturati quante sono le persone 
--con uno stipendio che differisce di al massimo una deviazione 
--standard dalla media della loro categoria?

/*WITH 
SELECT pers.posizione AS posizione,
       COUNT(pers.id) AS numero
FROM Persona pers
WHERE TRUE
GROUP BY pers.posizione;*/

--4. Chi sono gli strutturati che hanno lavorato 
--almeno 20 ore complessive in attività progettuali? 
--Restituire tutti i loro dati e il numero di ore lavorate.

SELECT pers.id AS id,
       pers.nome AS nome,
       pers.cognome AS cognome,
       pers.posizione AS posizione,
       pers.stipendio AS stipendio,
       SUM(attprog.oreDurata) AS ore_lavorate
FROM Persona pers
    JOIN AttivitaProgetto attprog
        ON pers.id = attprog.persona
WHERE TRUE
GROUP BY pers.id
HAVING SUM(attprog.oreDurata) > 19;

--5. Quali sono i progetti la cui durata è superiore 
--alla media delle durate di tutti i progetti? 
--Restituire nome dei progetti e loro durata in giorni.

SELECT prog.nome AS nome_progetto,
       (prog.fine - prog.inizio) AS durata_progetto
FROM Progetto prog
WHERE TRUE
GROUP BY prog.id
HAVING (prog.fine - prog.inizio) > (
    SELECT AVG(prog.fine - prog.inizio)
    FROM Progetto prog
    );

--6. Quali sono i progetti terminati in data odierna 
--che hanno avuto attività di tipo “Dimostrazione”? 
--Restituire nome di ogni progetto e il numero complessivo 
--delle ore dedicate a tali attività nel progetto.

SELECT prog.nome AS nome_progetto,
       SUM(attprog.oreDurata) AS ore_dedicate
FROM Progetto prog
    JOIN AttivitaProgetto attprog
        ON prog.id = attprog.progetto
WHERE attprog.tipo = 'Dimostrazione'
GROUP BY prog.id;

--7. Quali sono i professori ordinari che hanno fatto 
--più assenze per malattia del numero di assenze medio 
--per malattia dei professori associati? 
--Restituire id, nome e cognome del professore 
--e il numero di giorni di assenza per malattia.

SELECT pers.id AS id_prof,
       pers.nome AS nome_prof,
       pers.cognome AS cognome_prof,
       COUNT(asse.id) AS numero_assenze_malattia
FROM Persona pers
    JOIN Assenza asse
        ON pers.id = asse.persona
WHERE asse.tipo = 'Malattia'
  AND pers.posizione = 'Professore Ordinario'
GROUP BY pers.id
HAVING COUNT(asse.id) > (SELECT(
    SELECT COUNT(asse.id)
    FROM Persona pers
        JOIN Assenza asse
            ON pers.id = asse.persona
    WHERE asse.tipo = 'Malattia'
      AND pers.posizione = 'Professore Associato'
)/
(
    SELECT 1.0*COUNT(asse.id)
    FROM Persona pers
        JOIN Assenza asse
            ON pers.id = asse.persona
    WHERE asse.tipo = 'Malattia'
      AND pers.posizione = 'Professore Associato'  
));