#!/bin/bash

# Passo 1: pulisci la cartella "Lezione3/visual/retail/" sull'host
rm -rf Lezione3/visual/retail/*.png

# Passo 2: Esegui il codice per le visualizzazioni nel container e genera immagini .png in "Lezione3/visual/retail/" sull'host
docker exec -it -w /home/Lezione3/codice/retail its_dev python retail_data_pipeline.py

# Passo 3: Apri le immagini .png in "Lezione3/visual/retail/" sull'host
eog Lezione3/visual/retail/
# eog --slide-show Lezione3/visual/retail/