from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# Per iniziare generiamo una coppia di chiavi e le stampiamo
# Generating RSA Key Pair
# Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
#sProfPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAn1Q4/NisrrEa/Su+tTERKnsTelXHanenIe8nYbudpY9ymyXJ\n5SZDLVivQZ8Ml0g0ivNQ134ZzqGkMt8COK5odoworlmpDFCU+w5HmOlyy91/NPJ1\nLFSUV2B4GJhCBcGeK4VtKhimpDdWLiuo9E3I+GF7QAOFvt+4lCY1xycUHkzrVXuI\nLKOjYahZf0hPs6CeoySeVKvhIhb1u4yJLlbQgeQUyOs420rgHiUf+OxJ5n+KKWZe\n9NmwyHro37P631BCJtZM/Iov8im9/y9TWraFZP59QOUbjcUokv0YOK8b31MkNeA/\nt9LPQg2lTpaCTpbwJ1NmYA2uWD+WGCJm3AemgQIDAQABAoIBAA7SsJyWx0tXWcny\nVG3vWzKnEahWK6p+6EiIGJNcokLhZh8DXysCVMn2ur4G/zkMiYA149sF4H5wsQyJ\n4onbHAfkwUd7OvbU1mTHBCfjQYAFouHjqWgO6bV5WaL8I1moFOrlS8MuA5mP4Q+E\nQKs97gkW/0xKJ5rFnfABNWFKWZz56FpD7/zBTmgy2wtHMJYUmt2BskO86pFgeEw8\nmW6d/GNtX0Y2N7OENcDd8vGcJg91ZGx3D8YXVk+fCZXEVxFarQPuNx9xwCRATo1D\niek2yumuVVL1chyCIxXzDV+yBCOgAJM5OYj0C1VnU4EVvViXg44QOjC+wQYB4tEa\nx2auf+MCgYEAvPvPFuY4D9SEqcmUR9NsYr/EOgs7YTsTpGPyGbsHTFZmicIF/Obh\n0iIut3k7A5pg/lnLuyPKQBD6xsNZNsyY67oz4mMBfrPBxIsZZMhmDQNgyL67YI0h\ntUxIZyhT437FrXFbnXf9udEp0WoOtxbdwIinefrK/4OS4o3lPFo1eRsCgYEA19RT\nW2fpzXjHYBjsCix4zO8BF20LKKml1YAuRT6kR72bczzpZQA7vVhzZYd9uo+hAsPr\nGrsIm4m6NMoAMYnO6V+Wfzcr4IqvJnI9z9yUjaml3UPp0uGAfEPEmRmeeAl+g+gx\nuFyjj/enUlxELVc4JAOlD9q/pvC2J91VZ/hnFJMCgYAV8/ZphZLLm/dRNd5ovZGg\nowArcfSS5ebxOL796DD/2CWPKR/C8hsXauscWxPU5lEQGuREt/KdoJtRDY5GhFvb\nPkUarj+VNVJz/2iSwYjBSDws9aMUozBgPB1JBnFAQxC5hiqLT04FENwXvIc7E4fs\n/rLdw5ljNyiP8sXHTf9aMwKBgQCk9kFcDNlz1cu1lHbc887E/Cx+ZjbwNnJs89Lp\n1A4mUzK8aqMNMpd2imNxB5U+gccT4QESZkAW+bbb4EUzl9wRHaFezKF5tyZWIV1D\nQZo9iJwguWa/auIUmItsZVts7fzH/zH5cr0FLcmytpjZet+LD0obCxwPEc54O8Cq\nff7zhwKBgCteXoEnI7oOk50We0DlpzURvB90LbraqUF0xrSEsDNLonTEwcffdssE\npglmYr8MTa7tbc/7jJhbYe4r2J5cDfiqgEYRGj5oKlHLo9MCEKdSD22JsXq/GzjJ\nwke5+Zl4vYARKmH1IfTI0Ofpghc3Z/NBfRqTGD4CmOVd1jwC6aA5\n-----END RSA PRIVATE KEY-----"
#sProfPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn1Q4/NisrrEa/Su+tTER\nKnsTelXHanenIe8nYbudpY9ymyXJ5SZDLVivQZ8Ml0g0ivNQ134ZzqGkMt8COK5o\ndoworlmpDFCU+w5HmOlyy91/NPJ1LFSUV2B4GJhCBcGeK4VtKhimpDdWLiuo9E3I\n+GF7QAOFvt+4lCY1xycUHkzrVXuILKOjYahZf0hPs6CeoySeVKvhIhb1u4yJLlbQ\ngeQUyOs420rgHiUf+OxJ5n+KKWZe9NmwyHro37P631BCJtZM/Iov8im9/y9TWraF\nZP59QOUbjcUokv0YOK8b31MkNeA/t9LPQg2lTpaCTpbwJ1NmYA2uWD+WGCJm3Aem\ngQIDAQAB\n-----END PUBLIC KEY-----"
sPub = '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA+5DK4EtTk8w6N9zOkh4R\ncM21b2VCc3p6hQ3G1m8aFNssI3v5w6BbtBTj7HWcXGkA0Zxd/1Xxoeux4M/255WR\nYuGsxDmDmyWdJbZbleweMe69trW/NUZym5eIZo5GS6N/FmLDUO3SfZRCucZ9XzGL\nKWUtHNtUvGhsavxoLCKa20Z49AzUG/WaA3u0R/nT2KThhRNlVTrOs96ETU38OV8r\nmC+cVn4FCZCfD6nyXCY+65wNHp4MNW3Y/al5NdiYWt6Qt8dy9upzjOlDUJXGVRhl\nqkez/H67/u/AUclGWlCFz1xaymwQJbFUi1pDmyUI88qsSxXFjms+7nxrP9PcEtLL\n5wIDAQAB\n-----END PUBLIC KEY-----'
sPriv = '-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA+5DK4EtTk8w6N9zOkh4RcM21b2VCc3p6hQ3G1m8aFNssI3v5\nw6BbtBTj7HWcXGkA0Zxd/1Xxoeux4M/255WRYuGsxDmDmyWdJbZbleweMe69trW/\nNUZym5eIZo5GS6N/FmLDUO3SfZRCucZ9XzGLKWUtHNtUvGhsavxoLCKa20Z49AzU\nG/WaA3u0R/nT2KThhRNlVTrOs96ETU38OV8rmC+cVn4FCZCfD6nyXCY+65wNHp4M\nNW3Y/al5NdiYWt6Qt8dy9upzjOlDUJXGVRhlqkez/H67/u/AUclGWlCFz1xaymwQ\nJbFUi1pDmyUI88qsSxXFjms+7nxrP9PcEtLL5wIDAQABAoIBAAbsTvrYYHZAdcSf\nkKoUYYa5FZ4gw/++Q7j9v33qPkiy4gj3zkaRr8RicqN6neJneTZ8xc7YNE2Sz3L1\nNjK1mGBCnNLCFawSGm1hdPJ6BRC2B0+zWA3ztECUT+M8y1lz7SWMX7hdLGCWR12C\nxWS7dVoVBHUoa+yGESnC4my5v4kFBcamw/UGQdUjiLJ2ObSEeRUfWWhfI7EpOjVR\njxNFUCChcFr3AA4REd9lJw2ntj+nM2W9sVBxBfN8VM4mJfazbStRfcg90mUQMwLK\n4z+oVDR6/q72I4sapSyVtxUvjfXsjWwwJLPleJkxFdOiP2OvNtaADhRlfZzuHBEc\nbMfjPgUCgYEA/ZxJEl2K4l6XaaNVgouKDqMzpfVJIjI6O5X6zJ5rGNVvqFuzTTEz\nUnXYa4Qw0ogc4nVCYfDm5PlV1rDRVRZOByKGlopJcO06F8eOC36pZaTNWS2iO2lJ\nvOMNQtf/P7DlbSjm6NLdyNG8pEiQef63oeBPFMS9lEc8in+z7WmndvUCgYEA/e+T\nIHxmkRmsQQN9oEihVgmxRM+UKLSAITN6rUCBFsJrFfMkY4Xx7LV4rI5WAs3o8Amh\nPZ7pWW6Pw+faRKM+TTJIKufxnOg9lIGzsKC97WqENQwYdHac/lQJwFSxB6yASm/E\nJZkmP58852Wnvo4dZi8I1vicxNjZDFVAG6TslesCgYEA04AF1IIcdCKMxXWIt4El\nloV2aj4ASrt2owC2EvU+vYwqPU6UXpjcgzVyUmAA02LeK+G8ha+A744cjxoQyZP7\naKnbcipLixjb7L7ocB+mp/TjqC6NcFyjORplkcxOu1AMVZfZ0msguPxpBNzbWFIb\n1K0bZmeY7tLl418Sr7kABw0CgYEA4mryUX36ahhtCY8WPYtlJ3T+9a7smRrQQEpJ\ncR9ZurRhjTG92Wt+GaR5U8qaEGgO8bB0b6A4yoAVegVKDfdMPsK9rFwhh9lfxwGa\n+btpfb6C4VXGnFmChBbklvQs4P3Dahub1jZm70WJpX1zgynuNsVraVpFVhNP/Hoq\n7jswpD8CgYBicu19FuhsbUmTokypgYs/dJemhy2p4cd4EaykGhPIrBnAvD59lH+K\nRm4mbgM428NeyW5FgxUT6Ypraqp42wCxP/IiYjMGN3NH8NO44JlElbDtv6onuGCc\npnJXUxh2wKx7F6r7soBkNO82RXSGXI6Tnl1PvNB41RSH8AGRS1A3nw==\n-----END RSA PRIVATE KEY-----'
# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")

# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
message = "This is a secret message"
encrypted_message = encrypt_message(message, public_key)
decrypted_message = decrypt_message(encrypted_message, key_pair)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)