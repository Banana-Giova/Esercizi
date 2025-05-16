import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt


class DataPipeline:
    def __init__(self, json_path:str, csv_path:tuple[str]):
        try:
            self.json_path = json_path
            self.csv_path = csv_path
        except Exception as e:
            print("Errore durante l'inizializzaione:\n" + e)
    
    def load_json(self):
        try:
            self.df_json = pd.read_json(self.json_path)
        except Exception as e:
            print("Errore durante il caricamento del JSON:\n" + e)

    def load_csv(self):
        try:
            csv_path1, csv_path2 = self.csv_path
            self.df_c1 = pd.read_csv(csv_path1)
            self.df_c2 = pd.read_csv(csv_path2)
        except Exception as e:
            print("Errore durante il caricamento del CSV:\n" + e)

    def merge_data(self) -> pd.DataFrame:
        db_merged = pd.merge(self.df_c1, self.df_c2, on='PassengerId')
        return pd.merge(db_merged, self.df_json, on='PassengerId')
    
    def expand_json_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df['preferences'] = df['preferences'].apply(json.loads)
        prefs_expanded = pd.json_normalize(df['preferences'])
        return pd.concat([df.drop('preferences', axis=1), prefs_expanded], axis=1)
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Operazioni varie di pulizia dati"""
        
        # Studia il dataframe - Fase pre
        # ESERCIZIO 1 
        # Task: stampa i tipi del df e le colonne Age' ,'Fare', 'preferred_deck', 'dining_time', 'activity', 'Sex' 
        #       delle prime 10 ed ultime 5 righe        
        print(df.dtypes)

        cols = ['Age', 'Fare', 'preferred_deck', 'dining_time', 'activity', 'Sex']

        print(df[cols].head(10))
        print(df[cols].tail(5))
        
        # Sostituisce valori nulli/assenti con NaN
        # ESERCIZIO 2 
        # Task: sostituire i '?' con numpy NaNs        

        df = df.replace("?", np.nan)
        print("\n\nNaN inseriti e rimossi valori nulli\n\n")

        # Limita gli outliers
        # ESERCIZIO 3 
        # Task: stabilisci una soglia max di età ('Age') a cui riportare gli outliers (soglia_max=80)

        df['Age'] = df['Age'].clip(upper=80)

        # Sostituisce NaNs con il valor medio
        # ESERCIZIO 4
        # Task: applicare la sostituzione con il valor medio alle colonne 'Age' e 'Fare'        
        """   
        df['Age'] = df['Age'].replace(np.nan, df['Age'].mean())
        df['Fare'] = df['Fare'].replace(np.nan, df['Fare'].mean())
        
        Corretto, ma non idiomatico"""

        df['Age'] = df['Age'].fillna(df['Age'].mean())
        df['Fare'] = df['Fare'].fillna(df['Fare'].mean())
        
        # Sositutisce NaNs con valori random di colonne categoriche
        decks = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
        df["preferred_deck"] = df["preferred_deck"].apply(
            lambda x: np.random.choice(decks) if pd.isna(x) else x
        )
        times = np.array(['early', 'flexible', 'late'])
        df["dining_time"] = df["dining_time"].apply(
            lambda x: np.random.choice(times) if pd.isna(x) else x
        )
        
        # Sositutisce NaNs con il valore più frequente
        # ESERCIZIO 5 
        # Task: applicare alla colonna 'activity' la sostituzione con il valore più frequente        
        
        df['activity'] = df['Age'].fillna(df['activity'].mode()[0])

        # Correzione di errori per contenuti standard
        # ESERCIZIO 6 
        # Task: correggere 'mael' con 'male' e 'femael' con 'female' nella colonna 'Sex'        
        
        mapping = {
            'mael': 'male',
            'femael': 'female'
        }

        df['Sex'] = df['Sex'].replace(mapping)
        
        # Conversione dei tipi di dato
        df = df.convert_dtypes()
        # ESERCIZIO 7
        # Task: rendere l'età di tipo float 
        
        df['Age'] = df['Age'].astype(float)

        # Studia il dataframe - Fase post        
        # ESERCIZIO 8 
        # Task: stampa i tipi del df e le colonne Age' ,'Fare', 'preferred_deck', 'dining_time', 'activity', 'Sex' 
        #       delle prime 10 ed ultime 5 righe, Cosa è cambiato rispetto all'output dell'ESERCIZIO 1?         

        print(df.dtypes)

        cols = ['Age', 'Fare', 'preferred_deck', 'dining_time', 'activity', 'Sex']

        print(df[cols].head(10))
        print(df[cols].tail(5))

        return df
    
    def visualize(self, df: pd.DataFrame) -> None:
        """Crea e salva visualizzazioni"""
        # QUI INSERIAMO LE VISUALIZZAZIONI CON MATPLOTLIB E SEABORN
        counts_deck = df['preferred_deck'].value_counts()
        ax = counts_deck.plot(
            kind='pie',
            autopct='%1.1f%%',
            startangle=90,
            title="Distribuzione dei ponti preferiti"
        )
        ax.set_ylabel("")
        plt.tight_layout()
        plt.savefig("deck_distribution.png", dpi=150)
        plt.clf()
        
    def run_pipeline(self) -> pd.DataFrame:
        """Esegue la pipeline completa"""
        self.load_json()
        self.load_csv()
        print("Letti dati da più fonti (db, JSON)")
        # Preprocessa dati (aggrega, espande e pulisce)
        merged_df = self.merge_data()
        print("Aggregati dati da più fonti (db, JSON)")        
        expanded_df = self.expand_json_data(merged_df)
        print("Effettuata espansione dati (JSON -> nuove colonne)")        
        cleaned_df = self.clean_data(expanded_df)
        print("Effettuata pulizia dati")
        # Visualizza risultati
        # self.visualize(cleaned_df)
        # print("Visualizzati risultati di analisi")
        self.data = cleaned_df
        return cleaned_df
        
if __name__ == "__main__":
    pipe_jpath = "/home/banana/Desktop/Coding/Esercizi/IA/Lezione2/dati/titanic/titanic_prefs_small.json"
    pipe_csv_tuple = ("/home/banana/Desktop/Coding/Esercizi/IA/Lezione2/dati/titanic/passenger_info_small.csv", 
                      "/home/banana/Desktop/Coding/Esercizi/IA/Lezione2/dati/titanic/ticket_info_small.csv")

    pipeline = DataPipeline(pipe_jpath, pipe_csv_tuple)
    final_df = pipeline.run_pipeline()
    pipeline.visualize(final_df)
    print("Pipeline (esrcz) completata con successo!")
    # print(final_df.head())