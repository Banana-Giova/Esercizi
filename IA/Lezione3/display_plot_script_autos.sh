#!/bin/bash

# Passo 1: pulisci la cartella "Lezione3/visual/autos/" sull'host
rm -rf Lezione3/visual/autos/*.png

# Passo 2: Esegui il codice per le visualizzazioni nel container e genera immagini .png in "Lezione3/visual/autos/" sull'host
docker exec -it -w /home/Lezione3/codice/autos its_dev python autos_data_pipeline_complete.py

# Passo 3: Apri le immagini .png in "Lezione3/visual/autos/" sull'host
eog Lezione3/visual/autos/
# eog --slide-show Lezione3/visual/autos/