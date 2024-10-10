from cryptography.fernet import Fernet
import os
import subprocess

en_key = Fernet.generate_key()
de_key = str(en_key)[2:-1]

with open("key.txt", 'w') as f:
    f.write(de_key)