#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 17:28:35 2025

@author: stefano
"""

import pandas as pd
import statistics

import os
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the data file
data_path = os.path.join(script_dir, '../dati/SomeMusicAlbums.csv')
df = pd.read_csv(data_path)

#df = pd.read_csv("../dati/SomeMusicAlbums.csv")

## Esercizio 1: Carica il CSV in un DataFrame
## Task: Leggi i dati del file CSV fornito in un Pandas DataFrame e visualizza le prime 3 righe  
## Soluzione:
print("***ESERCIZIO 1***")

print(df.head(3))

print("*****************"+"\n")    
 
### Esercizio 2: Mostra informazioni di base sul DataFrame 
### Task: Mostra il numero di righe, colonne e tipi di dati per ogni colonna 
### Soluzione:
print("***ESERCIZIO 2***")

righe, colonne = df.shape
print(f"Num. di righe: {righe}\nNum. di colonne: {colonne}")
print(f"\nTipi di dati per colonna:\n{df.dtypes}")

print("*****************"+"\n")
 
### Esercizio 3: Filtra gli album per genere
### Task: Crea un nuovo DataFrame contenente solo gli album con "rock" nella colonna 'Genre'
### Soluzione:
print("***ESERCIZIO 3***")

album_rock = df[df['Genre'].str.contains('rock', case=False, na=False)]
print(album_rock)

print("*****************"+"\n")

## Esercizio 4: Trova gli album pubblicati dopo il 1980
## Task: Filtra gli album pubblicati dopo il 1980 e visualizza solo le colonne 'Artist', 'Album' e 'Released'
## Soluzione:
print("***ESERCIZIO 4***")

eighty_artbum = df[df['Released'] > 1980][['Artist', 'Album', 'Released']]
print(eighty_artbum)

print("*****************"+"\n")

### Esercizio 5: Calcola la media delle valutazioni
### Task: Calcola la media della colonna 'Rating' per tutti gli album
### Soluzione:
print("***ESERCIZIO 5***")

print(df['Rating'].mean())

print("*****************"+"\n")

### Esercizio 6: Trova l'album più lungo e il più breve
### Task: Identifica l'album con la durata massima nella colonna 'Length' e visualizza i suoi dettagli
### Soluzione:
print("***ESERCIZIO 6***")

the_longest = df[df['Length'] == df['Length'].max()]
print(the_longest)

print("*****************"+"\n")
 
### Esercizio 7: Elenco generi unici
### Task: Estrai e stampa tutti i generi unici nel dataset (dividendo i generi combinati come "pop, rock")
### Soluzione:
print("***ESERCIZIO 7***")

raw_uniques:list = (df['Genre'].unique()).tolist()
uniques:list = []
for i in raw_uniques:
    for j in str(i).split(','):
        if j.strip() not in uniques:
            uniques.append(j.strip())

print(uniques)
print("*****************"+"\n")

### Esercizio 8: Confronta le vendite con vendite dichiarate
### Task: Aggiungi una nuova colonna 'Sales_Difference' che mostri la differenza tra 'Claimed Sales' e 'Music Recording Sales'
### Soluzione:
print("***ESERCIZIO 8***")

df['Sales_Difference'] = df['Claimed Sales (millions)'] - df['Music Recording Sales (millions)']
print(df)

print("*****************"+"\n")
  
### Esercizio 9: Trova gli album colonna sonora
### Task: Elenca tutti gli album contrassegnati come 'Soundtrack' (dove la colonna è "Y")
### Soluzione:
print("***ESERCIZIO 9***")

print(df[df['Soundtrack'] == 'Y'])

print("*****************"+"\n")

### Esercizio 10: Salva i dati filtrati in un file CSV
### Task: Salva tutti gli album con una valutazione (Rating) ≥ 9 in un nuovo file CSV
### Soluzione:
print("***ESERCIZIO 10***")

best_hits = df[df['Rating'] >= 9]
print(best_hits)
best_hits.to_csv('csv/best_hits.csv', index=False)

print("******************"+"\n")
  
### Esercizio 11: Conta gli album per genere
### Task:Conta quanti album appartengono a ogni genere unico (dividendo generi combinati come "pop, rock")
### Soluzione:  
print("***ESERCIZIO 11***")

raw_uniques2:list = (df['Genre'].unique()).tolist()
uniques2:dict = {}
for i in raw_uniques2:
    for j in str(i).split(','):
        if j.strip() not in uniques2:
            uniques2[j.strip()] = 1
        else:
            uniques2[j.strip()] += 1

print(uniques2)
print("******************"+"\n")

### Esercizio 12: Trova l'album con la maggior differenza tra vendite e vendite dichiarate
### Task: Identifica l'album con la maggiore differenza tra 'Claimed Sales' e 'Music Recording Sales' e visualizza i suoi dettagli
### Soluzione:  
print("***ESERCIZIO 12***")

print(df[df['Sales_Difference'] == df['Sales_Difference'].max()])

print("******************"+"\n")
  
### Esercizio 13: Filtra gli album per generi multipli
### Task: Crea un nuovo DataFrame contenente gli album che includono entrambi "rock" e "pop" nella colonna 'Genre'
### Soluzione:**  
print("***ESERCIZIO 13***")

poprock = df[df['Genre'].str.contains('rock|pop', case=False, na=False)]
print(poprock)

print("******************"+"\n")
    
### Esercizio 14: Calcola la durata media per genere
### Task: Calcola la media della durata (in minuti) degli album per ogni genere (dividendo generi combinati)
### Soluzione:  
print("***ESERCIZIO 14***")

def length_to_num(length:str) -> int:
    h, m, s = map(int, length.split(':'))
    return (h*3600)+(m*60)+s

genres_length = df[['Genre', 'Length']]
genres_length['Pract_Length'] = df['Length'].apply(length_to_num)
raw_genre_avg:dict = {}

for index, row in genres_length.iterrows():
    for j in str(row['Genre']).split(','):
        if j.strip() not in raw_genre_avg:
            raw_genre_avg[j.strip()] = []
        raw_genre_avg[j.strip()].append(int(row["Pract_Length"]))

genre_avg = {}
for ki, vi in raw_genre_avg.items():
    genre_avg[ki] = statistics.mean(vi)

print(genre_avg)

print("******************"+"\n")

### Esercizio 15: Trova l'album più venduto che non è una colonna sonora
### Task: Identifica l'album con le maggiori 'Music Recording Sales' che non è una colonna sonora
### Soluzione:  
print("***ESERCIZIO 15***")

print(df[
    (df['Music Recording Sales (millions)'] == df['Music Recording Sales (millions)'].max()) 
  & (df['Soundtrack'] != 'Y')])

print("******************"+"\n")