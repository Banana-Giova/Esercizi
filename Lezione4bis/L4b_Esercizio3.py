def convert_to_title(col_number:int) -> str:
    """

        Dato un intero col_number, restituire il suo corrispondente
        titolo di colonna come ad esempio compare su un foglio Excel

        Esempio 1:
        col_number = 1 -> restituire "A"
        col_number = 2 -> restituire "B"
        col_number = 26 -> restituire "Z"

        Esempio 2:
        col_number = 27 -> restituire "AA"
        col_number = 28 -> restituire "AB"

        Esempio 3:
        col_number = 701 -> restituire "ZY"
    
    """

    result:str = ""

    while col_number > 0:
        resto:int = (col_number - 1) % 26
        result = chr(resto + ord("A")) + result
        col_number = (col_number - 1) // 26
    return result