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





--4. Quali sono il nome, il cognome e la posizione dei 
--Professori Ordinari che hanno fatto almeno una assenza per malattia?





--5. Quali sono il nome, il cognome e la posizione dei 
--Professori Ordinari che hanno fatto più di una assenza per malattia?





--6. Quali sono il nome, il cognome e la posizione dei 
--Ricercatori che hanno almeno un impegno per didattica?





--7. Quali sono il nome, il cognome e la posizione dei
--Ricercatori che hanno più di un impegno per didattica?





--8. Quali sono il nome e il cognome degli strutturati 
--che nello stesso giorno hanno sia attività progettuali 
--che attività non progettuali?





--9. Quali sono il nome e il cognome degli strutturati 
--che nello stesso giorno hanno siaattività progettuali 
--che attività non progettuali? Si richiede anche di proiettare 
--il giorno, il nome del progetto, il tipo di attività non progettuali 
--e la durata in ore di entrambe le attività.





--10. Quali sono il nome e il cognome degli strutturati 
-- che nello stesso giorno sono assenti e hanno attività progettuali?





--11. Quali sono il nome e il cognome degli strutturati 
--che nello stesso giorno sonoassenti e hanno attività progettuali? 
--Si richiede anche di proiettare il giorno, il nome del progetto, 
--la causa di assenza e la durata in ore della attività progettuale.





--12. Quali sono i WP che hanno lo stesso nome, 
--ma appartengono a progetti diversi?