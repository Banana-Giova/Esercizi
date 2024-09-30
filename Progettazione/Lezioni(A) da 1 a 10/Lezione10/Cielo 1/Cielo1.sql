--1. Quali sono i voli (codice e nome della compagnia) 
--   la cui durata supera le 3 ore?

SELECT codice, comp
FROM Volo
WHERE durataMinuti > 180;

--2. Quali sono le compagnie che hanno voli 
--   che superano le 3 ore?

SELECT DISTINCT comp
FROM Volo
WHERE durataMinuti > 180;

--3. Quali sono i voli (codice e nome della compagnia) 
--   che partono dall’aeroporto con codice ‘CIA’ ?

SELECT codice, comp
FROM ArrPart
WHERE partenza = 'CIA';

--4. Quali sono le compagnie che hanno voli 
--   che arrivano all’aeroporto con codice ‘FCO’ ?

SELECT DISTINCT comp
FROM ArrPart
WHERE arrivo = 'FCO';

--5. Quali sono i voli (codice e nome della compagnia) 
--   che partono dall’aeroporto ‘FCO’
--   e arrivano all’aeroporto ‘JFK’ ?

SELECT codice, comp
FROM ArrPart
WHERE partenza = 'FCO'
    AND arrivo = 'JFK';

--6. Quali sono le compagnie che hanno voli che partono 
-- dall’aeroporto ‘FCO’ e atterrano all’aeroporto ‘JFK’ ?

SELECT DISTINCT comp
FROM ArrPart
WHERE partenza = 'FCO'
    AND arrivo = 'JFK';

--7. Quali sono i nomi delle compagnie che hanno voli
--   diretti dalla città di ‘Roma’ alla città di ‘New York’ ?

SELECT DISTINCT ArrPart.comp
FROM ArrPart, LuogoAeroporto AS partenza, LuogoAeroporto as arrivo
WHERE ( partenza.citta = 'Roma'
        AND partenza.aeroporto = ArrPart.partenza )
    AND ( arrivo.citta = 'New York'
        AND arrivo.aeroporto = ArrPart.arrivo );

--8. Quali sono gli aeroporti (con codice IATA, nome e luogo) 
--   nei quali partono voli della compagnia di nome ‘MagicFly’ ?

SELECT Aeroporto.codice, Aeroporto.nome, LuogoAeroporto.citta
FROM Aeroporto, LuogoAeroporto, ArrPart
WHERE ArrPart.comp = 'MagicFly'
    AND ArrPart.partenza = Aeroporto.codice
    AND ArrPart.partenza = LuogoAeroporto.aeroporto

--9. Quali sono i voli che partono da un qualunque aeroporto 
--   della città di ‘Roma’ e atterrano ad un qualunque aeroporto 
--   della città di ‘New York’ ? Restituire: codice del volo, 
--   nome della compagnia, e aeroporti di partenza e arrivo.

SELECT ArrPart.codice, ArrPart.comp, aeroporto_partenza.nome, aeroporto_arrivo.nome
FROM ArrPart, 
     LuogoAeroporto AS luogo_partenza, LuogoAeroporto AS luogo_arrivo,
     Aeroporto AS aeroporto_partenza, Aeroporto AS aeroporto_arrivo
WHERE ( luogo_partenza.citta = 'Roma'
        AND luogo_partenza.aeroporto = aeroporto_partenza.codice
        AND luogo_partenza.aeroporto = ArrPart.partenza )
    AND ( luogo_arrivo.citta = 'New York'
        AND luogo_arrivo.aeroporto = aeroporto_arrivo.codice
        AND luogo_arrivo.aeroporto = ArrPart.arrivo );

--10. Quali sono i possibili piani di volo con esattamente 
--    un cambio (utilizzando solo voli della stessa compagnia) 
--    da un qualunque aeroporto della città di ‘Roma’ ad un 
--    qualunque aeroporto della città di ‘New York’ ? 
--    Restituire: nome della compagnia, codici dei voli, 
--    e aeroporti di partenza, scalo e arrivo.

SELECT primo_volo.comp AS compagnia, 
       primo_volo.codice AS codice_volo_1, 
       aeroporto_partenza.nome AS partenza_da,
       aeroporto_scalo.nome AS scalo_a,
       secondo_volo.codice AS codice_volo_2,
       aeroporto_arrivo.nome AS arrivo_a
FROM ArrPart primo_volo, 
     ArrPart secondo_volo, 
     Aeroporto aeroporto_partenza, 
     Aeroporto aeroporto_scalo, 
     Aeroporto aeroporto_arrivo,
     LuogoAeroporto luogo_partenza,
     LuogoAeroporto luogo_arrivo
WHERE primo_volo.comp = secondo_volo.comp
  AND luogo_partenza.citta = 'Roma'
  AND luogo_partenza.aeroporto = aeroporto_partenza.codice
  AND primo_volo.partenza = aeroporto_partenza.codice
  AND primo_volo.arrivo = aeroporto_scalo.codice
  AND secondo_volo.partenza = aeroporto_scalo.codice
  AND secondo_volo.arrivo = aeroporto_arrivo.codice
  AND luogo_arrivo.aeroporto = aeroporto_arrivo.codice
  AND luogo_arrivo.citta = 'New York';

--11. Quali sono le compagnie che hanno voli che partono 
--    dall’aeroporto ‘FCO’, atterrano all’aeroporto ‘JFK’, 
--    e di cui si conosce l’anno di fondazione?

SELECT DISTINCT compagnia.nome AS nome_compagnia
FROM ArrPart ap,
     Compagnia compagnia
WHERE ap.partenza = 'FCO'
  AND ap.arrivo = 'JFK'
  AND ap.comp = compagnia.nome
  AND compagnia.annoFondaz IS NOT NULL;

--Non scordarti 'IS'!