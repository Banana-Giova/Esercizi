import pandas as pd
import numpy as np
from typing import Tuple
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from calendar import month_abbr

class DataSourceConfig:
    db_uri: str = "postgresql+psycopg://postgres:postgres@postgresql:5432/retail_db"
    csv_path: str = "../../dati/retail/sales_all_months_2011.csv"    
    output_plot_1: str = "../../visual/retail/plot_esrcz1.png"
    output_plot_2: str = "../../visual/retail/plot_esrcz2.png"    

class DataPipeline:

    def __init__(self, config: DataSourceConfig):
        self.config = config
        self.data = None
        
    def load_from_csv(self) -> pd.DataFrame:
        """Carica dati da un file CSV"""
        df = pd.read_csv(self.config.csv_path)
        # Studio dati caricati da file CSV
        # print(df.dtypes)
        # print(df.info)
        # print(df.shape)
        # print(df.describe())
        return df
    
    def load_from_excel(self) -> pd.DataFrame:
        """Carica dati da un file Excel"""
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
        df = df.convert_dtypes() 
        # Ridenominazione colonna
        df.rename(columns={'Month (Number)': 'Month'}, inplace=True)
        # Rimozione righe con quantità negative
        df = df[df['Quantity'] > 0]
        # # Esempio ulteriore di pre-processamento/pulizia: Calcolo del prezzo totale per prodotto in fattura
        # df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
        # # Esempio ulteriore di pre-processamento/pulizia: Rimozione righe con valori mancanti in campi importanti
        # df = df.dropna(subset=['StockCode', 'CustomerID', 'Country', 'InvoiceDate'])
        # # Esempio ulteriore di pre-processamento/pulizia: Mantenimento del solo primo pease di coppie di paesi spearati da virgola osservate
        # df['Country'] = df['Country'].str.split(',').str[0].str.strip()
        # Rimozione righe con paese non specificato
        df = df[df['Country'] != "Unspecified"]
        # Esclusione di dati UK
        df = df[df['Country'] != "United Kingdom"]
        # # Esempio ulteriore di pre-processamento/pulizia: Inclusione di dati di un solo paese
        # df = df[df['Country'] == "Italy"]     
        return df

    def esrcz1_proportion_top100_products(self, df_in: pd.DataFrame) -> None:
        """Calcola e visualizza la ripartizione per numero di fatture dei 100 prodotti più venduti"""
        # Lavora solo su copia locale dei dati in ingresso
        df = df_in.reset_index(drop=True).copy()
        # Recupero solo dei principali 100 prodotti per numero di fatture in cui compaiono
        df_agg = df.groupby('StockCode').agg(InvoiceCount=('InvoiceNo', 'count'))
        top_products = df_agg.sort_values(by='InvoiceCount', ascending=False).head(100)
        ## Soluzione alternativa e compatta alle due righe sopra
        # top_products = df.groupby('StockCode')['InvoiceNo'].count().nlargest(100).reset_index()
        # Calcolo dei contenitori/intervalli di frequenza e i relativi conteggi
        count, bin_edges = np.histogram(top_products['InvoiceCount'])
        # Visualizzazione
        plt.figure(figsize=(12, 8))
        # top_products.plot(kind='hist', color='green', figsize=(12, 8))
        # top_products.plot(kind='hist', xticks=bin_edges, color='green', figsize=(12, 8))
        # plt.hist(x=top_products['InvoiceNo'], color='green')
        plt.hist(x=top_products['InvoiceCount'], color='green')                             
        plt.title('Esercizio 1 - Ripartizione, per Numero di Fatture, dei 100 Prodotti più Venduti')
        plt.xlabel('Numero di Fatture')
        plt.ylabel('Percentuale di Prodotti Top 100 (%)')
        plt.xticks(bin_edges)
        plt.annotate(text='Es. '+str(count[0])+'% dei 100 prodotti più venduti compaiono\n'+ 
                     'in un numero di fatture compreso tra '+str(bin_edges[0])+' e '+str(bin_edges[1]), 
                     xy=(300,50)), # testo da mostrare
        plt.tight_layout()
        plt.show()
        plt.savefig(self.config.output_plot_1)
        plt.close()     
    
    def esrcz2_monthly_invoices_by_country(self, df_in: pd.DataFrame) -> None:
        """Calcola e visualizza il numero delle fatture mensili totali per nazione"""
        # Lavora solo su copia locale dei dati in ingresso
        df = df_in.reset_index(drop=True).copy()               
        # Conteggio delle fatture menisili per nazione
        monthly_counts = (df.groupby(['Country', 'Month'])['InvoiceNo']
                          .nunique()
                          .reset_index()
                          .rename(columns={'InvoiceNo': 'InvoiceCount'}))
        # Selezione di tutti le nazioni
        complete_countries = (monthly_counts.groupby('Country')['Month']
                            .nunique()
                            .index.tolist())
        # Visualizzzazione
        plt.figure(figsize=(12, 8))
        # Creazione di una line plot per ogni nazione
        for country in complete_countries:
            country_data = monthly_counts[monthly_counts['Country'] == country]
            plt.plot(country_data['Month'], country_data['InvoiceCount'], 
                    # marker='o', label=country)
                    label=country)          
        # Formattazione
        plt.title('Esercizio 2 - Conteggio Fatture Mensili per Nazione')
        plt.xlabel('Mese')
        plt.ylabel('Numero di Fatture')
        plt.xticks(range(1, 13), [month_abbr[i] for i in range(1, 13)])
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
        plt.savefig(self.config.output_plot_2)
        plt.close()        
        # # Stampa i paese inclusi
        # print(f"Paesi considerati con dati mensili sulle fatture: {', '.join(complete_countries)}")
    
    def run_pipeline(self) -> pd.DataFrame:
        """Esegui la pipeline di analisi dati"""    
        csv_df = self.load_from_csv()
        print("   Letti dati da un file CSV") 
        cleaned_df = self.preprocess_data(csv_df)
        print("   Pre-processamento e pulizia dati completati")
        print("   Esecuzione Esercizio 1: Ripartizione, per Numero di Fatture, dei 100 prodotti più venduti")
        self.esrcz1_proportion_top100_products(cleaned_df)
        print("   Esecuzione Esercizio 2: Conteggio Fatture Mensili per Nazione")
        self.esrcz2_monthly_invoices_by_country(cleaned_df) 
        return(cleaned_df)

if __name__ == "__main__":
    config = DataSourceConfig() 
    # Esegui la pipeline
    pipeline = DataPipeline(config)
    print("Pipeline avviata...")
    final_df = pipeline.run_pipeline()
    print("Pipeline completata con successo!")
    # print(final_df.head())