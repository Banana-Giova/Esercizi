--Query 1--
SELECT distinct cognome 
FROM persona;

--Query 2--
SELECT id, nome, cognome 
FROM persona 
WHERE posizione = 'Ricercatore';

--Query 3--
SELECT id, cognome 
FROM persona 
WHERE posizione = 'Professore Associato' and cognome like 'V%';

--Query 4--
SELECT id, cognome 
FROM persona 
WHERE posizione = 'Professore Ordinario' or posizione = 'Professore Associato' and cognome like 'V%';

--Query 5--
select id, nome
from Progetto
where CURRENT_DATE > fine;

--Query 6--
SELECT nome
FROM progetto
ORDER BY inizio ASC;

--Query 7--
SELECT nome
FROM wp
ORDER BY nome ASC;

--Query 8--
SELECT distinct tipo
FROM assenza;

--Query 9--
SELECT distinct tipo
FROM attivitaprogetto;

--Query 10--
SELECT distinct giorno
FROM attivitanonprogettuale
WHERE tipo = 'Didattica'
ORDER BY giorno ASC;