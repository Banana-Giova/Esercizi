--Query 1 -> Giusta, con appunto--
SELECT distinct cognome 
FROM persona;
--WHERE TRUE;--
--where è opzionale, ma è meglio metterlo

--Query 2 -> Giusta, ma da indentare--
SELECT id, nome, cognome 
FROM persona 
WHERE posizione = 'Ricercatore';

--Query 3 -> Giusta, ma da indentare--
SELECT id, cognome 
FROM persona 
WHERE posizione = 'Professore Associato' and cognome like 'V%';

--Query 4 -> Sbagliata--
SELECT id, cognome 
FROM persona 
WHERE posizione = 'Professore Ordinario' or posizione = 'Professore Associato' and cognome like 'V%';
--WHERE ( posizione = 'Professore Ordinario' 
    --or posizione = 'Professore Associato' )
    --and cognome like 'V%';

--oppure--

--WHERE posizione IN ('Professore Ordinario', 'Professore Associato')
    --and cognome like 'V%';

--Query 5 -> Giusta, ricorda le maiuscole per ortografia--
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

--Query 8 -> Giusta, ma ricorda il WHERE--
SELECT distinct tipo
FROM assenza;

--Query 9 -> Giusta, ma ricorda il WHERE--
SELECT distinct tipo
FROM attivitaprogetto;

--Query 10 -> Giusta--
SELECT distinct giorno
FROM attivitanonprogettuale
WHERE tipo = 'Didattica'
ORDER BY giorno ASC;