from CodificatoriMessaggio import *

augusto:CifratoreAScorrimento = CifratoreAScorrimento(6)
ottaviano:CifrarioACombinazione = CifrarioACombinazione(6)


gerrys = augusto.codifica("Signori, buonasera!")
print(gerrys)
print(augusto.decodifica(gerrys))

carlos = ottaviano.codifica("Io sono Caparezza! Vengo dalla monnezza!")
print(carlos)
print(ottaviano.decodifica(carlos))

if False:
    caparezza = 'caparezza.txt'
    print(augusto.leggiDaFile(caparezza))
    augusto.decodificaSuFile(caparezza)