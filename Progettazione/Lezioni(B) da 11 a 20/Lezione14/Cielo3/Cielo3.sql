--1. Qual è la durata media, per ogni compagnia, dei voli 
--che partono da un aeroporto situato in Italia?

WITH italian_iata AS (
    SELECT aero.codice AS codice
    FROM Aeroporto aero
		JOIN LuogoAeroporto lurto
			ON aero.codice = lurto.aeroporto
    WHERE lurto.nazione = 'Italy'
)
SELECT ap.comp AS compagnia,
       AVG(volo.durataMinuti) AS durata_media
FROM italian_iata,
     ArrPart ap
    JOIN Volo volo
        ON ap.codice = volo.codice
WHERE ap.partenza = italian_iata.codice
GROUP BY ap.comp;

--2. Quali sono le compagnie che operano voli con durata media 
--maggiore della durata media di tutti i voli?

WITH all_voli AS (
    SELECT durataMinuti AS durata
    FROM Volo
)
SELECT volo.comp AS compagnia,
	   AVG(volo.durataMinuti)
FROM Volo volo,
	 all_voli
GROUP BY volo.comp
HAVING AVG(volo.durataMinuti) > AVG(all_voli.durata);

--3. Quali sono le città dove il numero totale di voli in arrivo 
--è maggiore del numero medio dei voli in arrivo per ogni città?

/*WITH num AS (
    SELECT COUNT(ap.arrivo) AS arrivi
    FROM ArrPart ap
        JOIN LuogoAeroporto lurto
            ON ap.arrivo = lurto.aeroporto
)
SELECT lurto.citta AS citta
FROM num,
	 ArrPart ap
    JOIN LuogoAeroporto lurto
        ON ap.arrivo = lurto.aeroporto
GROUP BY lurto.citta
HAVING COUNT(ap.arrivo) > AVG(num.arrivi);*/

WITH num AS (
    SELECT lurto.citta AS citta,
	       COUNT(ap.arrivo) AS arrivi
    FROM ArrPart ap
        JOIN LuogoAeroporto lurto
            ON ap.arrivo = lurto.aeroporto
    GROUP BY lurto.citta
), average AS (
	SELECT AVG(num.arrivi) AS total
	FROM num
)
SELECT num.citta
FROM num,
	 average
WHERE num.arrivi > average.total;

--4. Quali sono le compagnie aeree che hanno voli in partenza 
--da aeroporti in Italia con una durata media inferiore alla 
--durata media di tutti i voli in partenza da aeroporti in Italia?

WITH mastino AS (
    SELECT ap.comp AS compagnia,
           COUNT()
    FROM ArrPart ap
        JOIN LuogoAeroporto lurto
            ON ap.partenza = lurto.aeroporto
        JOIN Volo volo
            ON ap.codice = volo.codice
)

--5. Quali sono le città i cui voli in arrivo hanno 
--una durata media che differisce di più di una deviazione standard 
--dalla durata media di tutti i voli? Restituire città e
--durate medie dei voli in arrivo.



--6. Quali sono le nazioni che hanno il maggior numero di città 
--dalle quali partono voli diretti in altre nazioni?

