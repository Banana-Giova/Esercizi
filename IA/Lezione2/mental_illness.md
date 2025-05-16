Conda permette di creare ambienti con versioni specifiche di Python e librerie, anche se non sono installate globalmente.

    Installa Miniconda:
    bash

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

Crea un ambiente con Python 3.11:
bash

    conda create -n myenv python=3.11
    conda activate myenv
    pip install numpy==1.23.5 pandas==1.5.3 matplotlib==3.6.0