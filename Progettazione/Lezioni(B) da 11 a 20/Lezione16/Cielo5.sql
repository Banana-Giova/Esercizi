--1. Quali sono gli aeroporti raggiungibili dall’aeroporto ‘JFK’ 
--tramite voli diretti e indiretti?

SELECT DISTINCT ap.arrivo AS aeroporti
FROM ArrPart ap
WHERE ap.partenza = 'JFK'
   OR ap.partenza IN (
    SELECT DISTINCT nest_ap.arrivo
    FROM ArrPart nest_ap
    WHERE nest_ap.partenza = 'JFK'
);

--2. Quali sono le città raggiungibili con voli diretti 
--e indiretti partendo da Roma?

SELECT DISTINCT lurto.citta AS citta
FROM ArrPart ap
    JOIN LuogoAeroporto lurto
        ON ap.partenza = lurto.aeroporto
WHERE lurto.citta = 'Roma'
   OR ap.partenza IN (
    SELECT DISTINCT nest_ap.arrivo
    FROM ArrPart nest_ap
        JOIN LuogoAeroporto nest_lurto
            ON nest_ap.partenza = nest_lurto.aeroporto
    WHERE nest_lurto.citta = 'Roma'
);

--3. Quali sono i piani di volo, con al più
--due scali intermedi, da ‘FCO’ a ‘JFK’? 
--Per ogni piano di volo restituire la sequenza di voli previsti 
--(con aeroporto di partenza, compagnia, codice volo, 
--aeroporto di arrivo) e la durata complessiva. 
--Evitare di restituire piani di volo ‘degeneri’, 
--ovvero che facciano tappa intermedia a FCO 
--o due volte nello stesso aeroporto. 
--Ordinare il risultato per durata complessiva del piano di volo.

SELECT CONCAT(ap.partenza,', ', ap.comp,', ', ap.codice,', ', ap.arrivo) AS piano_di_volo,
       volo.durataMinuti AS durata_complessiva
FROM ArrPart ap
    JOIN Volo volo
        ON volo.codice = ap.codice
WHERE ap.partenza = 'FCO'
  AND ap.arrivo = 'JFK'
UNION
SELECT CONCAT(ap1.partenza,', ', ap1.comp,', ', ap1.codice,', ', ap1.arrivo,' => ',
			  ap2.partenza,', ', ap2.comp,', ', ap2.codice,', ', ap2.arrivo) AS piano_di_volo,
	   (volo1.durataMinuti + volo2.durataMinuti) AS durata_complessiva
FROM ArrPart ap1
    JOIN Volo volo1
        ON volo1.codice = ap1.codice
	JOIN ArrPart ap2
		ON ap1.arrivo = ap2.partenza
	JOIN Volo volo2
		ON volo2.codice = ap2.codice
WHERE ap1.partenza = 'FCO'
  AND ap2.arrivo = 'JFK'
UNION
SELECT CONCAT(ap1.partenza,', ', ap1.comp,', ', ap1.codice,', ', ap1.arrivo,' => ',
			  ap2.partenza,', ', ap2.comp,', ', ap2.codice,', ', ap2.arrivo,' => ',
			  ap3.partenza,', ', ap3.comp,', ', ap3.codice,', ', ap3.arrivo) AS piano_di_volo,
	   (volo1.durataMinuti + volo2.durataMinuti + volo3.durataMinuti) AS durata_complessiva
FROM ArrPart ap1
    JOIN Volo volo1
        ON volo1.codice = ap1.codice
	JOIN ArrPart ap2
		ON ap1.arrivo = ap2.partenza
	JOIN Volo volo2
		ON volo2.codice = ap2.codice
	JOIN ArrPart ap3
		ON ap2.arrivo = ap3.partenza
	JOIN Volo volo3
		ON volo3.codice = ap3.codice
WHERE ap1.partenza = 'FCO'
  AND ap3.arrivo = 'JFK'
  AND ap3.partenza <> 'FCO'
  AND ap2.partenza <> 'JFK'
ORDER BY durata_complessiva ASC;