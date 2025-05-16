Con i componenti dell'Ecosistema Docker per i corsi ITS ICT Academy correttamente installati ed attivi, eseguire le pipeline per gli esempi "autos", "titanic" e "retail" della Lezione 3 con i comandi:

docker exec -it -w /home/Lezione3/codice/autos its_dev python autos_data_pipeline_complete.py
docker exec -it -w /home/Lezione3/codice/titanic its_dev python titanic_data_pipeline_complete.py
docker exec -it -w /home/Lezione3/codice/retail its_dev python retail_data_pipeline_esrcz.py
docker exec -it -w /home/Lezione3/codice/retail its_dev python retail_data_pipeline.py

Se attivati i passi di visualizzazione dati nelle pipeline (i.e. funzione "visualize" nella classe "DataPipeline"), ed assumendo di dedicare al codice delle lezioni la directory per esempio /home/ITS_Academy/Lezioni_IA.1 sulla propria macchina Linux, le immagini generate in formato .png dalle pipeline per gli esempi "autos", "titanic" e "retail" della Lezione 3 si trovano rispettivamente nelle cartelle:

/home/ITS_Academy/Lezioni_IA.1/Lezione3/visual/autos/
/home/ITS_Academy/Lezioni_IA.1/Lezione3/visual/titanic/
/home/ITS_Academy/Lezioni_IA.1/Lezione3/visual/retail/

Esse potranno essere visualizzate con il programma di visualizzazione immagini preferito.

SCRIPT di shell: assumendo di utilizzare l'ambiente GNOME e di avere disponibile nell'ambiente il programma di visualizzazione immagini di default "Eye Of GNOME" (eog), è possibile automatizzare l'esecuzione delle pipeline e la visualizzazione delle eventuali immagini generate aprendo un terminale nella cartella dedicata alle lezioni, per esempio /home/ITS_Academy/Lezioni_IA.1/, ed eseguendo rispettivamente per "autos", "titanic" e "retail" i seguenti comandi:

Lezione3/display_plot_script_autos.sh
Lezione3/display_plot_script_titanic.sh
Lezione3/display_plot_script_retail.sh

Nota: assicurarsi di avere i permessi di esecuzione sui tre file di bash (in caso di necessità, eseguire dal terminale in /home/ITS_Academy/Lezioni_IA.1/ il comando "chmod +777 Lezione3/*.sh")   
