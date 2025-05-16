#!/bin/bash

# Passo 1: pulisci la cartella "Lezione3/visual/titanic/" sull'host
rm -rf Lezione3/visual/titanic/*.png

# Passo 2: Esegui il codice per le visualizzazioni nel container e genera immagini .png in "Lezione3/visual/titanic/" sull'host
docker exec -it -w /home/Lezione3/codice/titanic its_dev python titanic_data_pipeline_complete.py

# Passo 3: Apri le immagini .png in "Lezione3/visual/titanic/" sull'host
eog Lezione3/visual/titanic/
# eog --slide-show Lezione3/visual/titanic/