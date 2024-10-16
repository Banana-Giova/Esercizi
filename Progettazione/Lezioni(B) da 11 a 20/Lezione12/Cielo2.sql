--1. Quante sono le compagnie che operano 
--(sia in arrivo che in partenza) nei diversi aeroporti?

SELECT aero.nome AS nome_aeroporto,
       aero.codice AS codice_aeroporto,
       COUNT(DISTINCT ap.comp) AS numero_compagnie
FROM Aeroporto aero, 
     ArrPart ap
WHERE ap.partenza = aero.codice
   OR ap.arrivo = aero.codice
GROUP BY aero.codice;

--2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ 
--e hanno una durata di almeno 100 minuti?

SELECT COUNT(*) AS numero_voli
FROM ArrPart ap
    JOIN Volo Volo
        ON volo.codice = ap.codice
WHERE ap.partenza = 'HTR'
  AND volo.durataMinuti >= 100;

--3. Quanti sono gli aeroporti sui quali opera 
--la compagnia ‘Apitalia’, per ogni nazione nella quale opera?

SELECT lurto.nazione AS nazione,
       COUNT(DISTINCT lurto.aeroporto) AS numero_aeroporti
FROM ArrPart ap,
     LuogoAeroporto lurto
WHERE ap.comp = 'Apitalia'
  AND (ap.partenza = lurto.aeroporto
   OR ap.arrivo = lurto.aeroporto)
GROUP BY lurto.nazione;

--4. Qual è la media, il massimo e il minimo 
--della durata dei voli effettuati dalla compagnia ‘MagicFly’ ?

SELECT AVG(volo.durataMinuti) AS durata_media,
       MAX(volo.durataMinuti) AS durata_massima,
       MIN(volo.durataMinuti) AS durata_minima
FROM ArrPart ap
    JOIN Volo volo
        ON ap.codice = volo.codice
WHERE ap.comp = 'MagicFly';

--5. Qual è l’anno di fondazione della compagnia 
--più vecchia che opera in ognuno degli aeroporti?

SELECT aero.nome AS nome_aeroporto,
       aero.codice AS codice_aeroporto,
       MIN(comp.annoFondaz)
FROM Aeroporto aero,
     ArrPart ap
    JOIN Compagnia comp
        ON ap.comp = comp.nome
WHERE comp.annoFondaz IS NOT NULL
  AND (ap.partenza = aero.codice
       OR ap.arrivo = aero.codice)
GROUP BY aero.codice;

--6. Quante sono le nazioni (diverse) raggiungibili 
--da ogni nazione tramite uno o più voli?

SELECT lupart.nazione AS nazione,
       COUNT(DISTINCT luarr.nazione) AS nazioni_raggiungibili
FROM ArrPart ap
    JOIN LuogoAeroporto lupart
        ON ap.partenza = lupart.aeroporto
    JOIN LuogoAeroporto luarr
        ON ap.arrivo = luarr.aeroporto
WHERE luarr.nazione <> lupart.nazione
GROUP BY lupart.nazione;

--7. Qual è la durata media dei voli che partono 
--da ognuno degli aeroporti?

SELECT aero.nome AS nome_aeroporto,
       aero.codice AS codice_aeroporto,
       AVG(volo.durataMinuti) AS durata_media_volo
FROM Aeroporto aero
    JOIN ArrPart ap
        ON aero.codice = ap.partenza
        JOIN Volo volo
            ON volo.codice = ap.codice
WHERE TRUE
GROUP BY aero.codice;

--8. Qual è la durata complessiva dei voli operati 
--da ognuna delle compagnie fondate a partire dal 1950?

SELECT comp.nome AS nome_compagnia,
       SUM(volo.durataMinuti) AS durata_media_volo
FROM Volo volo
    JOIN Compagnia comp
        ON volo.comp = comp.nome
WHERE comp.annoFondaz IS NOT NULL
  AND comp.annoFondaz >= 1950
GROUP BY comp.nome;

--9. Quali sono gli aeroporti nei quali operano 
--esattamente due compagnie?

SELECT aero.nome AS nome_aeroporto,
       aero.codice AS codice_aeroporto
FROM Aeroporto aero,
     ArrPart ap
WHERE ap.partenza = aero.codice
   OR ap.arrivo = aero.codice
GROUP BY aero.codice
HAVING COUNT(DISTINCT ap.comp) = 2;

--10. Quali sono le città con almeno due aeroporti?

SELECT lurto.citta AS citta
FROM Aeroporto aero
    JOIN LuogoAeroporto lurto
        ON lurto.aeroporto = aero.codice
WHERE TRUE
GROUP BY lurto.citta
HAVING COUNT(DISTINCT lurto.aeroporto) > 1;

--11. Qual è il nome delle compagnie i cui voli hanno 
--una durata media maggiore di 6 ore?

SELECT comp.nome AS nome_compagnia
FROM Volo volo
    JOIN Compagnia comp
        ON volo.comp = comp.nome
WHERE TRUE
GROUP BY comp.nome
HAVING AVG(volo.durataMinuti) > 360;

--12. Qual è il nome delle compagnie i cui voli hanno 
--tutti una durata maggiore di 100 minuti?

SELECT comp.nome AS nome_compagnia
FROM Volo volo
    JOIN Compagnia comp
        ON volo.comp = comp.nome
WHERE TRUE
GROUP BY comp.nome
HAVING MIN(volo.durataMinuti) > 100;