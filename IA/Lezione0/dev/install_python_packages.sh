#!/bin/bash

# NOTA: Anche qui sotto sostituire con il proprio path per il progetto!
if [ -f "/home/user/Scrivania/VSCodeProjects/Esercizi/IA/Lezione0/test/python_requirements.txt" ]; then
    pip install --no-cache-dir -r /home/user/Scrivania/VSCodeProjects/Esercizi/IA/Lezione0/test/python_requirements.txt
fi

apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*