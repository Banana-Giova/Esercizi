#with open('data/Badassium.txt') as gargarozz:
#    print(gargarozz.readline())

"""
In alternativa si può usare
|
V

try:
    print("Sono nel try")
except:
    print("Sono nel'Except")
finally:
    print("Sono nel finally")
"""

class DatabaseConnection:
    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.db.connect()
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.db.rollback()
        else:
            self.db.commt()

        self.db.disconnect()
        return False

    def connect(self):
        self.connection = f"Connection to the database: {self.db_name}"
        print(self.connection)

    def disconnect(self):
        print(f"Disconnection to the database: {self.db_name}")
        self.connection = None

    def commit(self):
        print("Committing transaction")

    def rollback(self):
        print("Rolling back transaction")

    def execute_query(self, query):
        print("Executing query")
        return f"Results of {query}"
    
#Decorators

def ciao(name:str):
    return f"Ciao {name}!"

def saluta_danielone(func):
    return func("Danielone")

print(saluta_danielone(ciao))