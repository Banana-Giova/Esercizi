def is_palindrome(x: int) -> bool:
    """

    Dato un intero x, restituisce True se x è
    palindromo, e False altrimenti

    Esempio 1:
    x = 121 -> True
    Spigazione: 121 si legge come 121 sia da destra che da sinistra.

    Esempio 2:
    x = -121 -> False
    Spiegazione: Da sinistra a destra leggiamo -121.
    Da destra a sinistra leggiamo 121-, perciò non è palindromo.

    Esempio 3:
    x = 10 -> False
    Speigazione: 01 da destra a sinistra.
    Perciò non è palindromo

    """
    x_string:str = str(x)
    x_list:list = list(x_string)      #trasformo prima l'int in str e poi in lista
    rev_x_list:list = []
    for i in x_list:
        rev_x_list.insert(0, i)

    return x_list == rev_x_list       #risultato in bool del dilemma: palindromo o no?

if False:
    print(is_palindrome(121))