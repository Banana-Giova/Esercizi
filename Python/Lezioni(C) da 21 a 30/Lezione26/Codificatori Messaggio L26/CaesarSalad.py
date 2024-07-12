from CodificatoriMessaggio import *

augusto:CifratoreAScorrimento = CifratoreAScorrimento(6)
ottaviano:CifrarioACombinazione = CifrarioACombinazione(6)

if False:
    gerrys = augusto.codifica("Signori, buonasera!")
    print(gerrys)
    print(augusto.decodifica(gerrys))

carlos = ottaviano.codifica("1234567")
print(carlos)