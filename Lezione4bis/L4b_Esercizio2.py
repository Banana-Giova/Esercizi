#Giovanni di Giuseppe   22/04/2024

def lenght_of_last_word(s:str) -> int:
    """
        
        Data una stringa s che contiene parole e spazi,
        restituire la lunghezza dell'ultima parola in s.

        Una parola è una sottostringa che contiene
        caratteri contigui diversi dallo spazio.

        Esempio 1:
        s = "Hello World" -> restituire 5
        Spigazione: L'ultima parola è "World" che ha lunghezza 5

        Esempio 2:
        s = "    fly me     to    the moon   " -> restituire 4
        Spiegazione: L'ultima parola è "moon" che ha lunghezza 4

        Esempio 3:
        s = "luffy is still a joyboy" -> restituire 6
        Spiegazione: L'ultima parola è "joyboy" che ha lunghezza 6
    
    """
    
    s_strip:str = s.strip(" ")      #strip della stringa originale per rimuovere eventuali spazi in eccesso
    s_list:list = s_strip.split(" ")       #split della stringa in una lista di stringhe
    return(len(s_list[-1]))

if False:
    print(lenght_of_last_word("Hello      World         "))