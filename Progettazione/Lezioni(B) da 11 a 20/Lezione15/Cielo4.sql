--1. Quali sono i voli di durata maggiore della durata media 
--di tutti i voli della stessa compagnia? 
--Restituire il codice del volo, la compagnia e la durata.

WITH voli_comp AS (
    SELECT AVG(durataMinuti) AS durmed,
           comp AS compagnia
    FROM volo
    GROUP BY comp
)
SELECT volo.codice AS codice_del_volo,
       volo.comp AS compagnia,
       volo.durataMinuti AS durata
FROM Volo volo
    JOIN voli_comp vomp
        ON vomp.compagnia = volo.comp
WHERE volo.durataMinuti > vomp.durmed;

--2. Quali sono le città che hanno piu” di un aeroporto 
--e dove almeno uno di questi ha un volo operato da “Apitalia”?

SELECT DISTINCT lurto.citta
FROM LuogoAeroporto lurto
    JOIN ArrPart part
        ON part.partenza = lurto.aeroporto
    JOIN ArrPart arr
        ON arr.arrivo = lurto.aeroporto
WHERE lurto.citta IN (
	SELECT lurto1.citta
    FROM LuogoAeroporto lurto1
        JOIN Aeroporto aero1
            ON lurto1.aeroporto = aero1.codice
    GROUP BY lurto1.citta
    HAVING COUNT(lurto1.citta) > 1
    ) AND 

--3. Quali sono le coppie di aeroporti (A, B) 
--tali che esistono voli tra A e B ed il numero
--di voli da A a B è uguale al numero di voli da B ad A?



--4. Quali sono le compagnie che hanno voli con durata media 
--maggiore della durata media di tutte le compagnie?



--5. Quali sono gli aeroporti da cui partono voli 
--per almeno 2 nazioni diverse?



--6. Quali sono i voli che partono dalle città 
--con un unico aeroporto? Restituire codice
--dei voli, compagnie, e gli aeroporti di partenza e di arrivo.



--7. Quali sono gli aeroporti raggiungibili dall’aeroporto “JFK” 
--tramite voli diretti e indiretti?



--8. Quali sono le città raggiungibili 
--con voli diretti e indiretti partendo da Roma?



--9. Quali sono le città raggiungibili con esattamente 
--uno scalo intermedo partendo dall’aeroporto “JFK”?

