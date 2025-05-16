import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import matplotlib.pyplot as plt


class DataSourceConfig:
    db_uri: str = "postgresql+psycopg://postgres:postgres@postgresql:5432/titanic_db"

class DataPipeline:
    def __init__(self, config:DataSourceConfig, csv_paths:tuple[str]):
        try:
            self.config = config
            self.csv_paths = csv_paths
        except Exception as e:
            print("Errore durante l'inizializzaione:\n" + e)

    def load_csv(self):
        try:
            csv_path1, csv_path2, csv_path3 = self.csv_paths
            self.df_c1 = pd.read_csv(csv_path1)
            self.df_c2 = pd.read_csv(csv_path2)
            self.df_c3 = pd.read_csv(csv_path3)
        except Exception as e:
            print("Errore durante il caricamento dei CSV:\n" + e)

    def rename_csv1_2(self):
        """--- 1) Sezione di ridenominazione delle colonne ---"""
        self.df_c1.rename(columns={'Col1':'CustomerID'}, inplace=True)
        self.df_c1.rename(columns={'Col2':'Country'}, inplace=True)

        self.df_c2.rename(columns={'Col1':'StockCode'}, inplace=True)
        self.df_c2.rename(columns={'Col2':'Description'}, inplace=True)

    def merge_data(self) -> pd.DataFrame:
        """--- 2) Sezione di aggregazione dei dati ---"""
        db_merged1_3 = pd.merge(self.df_c1, self.df_c3, on='CustomerID')
        return pd.merge(db_merged1_3, self.df_c2, on='StockCode')
    
    def DB_rw(self, df: pd.DataFrame):
        try:
            engine = create_engine(self.config.db_uri)
            SIMPLE_QUERY_1 = """
                            SELECT *
                            FROM public.transaction
                            """
            df.to_sql('transaction', engine, if_exists='replace', index=False)
            print("\nTabella salvata su PostgreSQL! Lettura in corso...\n")
            df_from_db = pd.read_sql_query(text(SIMPLE_QUERY_1), con=engine.connect())
            print(df_from_db)
        except Exception as e:
            print("Lettura da database fallita: " + e)

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """--- 3) Sezione di pulizia dati ---"""
              
        # 1. Sostituzione dei valori "bizzarri" del codice del prodotto
        #    (POST, "C2", "D", "M") con "?";

        bizzarri = np.array(['POST', 'C2', 'D', 'M'])
        df = df.replace(bizzarri, "?")

        # 2. Sostizione dei valori ambigui del nome della nazione
        #    (i.e. contenenti una virgola) con "?";

        df.loc[df['Country'].str.contains(',', na=False), 'Country'] = "?"

        # 3. Trasformazione dei "?" nel DataFrame in valori nulli;

        df = df.replace("?", np.nan)

        # 4. Rimozione righe con valori nulli nel codice del prodotto;

        df = df.dropna(subset=['StockCode'])

        # 5. Sostituzione righe con valori nulli nel nome della nazione
        #    con il valore più frequente di quella colonna;

        nome_frequente = df['Country'].mode()[0]
        df.loc[df['Country'].isna(), 'Country'] = nome_frequente

        # 6. Rimozione righe con paese non specificato ("Unspecified");

        df = df.loc[df['Country'] != 'Unspecified']

        # 7. Esclusione dati UK;

        df = df.loc[df['Country'] != 'United Kingdom']

        # 8. Rimozione righe con quantità negative;

        df = df.loc[df['Quantity'] < 0]

        # 9. Conversione automatica dei tipi di dato.

        df = df.convert_dtypes()

        return df
    
    def visualize_5_prods(self, df: pd.DataFrame) -> None:
        """--- 4.a) Sezione di visualizzazione ---"""
        top5 = df['StockCode'].value_counts().head(5)
        plt.figure(figsize=(10, 6))
        top5.plot(kind='bar',
                  color='gold',
                  edgecolor='grey')
        plt.title("5 prodotti più venduti per numero di fatture in cui compaiono.")
        plt.xlabel('Prodotto')
        plt.ylabel('N. di Fatture')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        plt.savefig("top5_fatture.png", dpi=150)
        plt.clf()

    def visualize_distribution(self, df: pd.DataFrame) -> None:
        """--- 4.b) Sezione di visualizzazione ---"""
        count_fatture = df['InvoiceNo'].value_counts()
        ax = count_fatture.plot(
            kind='pie',
            autopct=None,
            startangle=90,
            labels=None,
            title="Distribuzione delle fatture per numero di prodotti contenuti."
        )
        ax.set_ylabel("")
        plt.tight_layout()
        plt.show()
        plt.savefig("distribuzione_fatture.png", dpi=150)
        plt.clf()
        
    def run_pipeline(self) -> pd.DataFrame:
        """Esegue la pipeline completa"""
        self.load_csv()
        self.rename_csv1_2()
        print("Letti dati da più fonti (db, JSON)")
        merged_df = self.merge_data()
        print("Effettuata espansione dati (JSON -> nuove colonne)")        
        cleaned_df = self.clean_data(merged_df)
        print("Effettuata pulizia dati")
        self.data = cleaned_df
        return cleaned_df
        
if __name__ == "__main__":
    pipe_csv_tuple = (
        "/home/user/Scrivania/VSCodeProjects/Esercizi/IA/Esame/dati/retail/customer.csv",
        "/home/user/Scrivania/VSCodeProjects/Esercizi/IA/Esame/dati/retail/product.csv",
        "/home/user/Scrivania/VSCodeProjects/Esercizi/IA/Esame/dati/retail/transaction.csv"
    )

    config = DataSourceConfig()
    pipeline = DataPipeline(config, pipe_csv_tuple)
    final_df = pipeline.run_pipeline()
    pipeline.DB_rw(final_df)
    pipeline.visualize_5_prods(final_df)
    pipeline.visualize_distribution(final_df)
    print("Pipeline d'esame completata con successo!")