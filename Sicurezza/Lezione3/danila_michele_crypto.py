"""
(Step 0)
Prima di iniziare è bene creare un ambiente virtuale nel quale
scaricare "pycryptodome" con "pip". Una volta scaricato, nel
proprio file vanno importate i seguenti moduli, in quanto ci
torneranno utili dopo:
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

"""
(Step 1)

Per generare le chiavi è necessario eseguire il seguente codice:
"""

key_pair = RSA.generate(2048)
print(key_pair.export_key())
public_key = key_pair.publickey()
print(public_key.export_key())
exit(0)

"""
Dopo avere eseguito il codice sopracitato, le chiavi stampate nel
terminale vanno copiate ed inserite in delle variabili, una per la
chiave pubblica ed una per la chiave privata:
"""

sPubGio = '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA+5DK4EtTk8w6N9zOkh4R\ncM21b2VCc3p6hQ3G1m8aFNssI3v5w6BbtBTj7HWcXGkA0Zxd/1Xxoeux4M/255WR\nYuGsxDmDmyWdJbZbleweMe69trW/NUZym5eIZo5GS6N/FmLDUO3SfZRCucZ9XzGL\nKWUtHNtUvGhsavxoLCKa20Z49AzUG/WaA3u0R/nT2KThhRNlVTrOs96ETU38OV8r\nmC+cVn4FCZCfD6nyXCY+65wNHp4MNW3Y/al5NdiYWt6Qt8dy9upzjOlDUJXGVRhl\nqkez/H67/u/AUclGWlCFz1xaymwQJbFUi1pDmyUI88qsSxXFjms+7nxrP9PcEtLL\n5wIDAQAB\n-----END PUBLIC KEY-----'
sPrivGio = '-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA+5DK4EtTk8w6N9zOkh4RcM21b2VCc3p6hQ3G1m8aFNssI3v5\nw6BbtBTj7HWcXGkA0Zxd/1Xxoeux4M/255WRYuGsxDmDmyWdJbZbleweMe69trW/\nNUZym5eIZo5GS6N/FmLDUO3SfZRCucZ9XzGLKWUtHNtUvGhsavxoLCKa20Z49AzU\nG/WaA3u0R/nT2KThhRNlVTrOs96ETU38OV8rmC+cVn4FCZCfD6nyXCY+65wNHp4M\nNW3Y/al5NdiYWt6Qt8dy9upzjOlDUJXGVRhlqkez/H67/u/AUclGWlCFz1xaymwQ\nJbFUi1pDmyUI88qsSxXFjms+7nxrP9PcEtLL5wIDAQABAoIBAAbsTvrYYHZAdcSf\nkKoUYYa5FZ4gw/++Q7j9v33qPkiy4gj3zkaRr8RicqN6neJneTZ8xc7YNE2Sz3L1\nNjK1mGBCnNLCFawSGm1hdPJ6BRC2B0+zWA3ztECUT+M8y1lz7SWMX7hdLGCWR12C\nxWS7dVoVBHUoa+yGESnC4my5v4kFBcamw/UGQdUjiLJ2ObSEeRUfWWhfI7EpOjVR\njxNFUCChcFr3AA4REd9lJw2ntj+nM2W9sVBxBfN8VM4mJfazbStRfcg90mUQMwLK\n4z+oVDR6/q72I4sapSyVtxUvjfXsjWwwJLPleJkxFdOiP2OvNtaADhRlfZzuHBEc\nbMfjPgUCgYEA/ZxJEl2K4l6XaaNVgouKDqMzpfVJIjI6O5X6zJ5rGNVvqFuzTTEz\nUnXYa4Qw0ogc4nVCYfDm5PlV1rDRVRZOByKGlopJcO06F8eOC36pZaTNWS2iO2lJ\nvOMNQtf/P7DlbSjm6NLdyNG8pEiQef63oeBPFMS9lEc8in+z7WmndvUCgYEA/e+T\nIHxmkRmsQQN9oEihVgmxRM+UKLSAITN6rUCBFsJrFfMkY4Xx7LV4rI5WAs3o8Amh\nPZ7pWW6Pw+faRKM+TTJIKufxnOg9lIGzsKC97WqENQwYdHac/lQJwFSxB6yASm/E\nJZkmP58852Wnvo4dZi8I1vicxNjZDFVAG6TslesCgYEA04AF1IIcdCKMxXWIt4El\nloV2aj4ASrt2owC2EvU+vYwqPU6UXpjcgzVyUmAA02LeK+G8ha+A744cjxoQyZP7\naKnbcipLixjb7L7ocB+mp/TjqC6NcFyjORplkcxOu1AMVZfZ0msguPxpBNzbWFIb\n1K0bZmeY7tLl418Sr7kABw0CgYEA4mryUX36ahhtCY8WPYtlJ3T+9a7smRrQQEpJ\ncR9ZurRhjTG92Wt+GaR5U8qaEGgO8bB0b6A4yoAVegVKDfdMPsK9rFwhh9lfxwGa\n+btpfb6C4VXGnFmChBbklvQs4P3Dahub1jZm70WJpX1zgynuNsVraVpFVhNP/Hoq\n7jswpD8CgYBicu19FuhsbUmTokypgYs/dJemhy2p4cd4EaykGhPIrBnAvD59lH+K\nRm4mbgM428NeyW5FgxUT6Ypraqp42wCxP/IiYjMGN3NH8NO44JlElbDtv6onuGCc\npnJXUxh2wKx7F6r7soBkNO82RXSGXI6Tnl1PvNB41RSH8AGRS1A3nw==\n-----END RSA PRIVATE KEY-----'

"""
Infine le chiavi vanno trasposte in un oggetto di classe RSA derivante
dal modulo importato all'inizio "Crypto.PublicKey":
"""

key_pair = RSA.import_key(sPrivGio)
public_key = RSA.import_key(sPubGio)

"""
(Step 2)
Con il proprio collega va scambiata solo la propria chiave pubblica.
Il messaggio infatti viene criptato utilizzando solo la propria chiave
pubblica, dunque quando si decripta è necessario avere solo quella.
"""

"""
(Step 3)
Per cifrare un messaggio è necessario utilizzare la seguente funzione:
"""

# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")

"""
Questa funzione, prima la funzione 'new()' restituisce un oggetto
cifrato 'cipher' creato utilizzando la chiave pubblica del nostro collega,
in modo che possa decriptarla utilizzando appunto la chiave in suo possesso,
poi il messaggio viene cifrato utilizzando l'oggetto 'cipher' appena cfeato e
infine viene ritornato, in modo leggibile nell'encoding UTF-8.
"""

"""
(Step 4)
Per decifrare un messaggio proveniente da un collega è necessario
utilizzare la seguente funzione:
"""

# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")

"""
Questa funzione prima crea un altro oggetto 'cipher', ma questa volta
utilizzando la coppia di chiavi pubbliche e private nostre, dato che il
nostro collega ha encriptato il messaggio utiizzando la nostra chiave
pubblica, poi si fa il processo inverso rispetto a quello fatto prima,
decriptando il messaggio tramite l'appena creato 'cipher'.
"""

"""
Ecco dei codici esempio.
L'esercizio è stato eseguito con Michele Badimassoud e Danila Rahautsou.
"""

#Scambio messaggi con Danila
sPubDanila = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtPD3AuJx+It53p1IjvNp\n2UREYCzdrdjgYyvZ26c09siosd37kqE3XwnXvZ7xISI4hNYIdorwVs7q+xs+EKFr\nwPrAEj3GSKgBjkA/gesAnXaKzlf591rmrXzXq9YuKFngAO8vBZH+vuAq9fOsYBGj\ntbMiPQwXZBfgnshjT1zxDnqm3ER4GaDl1aMZ3+YkaI6DAZsuGTvUFyBFKWlssS+F\nQa21epOh3zpT67TdAcjwLHtnUgZHTVRoLxCT5Q+fG/x44UwXfpJhAywY1hVjlOQ3\nmEUvLx1/GBe8aEgoWmGe0s/X23Bqafheg2MqiEVk8+qUJschAXlWOSv7OIakLqm8\nQwIDAQAB\n-----END PUBLIC KEY-----"
public_danila = RSA.import_key(sPubDanila)

messaggio_per_danila = "Le banane banali?"
messaggio_da_danila = 'YJdyAOD7WJQG8uGQnwJpEeuk2LDiUXhnG9LG6co/pqLsSDWSUZ6IrduSPHlJKUQKUhR30rj+Pkj4n/IEWbWq9VVr8edy83DuFhs4kvJccDaMieuLAWO+Spqc/EFYBmdsDLJppxiIp5TZUHReca0LoRyJSZEImOJ8LGIiCgeuUzgKoTg0ZmbaVAmyLoIi3KKQWTRItPHm0zK8VVPqfeP/yghBkU//6mQaj8WgdXu/EOpFKX+nSzJ4DAOpBGFIzOy/s++XCLUhBIMjoCKfwWfoC3bhHqKzbYUkXFCS6Jb2w0i2eITsCPNHcRa9RVJqwFbSCxh8pXAOGNAMhxIYbVFgDA=='

print(encrypt_message(messaggio_per_danila, public_danila))
print(decrypt_message(messaggio_da_danila, key_pair))


#Scambio messaggi con Michele
sPubMichele = '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAydm2ZlX4IYe9Saq8wSr5\ncA5XBiwwQRJP9c3bV1DVEdRMnozVvtn9t6NloQv4wBou6nY08M2gkKzsfjzhDfbt\noR+MtsSJpl1tsd/S8p/isSGVjuiYOqllkDrvOu/YcwHHyCjd5vTmYM6mL+CPXzWE\nUV3QYb3yB6jwfbzU6YArJipwNJl6+Denqf72Il22le+xzghgs7+OIByvMZbI2R2i\nu+82Elx+SLpS4GFigpiu4bsvPNI0vWmtb8jvy9Dc0N1qUf/y5to7VbsEbSrdS2z2\nYlvPjKQc0ym8hGCNiHHTnGXegAr/k7Ti/cGMVsSiFRc6HMwawLFkRjTA4rebcntp\nqQIDAQAB\n-----END PUBLIC KEY-----'
public_michele = RSA.import_key(sPubMichele)

messaggio_per_michele = "Badasium a rapporto: hanno distrutto l'Albania"
messaggio_da_michele = 'hfYk2OUTHWtcyoQasxsnX3eojhBUf4okqlkL/J37bto4l8xy8aHlIf6iPiA9lojZmTZxmJ54V3Enu0pb13MYnLhnwwVtRulzkgHp2qoJrzXHOx4nVv4v+NXUIDZfRNGRpa/dAoEZEXfc8mqwxTwjWvr3Ya4cZ+3mAu88ERxj/VPmSaG4IqCEa1ql+5/LH0fVCop65f9K7aZoZ0RCDz3usizbz/cTl/yhTFK9X4J+/Ld8GC2DQ42XOWjopYFU9xmAOMQiSlIA98k7fEcFdjgsM+gCJFukrYPWoorIHZo9LKNAzZSAX2OVULxcaRmpP9sNkaxhQQWI1nxr9dJhJ1bKCA=='

print(encrypt_message(messaggio_per_michele, public_michele))
print(decrypt_message(messaggio_da_michele, key_pair))