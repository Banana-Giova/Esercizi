BEGIN TRANSACTION;
SET CONSTRAINTS ALL DEFERRED;

INSERT INTO Utente(cf, nome, cognome)
VALUES
('DGSGNN02H501J', 'Giovanni', 'di Giuseppe'),
('MNNLNR02H501J', 'Eleonora', 'Mannucci');

INSERT INTO Veicolo(targa)
VALUES
('DYZ07K2'),
('M3G451U')

INSERT INTO Noleggio(utente, veicolo, inizio, is_terminato, fine)
VALUES
('DGSGNN02H501J', 'DYZ07K2', '2024-12-08 15:03:43', False, NULL),
('DGSGNN02H501J', 'DYZ07K2', '2023-11-07 15:03:43', True, '2024-11-07 15:03:43')

INSERT INTO Sinistro(istante, veicolo)
VALUES
('2024-12-08 15:03:43', 'DYZ07K2');

COMMIT;