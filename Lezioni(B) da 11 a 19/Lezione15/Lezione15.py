"""
Esercizio 1

Crea un context manager usando una classe

Definisci una classe FileManager che implementa un context manager 
che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, 
__enter__ e la funzione  __exit__

Esempio di funzionamento:

 Il context manager deve permettere di aprire il file, 
 effettuare operazioni e chiudere la risorsa aperta.

 with FileManager('example.txt', 'w') as f:
     f.write('Hello, world!')
"""

class ContextManager:
    def __init__(self, file_name:str, mode:str) -> None:
        
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        print("Resource acquired")
        self.file_wrapper = open(self.file_name, self.mode)

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exception type: {exc_type}")
        print(f"Exception value: {exc_value}")
        print(f"Traceback: {traceback}")
        self.file_wrapper.close()
        print("Resource stored")

"""
Esercizio 2

Crea un context manager che permette di calcolare 
il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with

with Timer():

     time.sleep(1)

 time elapsed: 1.00000

 in questo esempio il tempo passato non sarà mai uguale a 1
"""
import time

class Timer:

    def __enter__(self):
        
        self.time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exception type: {exc_type}")
        print(f"Exception value: {exc_value}")
        print(f"Traceback: {traceback}")
        print(f"Time elapsed: {time.time() - self.time}")

with Timer():

    time.sleep(1)