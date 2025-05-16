import pandas as pd
import numpy as np
from typing import Tuple
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from calendar import month_abbr

class DataSourceConfig:
    db_uri: str = ""
    csv_path: str = "" 
    excel_path: str = ""    
    output_plot_p2: str = ""
    output_plot_p5: str = ""    

class DataPipeline:

    def __init__(self, config: DataSourceConfig):
        self.config = config
        self.data = None
        
    def load_from_csv(self) -> pd.DataFrame:
        """Carica dati da un file CSV"""
        df = pd.read_csv(self.config.csv_path)
        return df
    
    def load_from_excel(self) -> pd.DataFrame:
        """Carica dati da un fmenisili per nazione
        monthly_counts = (df.groupby(['Country', 'Month'])['InvoiceNo']
                          .nunique()
                          .reset_ile Excel"""
        return pd.read_excel(self.config.excel_path)    
        
    def load_from_database_one(self) -> pd.DataFrame:
        """Carica dati da una tabella di un database"""        
        df = pd.DataFrame()
        return df
    
    def load_from_database_two(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Carica dati da due tabelle di un database"""
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        return df1, df2
 
    def preprocess_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Pulisci e prepara i dati per l'analisi"""
        # Conversione automatica tipi di dato

        # Ridenominazione colonna

        # Rimozione righe con quantità negative

        # Esempio ulteriore di pre-processamento/pulizia: Calcolo del prezzo totale per prodotto in fattura

        # Esempio ulteriore di pre-processamento/pulizia: Rimozione righe con valori mancanti in campi importanti
        
        # Esempio ulteriore di pre-processamento/pulizia: Mantenimento del solo primo pease di coppie di paesi spearati da virgola osservate

        # Rimozione righe con paese non specificato

        # Esclusione di dati UK

        # # Esempio ulteriore di pre-processamento/pulizia: Inclusione di dati di un solo paese

        df = pd.DataFrame()
        return df

    def esrcz1_proportion_top100_products(self, df_in: pd.DataFrame) -> None:
        """Calcola e visualizza la ripartizione per numero di fatture dei 100 prodotti più venduti"""
   
    
    def esrcz2_monthly_invoices_by_country(self, df_in: pd.DataFrame) -> None:
        """Calcola e visualizza il numero delle fatture mensili totali per nazione"""
    
    def run_pipeline(self) -> pd.DataFrame:
        """Esegui la pipeline di analisi dati"""  
        print("   Svolgere i due esercizi proposti implementando le varie fasi del processo di analisi dati ;-)")
        return(pd.DataFrame())

if __name__ == "__main__":
    config = DataSourceConfig() 
    # Esegui la pipeline
    pipeline = DataPipeline(config)
    print("Pipeline avviata...")
    final_df = pipeline.run_pipeline()
    print("Pipeline completata con successo!")
    # print(final_df.head())