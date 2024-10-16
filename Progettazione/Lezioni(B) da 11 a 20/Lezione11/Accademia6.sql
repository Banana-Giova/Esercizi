--1. Quanti sono gli strutturati di ogni fascia?

SELECT DISTINCT pers.posizione AS posizione,
                COUNT(*) AS numero_strutturati
FROM Persona pers
WHERE TRUE
GROUP BY pers.posizione;

--2. Quanti sono gli strutturati con stipendio ≥ 40000?

SELECT COUNT(*) AS numero_strutturati
FROM Persona pers
WHERE pers.stipendio >= 40000;

--3. Quanti sono i progetti già finiti che superano il 
--budget di 50000?

SELECT COUNT(*) AS numero_progetti
FROM Progetto prog
WHERE prog.budget >= 50000
  AND prog.fine < CURRENT_DATE;

--4. Qual è la media, il massimo e il minimo delle ore 
--delle attività relative al progetto ‘Pegasus’ ?

SELECT AVG(attprog.oreDurata) AS media_ore,
       MAX(attprog.oreDurata) AS massimo_ore,
       MIN(attprog.oreDurata) AS minimo_ore
FROM AttivitaProgetto attprog
WHERE TRUE;

--5. Quali sono le medie, i massimi e i minimi delle ore 
--giornaliere dedicate al progetto ‘Pegasus’ da ogni singolo docente?

SELECT pers.nome AS nome_docente,
       pers.cognome AS cognome_docente,
       AVG(attprog.oreDurata) AS media_ore,
       MAX(attprog.oreDurata) AS massimo_ore,
       MIN(attprog.oreDurata) AS minimo_ore
FROM AttivitaProgetto attprog
    JOIN Persona pers
        ON attprog.persona = pers.id
WHERE TRUE
GROUP BY pers.id;

--6. Qual è il numero totale di ore dedicate alla 
--didattica da ogni docente?

SELECT pers.nome AS nome_docente,
       pers.cognome AS cognome_docente,
       SUM(attprog.oreDurata) AS totale_ore
FROM AttivitaProgetto attprog
    JOIN Persona pers
        ON attprog.persona = pers.id
WHERE TRUE
GROUP BY pers.id;

--7. Qual è la media, il massimo e il minimo degli 
--stipendi dei ricercatori?

SELECT AVG(pers.stipendio) AS media_stipendio,
       MAX(pers.stipendio) AS massimo_stipendio,
       MIN(pers.stipendio) AS minimo_stipendio
FROM Persona pers
WHERE pers.posizione = 'Ricercatore';

--8. Quali sono le medie, i massimi e i minimi degli stipendi 
--dei ricercatori, dei professori associati e dei professori ordinari?

SELECT pers.posizione AS posizione,
       AVG(pers.stipendio) AS media_stipendio,
       MAX(pers.stipendio) AS massimo_stipendio,
       MIN(pers.stipendio) AS minimo_stipendio
FROM Persona pers
WHERE TRUE
GROUP BY pers.poszione;

--9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto 
--nel quale ha lavorato?

SELECT prog.nome AS progetto,
       SUM(attprog.oreDurata) AS ore_dedicate
FROM AttivitaProgetto attprog
    JOIN Persona pers
        ON attprog.persona = pers.id
    JOIN Progetto prog
        ON attprog.progetto = prog.id
WHERE pers.nome = 'Ginevra'
  AND pers.cognome = 'Riva'
GROUP BY prog.id;

--10. Qual è il nome dei progetti su cui lavorano 
--più di due strutturati?

SELECT prog.nome AS nome_progetto,
       COUNT(attprog.persona) AS numero_di_strutturati
FROM AttivitaProgetto attprog
    JOIN Persona pers
        ON attprog.persona = pers.id
    JOIN Progetto prog
        ON attprog.progetto = prog.id
WHERE TRUE
GROUP BY prog.id
HAVING COUNT(attprog.persona) >= 2;

--11. Quali sono i professori associati che hanno lavorato 
--su più di un progetto?

SELECT pers.nome AS nome_docente,
       pers.cognome AS cognome_docente,
       COUNT(attprog.persona) AS numero_di_progetti
FROM AttivitaProgetto attprog
    JOIN Persona pers
        ON attprog.persona = pers.id
    JOIN Progetto prog
        ON attprog.progetto = prog.id
WHERE TRUE
GROUP BY pers.id
HAVING COUNT(attprog.persona) >= 2;