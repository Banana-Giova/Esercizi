Ecco un documento di ripasso con i metodi pandas più utili, organizzato in sezioni tematiche. Ogni voce include una breve descrizione e riferimenti per approfondire.

Nel complesso, i metodi fondamentali di pandas si suddividono in:

* **Creazione e I/O**: lettura e scrittura di DataFrame/Series
* **Ispezione**: panoramica veloce del contenuto e della struttura
* **Selezione e indicizzazione**: accesso a righe e colonne
* **Filtri e slicing**: estrazione condizionale di sottoinsiemi
* **Raggruppamento e aggregazione**: sintesi di dati su gruppi
* **Merge e concatenazione**: unione di più DataFrame
* **Gestione dei valori mancanti**: rilevazione e imputazione
* **Ristrutturazione**: pivot, melt e trasformazioni di forma
* **Applicazione di funzioni**: map, apply, agg, transform
* **Data/time**: operazioni su indici temporali

## 1. Creazione e I/O

* `pd.read_csv()` / `pd.read_excel()` / `pd.read_json()` – caricano dati da file esterni ([W3Schools][1], [Real Python][2])
* `DataFrame(data)` / `Series(data)` – costruiscono oggetti pandas da dizionari, liste, arrays ([Real Python][3])
* `df.to_csv()` / `df.to_excel()` / `df.to_json()` – esportano DataFrame su file ([DataCamp][4])

## 2. Ispezione del DataFrame

* `df.head(n)` / `df.tail(n)` – prime/ultime n righe ([W3Schools][5], [DataCamp][4])
* `df.info()` – tipi di colonna e conteggio non-null ([Pandas][6])
* `df.describe()` – statistiche descrittive su colonne numeriche ([DataCamp][4])
* `df.dtypes`, `df.shape`, `df.columns`, `df.index` – dettagli su tipi, dimensioni ed etichette ([W3Schools][5], [W3Schools][7])

## 3. Selezione e indicizzazione

* `df['col']`, `df[['col1','col2']]` – selezione di una o più colonne ([W3Schools][1])
* `df.col` – shortcut se il nome è un identificatore Python valido ([Real Python][3])
* `df.loc[label]`, `df.loc[:, 'A':'C']` – selezione per etichetta (righe e colonne) ([Pandas][6])
* `df.iloc[pos]`, `df.iloc[:, 0:2]` – selezione per posizione integer ([Pandas][6])
* `df.at[label, col]`, `df.iat[pos_row, pos_col]` – accesso scalare super-veloce ([Pandas][6])

## 4. Filtri e slicing

* Condizioni booleane: `df[ df['A'] > x ]` ([Real Python][3])
* AND/OR: `df[(df['A']>x) & (df['B']==y)]` ([Real Python][3])
* `.query("A > @x and B == @y")` – sintassi stringa più leggibile ([Reddit][8])
* Slicing con `loc` / `iloc`: `df.iloc[0:3, 0:2]` ([Pandas][6])

## 5. Raggruppamento e aggregazione

* `df.groupby('col')` – crea un oggetto GroupBy ([Pandas][6])
* `.agg({'col1':'sum','col2':'mean'})` – aggregazioni multiple ([Pandas][6])
* `.transform()`, `.filter()`, `.apply()` – operazioni personalizzate su gruppi ([Pandas][6])

## 6. Merge, join e concatenazione

* `pd.concat([df1, df2], axis=0/1)` – concatenazione di DataFrame ([DataCamp][9])
* `pd.merge(df1, df2, on='key', how='inner/left/right/outer')` – join stile SQL ([DataCamp][9])
* `df.join(other_df, how='left')` – join basato sugli indici ([DataCamp][9])

## 7. Gestione dei valori mancanti

* `df.isnull()`, `df.notnull()` – maschere di NaN ([DataCamp][9])
* `df.dropna(axis=0/1, how='any/all')` – rimuove righe/colonne con NaN ([DataCamp][9])
* `df.fillna(value, method='ffill/bfill')` – imputazione ([DataCamp][9])

## 8. Ristrutturazione dei dati

* `df.pivot(index, columns, values)` – crea tabelle pivot ([W3Schools][1])
* `df.pivot_table(..., aggfunc)` – pivot con aggregazione ([W3Schools][1])
* `pd.melt(df, id_vars, value_vars)` – “scioglie” la tabella (long format) ([Pandas][10])
* `df.stack()`, `df.unstack()` – conversione tra livelli di MultiIndex ([Pandas][10])

## 9. Applicazione di funzioni

* `df.apply(func, axis=0/1)` – applica a righe o colonne ([Pandas][6])
* `df.map()` / `series.map()` – mappatura elemento per elemento ([Pandas][6])
* `df.pipe(func)` – chaining più leggibile ([Pandas][6])
* `df.assign(new_col=lambda x: ...)` – creazione di nuove colonne in modalità funzionale ([Reddit][8])

## 10. Date/Time e categorie

* `pd.to_datetime()` – converte in datetime ([Pandas][11])
* `.dt` accessor: `.dt.year`, `.dt.month`, `.dt.weekday`, ecc. ([Pandas][11])
* `df.resample('M').agg(...)` – raggruppa per frequenza temporale ([Pandas][11])
* `df.astype('category')` – risparmia memoria su variabili categoriche ([Real Python][12])

--------------------

La scelta del tipo di grafico dipende soprattutto:

    Natura delle variabili

        Numeriche Continue (Age, Fare): mostrano distribuzioni e densità.

        Categoriche (preferred_deck, dining_time, activity, Sex): confrontano frequenze o proporzioni.

    Scopo dell’analisi

        Distribuzione di un’unica variabile → Istogramma, Boxplot.

        Confronto fra categorie → Bar-plot (valori assoluti o medi), Violin plot (distribuzioni per categoria).

        Relazione fra due variabili numeriche → Scatterplot, Hexbin.

        Composizione (che percentuale occupa ogni categoria) → Bar-stacked, Pie (con poche categorie).

        Evoluzione temporale → Line plot (se hai una variabile “time”).

    Numero di categorie/valori

        Se hai molte categorie (p.es. decine), evita il pie chart (diventa illeggibile) e preferisci un bar-plot orizzontale o un heatmap.

        Con poche categorie (meno di 6–7), un pie chart può andare, ma il bar-plot rimane più immediato da leggere.