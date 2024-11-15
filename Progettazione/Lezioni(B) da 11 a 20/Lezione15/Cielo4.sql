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
WHERE (part.comp = 'Apitalia' OR arr.comp = 'Apitalia')
  AND lurto.citta IN (
  	  SELECT lurto1.citta
      FROM LuogoAeroporto lurto1
          JOIN Aeroporto aero1
              ON lurto1.aeroporto = aero1.codice
      GROUP BY lurto1.citta
      HAVING COUNT(lurto1.citta) > 1
      );

--3. Quali sono le coppie di aeroporti (A, B) 
--tali che esistono voli tra A e B ed il numero
--di voli da A a B è uguale al numero di voli da B ad A?

WITH ab_ba AS (
    SELECT ap.partenza rtenza,
           ap.arrivo rrivo,
           COUNT(*) as num_voli
    FROM ArrPart ap
    GROUP BY ap.partenza, ap.arrivo
)
SELECT abba1.rtenza AS partenza,
       abba1.rrivo AS arrivo
FROM ab_ba abba1,
     ab_ba abba2
WHERE abba1.rtenza = abba2.rrivo
  AND abba1.rrivo = abba2.rtenza
  AND abba1.num_voli = abba2.num_voli;

--4. Quali sono le compagnie che hanno voli con durata media 
--maggiore della durata media di tutte le compagnie?

SELECT volo.comp AS compagnia
FROM Volo volo
GROUP BY volo.comp
HAVING AVG(volo.durataMinuti) > (
        SELECT AVG(volo.durataMinuti)
        FROM Volo volo
    );

--5. Quali sono gli aeroporti da cui partono voli 
--per almeno 2 nazioni diverse?

/* Versione Errata:

SELECT part_luo.aeroporto
FROM ArrPart ap
    JOIN LuogoAeroporto part_luo
        ON ap.partenza = part_luo.aeroporto
    JOIN LuogoAeroporto arr_luo
        ON ap.arrivo = arr_luo.aeroporto
WHERE EXISTS (
        SELECT part_luo.aeroporto
        FROM LuogoAeroporto nest_arr
		WHERE part_luo.nazione <> nest_arr.nazione
        GROUP BY part_luo.aeroporto
        HAVING COUNT(nest_arr.nazione) >= 2
    )
GROUP BY part_luo.aeroporto;*/

SELECT part_luo.aeroporto
FROM ArrPart ap
    JOIN LuogoAeroporto part_luo
        ON ap.partenza = part_luo.aeroporto
WHERE EXISTS (
        SELECT nest_arr.nazione
        FROM LuogoAeroporto nest_arr
		WHERE part_luo.nazione <> nest_arr.nazione
        GROUP BY nest_arr.nazione
        HAVING COUNT(nest_arr.nazione) >= 2
    )
GROUP BY part_luo.aeroporto;

--6. Quali sono i voli che partono dalle città 
--con un unico aeroporto? Restituire codice
--dei voli, compagnie, e gli aeroporti di partenza e di arrivo.

SELECT ap.codice AS codice,
       ap.comp AS compagnia,
       ap.partenza AS partenza,
       ap.arrivo AS arrivo
FROM ArrPart ap
    JOIN LuogoAeroporto lurto
        ON ap.partenza = lurto.aeroporto
WHERE lurto.citta IN (
        SELECT nest_lurto.citta AS citta
        FROM LuogoAeroporto nest_lurto
        GROUP BY nest_lurto.citta
        HAVING COUNT(nest_lurto.aeroporto) = 1
    );

--7. Quali sono gli aeroporti raggiungibili dall’aeroporto “JFK” 
--tramite voli diretti e indiretti?

SELECT DISTINCT ap.arrivo AS aeroporti
FROM ArrPart ap
WHERE ap.partenza = 'JFK'
   OR ap.partenza IN (
    SELECT DISTINCT nest_ap.arrivo
    FROM ArrPart nest_ap
    WHERE nest_ap.partenza = 'JFK'
);

--8. Quali sono le città raggiungibili 
--con voli diretti e indiretti partendo da Roma?

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

--9. Quali sono le città raggiungibili con esattamente 
--uno scalo intermedo partendo dall’aeroporto “JFK”?

SELECT DISTINCT lurto.citta
FROM ArrPart ap
    JOIN LuogoAeroporto lurto
        ON ap.arrivo = lurto.aeroporto
WHERE ap.partenza <> 'JFK'
  AND ap.partenza IN (
    SELECT nest_ap.arrivo
    FROM ArrPart nest_ap
    WHERE nest_ap.partenza = 'JFK'
  );