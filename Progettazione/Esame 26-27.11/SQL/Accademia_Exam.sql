-- QUERY 1

SELECT nome, cognome, stipendio
FROM Persona
WHERE stipendio <= 40000;


-- QUERY 2

SELECT p.nome AS nome,
	   p.cognome AS cognome,
	   p.stipendio AS stipendio
FROM AttivitaProgetto attprog
	JOIN Persona p
		ON p.id = attprog.persona
			AND p.posizione = 'Ricercatore'
            AND p.stipendio <= 40000
GROUP BY p.nome, p.cognome, p.stipendio;

-- QUERY 3

SELECT SUM(budget) AS budget_totale
FROM Progetto;

-- QUERY 4

SELECT p.nome AS nome,
	   p.cognome AS cognome,
	   SUM(prog.budget) AS budget_totale_progetti
FROM AttivitaProgetto attprog
	JOIN Persona p
		ON p.id = attprog.persona
	JOIN Progetto prog
		ON prog.id = attprog.progetto
GROUP BY p.nome, p.cognome;

-- QUERY 5

SELECT p.nome AS nome,
	   p.cognome AS cognome,
	   COUNT(DISTINCT attprog.progetto) AS numero_progetti
FROM AttivitaProgetto attprog
	JOIN Persona p
		ON p.id = attprog.persona
			AND p.posizione = 'Professore Ordinario'
GROUP BY p.nome, p.cognome;

-- QUERY 6

SELECT p.nome AS nome,
	   p.cognome AS cognome,
	   COUNT(DISTINCT asse.id) AS n_assenze_malattia
FROM Assenza asse
	JOIN Persona p
		ON p.id = asse.persona
			AND p.posizione = 'Professore Associato'
WHERE asse.tipo = 'Malattia'
GROUP BY p.nome, p.cognome;

-- QUERY 7

SELECT p.nome AS nome,
	   p.cognome AS cognome,
	   SUM(attprog.oreDurata) AS tot_ore_dedicate
FROM Persona p
	JOIN AttivitaProgetto attprog
		ON p.id = attprog.persona
			AND attprog.progetto = '5'
GROUP BY p.nome, p.cognome;

-- QUERY 8

SELECT p.nome AS nome,
	   p.cognome AS cognome,
	   AVG(attprog.oreDurata) AS media_ore
FROM Persona p
	JOIN AttivitaProgetto attprog
		ON p.id = attprog.persona
GROUP BY p.nome, p.cognome;

-- QUERY 9

SELECT p.nome AS nome,
	   p.cognome AS cognome,
	   SUM(attnon.oreDurata) AS totale_ore_didattica
FROM Persona p
	JOIN AttivitaNonProgettuale attnon
		ON p.id = attnon.persona
			AND attnon.tipo = 'Didattica'
GROUP BY p.nome, p.cognome;

-- QUERY 10

SELECT p.nome AS nome,
	   p.cognome AS cognome,
	   SUM(attprog.oreDurata) AS tot_ore_svolte
FROM Persona P
	JOIN AttivitaProgetto attprog
		ON p.id = attprog.persona
			AND attprog.wp = '5'
			AND attprog.progetto = '3'
GROUP BY p.nome, p.cognome;