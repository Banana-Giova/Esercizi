--Query No.1)

SELECT volo.comp AS Compagnia, 
       AVG(volo.durataMinuti) AS durata_media
FROM Volo AS volo
    JOIN ArrPart ap
        ON volo.codice = ap.codice 
        AND volo.comp = ap.comp
    JOIN Aeroporto aero
        ON ap.partenza = aero.codice
    JOIN LuogoAeroporto lurto 
        ON aero.codice = lurto.aeroporto
WHERE lurto.nazione = 'Italy'
GROUP BY volo.comp

--Query No.2)

WITH durata_totale AS (
    SELECT sum(v.durataMinuti) AS som_dur, 
           volo.codice
    FROM Volo 
        AS volo
    GROUP BY volo.codice
    )

SELECT DISTINCT volo.comp, 
                AVG(volo.durataMinuti)
FROM durata_totale AS duratot, 
     Volo AS volo,
     ArrPart AS ap
WHERE volo.codice = ap.codice
AND volo.comp = ap.comp
GROUP BY volo.comp
HAVING AVG(dt.som_dur) < AVG(v.durataMinuti)

--Query No.3)

WITH num_voli AS (
    SELECT lurto.citta, 
           COUNT(ap.arrivo) AS numero_arrivi
    FROM ArrPart AS ap, 
         LuogoAeroporto AS lurto
    WHERE ap.arrivo = lurto.aeroporto 
    GROUP BY lurto.citta
),
media_voli AS (

    SELECT AVG(num_voli.numero_arrivi) AS tot_arr
    FROM num_voli
)

SELECT nuvo.citta, 
       nuvo.numero_arrivi
FROM num_voli AS nuvo, 
     media_voli AS nume
WHERE nuvo.numero_arrivi > nume.tot_arr;

--Query No.4)

WITH part_da_ita AS (
    SELECT ap.comp, 
           AVG(volo.durataMinuti) AS partenza_media
    FROM LuogoAeroporto AS lurto, 
         ArrPart AS ap, 
         Volo AS volo
    WHERE lurto.aeroporto = ap.partenza
    AND volo.codice = ap.codice
    AND lurto.nazione = 'Italy'
    GROUP BY ap.comp
),
media_tot AS ( 
    SELECT AVG(volo.durataMinuti) AS med_voli
    FROM LuogoAeroporto AS lurto, 
         ArrPart AS ap, 
         Volo AS volo
    WHERE lurto.aeroporto = ap.partenza
    AND volo.codice = ap.codice
    AND lurto.nazione = 'Italy'
    )
SELECT part.comp, 
       mt.med_voli
FROM part_da_ita AS part, 
     media_tot AS mt
WHERE part.partenza_media < mt.med_voli

--Query No.5)

WITH media_voli AS (
SELECT lurto.citta, 
       AVG(v.durataMinuti) AS dur_med
FROM LuogoAeroporto AS lurto, 
     Volo AS volo, 
     ArrPart AS ap
WHERE ap.codice = volo.codice
AND ap.arrivo = lurto.aeroporto
GROUP BY lurto.citta
),
media_tot_voli AS (
SELECT v.durataMinuti AS sum_tot
FROM Volo AS volo 
)
SELECT mv.citta, 
       mv.dur_med
FROM media_voli AS mv, 
     media_tot_voli AS mtv, 
     Volo AS volo
GROUP BY mv.citta , mv.dur_med 
HAVING mv.dur_med > (AVG(mtv.sum_tot) + STDDEV_SAMP(v.durataMinuti))
    OR  mv.dur_med < (AVG(mtv.sum_tot) - STDDEV_SAMP(v.durataMinuti))

--Query No.6)

WITH num_citta AS (
    SELECT nazione,aeroporto, 
           COUNT(citta) AS n_citta
    FROM LuogoAeroporto 
    GROUP BY nazione , aeroporto 
)
SELECT DISTINCT nc.nazione, nc.n_citta
FROM LuogoAeroporto AS lurto1,
     LuogoAeroporto AS lurto2,
     ArrPart AS ap,
     num_citta AS nc
WHERE ap.partenza = lurto1.aeroporto
AND lurto2.aeroporto = ap.arrivo
AND lurto1.nazione <> lurto2.nazione
AND lurto1.aeroporto <> lurto2.aeroporto
AND nc.aeroporto = ap.partenza