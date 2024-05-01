"""
9. Caesar Cipher Encryption/Decryption:

    Create functions for encrypting and decrypting a message using the Caesar cipher.
    Allow the user to specify the shift value (number of positions to shift each letter).
    Handle both encryption and decryption using the same function with appropriate adjustments.
    Encrypt and decrypt the given message using the specified shift value.
"""

import sys
sys.path.append('/home/banana/Desktop/Coding/Esercizi')
from Personal_Collection import int_inputter

def caesar_cipher(str_to_cipher:str) -> str:
    print("""Welcome to the Caesar Cipher Encrypter!
Input the shift value of your cipher!""")
    shift_value:int = int_inputter()
    while True:
        choice:str = (input("""Great! Do you want to encrypt or decrypt?
Type 'Encrypt' or 'Decrypt' -> """)).casefold()
        if choice == "encrypt":
            print("Encryption loading...")
            break
        elif choice == "decrypt":
            print("Decryption loading...")
            break
        else:
            print("Invalid choice, type 'Encrypt' or 'Decrypt'.")

    low_alphabet:list = list(map(chr, range(ord('a'), ord('z')+1)))
    upp_alphabet:list = []
    for i in low_alphabet:
        upp_alphabet.append(i.capitalize())
    numbers_list:list[int] = [i + 1 for i in range(26)]
    low_alpha_dict:dict = dict(zip(low_alphabet, numbers_list))
    upp_alpha_dict:dict = dict(zip(upp_alphabet, numbers_list))
    
    list_to_cipher:list[str] = list(str_to_cipher)
    ciphered_list:list = []

    while True:
        if choice == "encrypt":
            for i in list_to_cipher:
                low_char:bool = False
                upp_char:bool = False
                if i in low_alphabet\
                or i in upp_alphabet:
                    counter:int = shift_value
                    if i in low_alphabet:
                        i = low_alpha_dict[i]
                        low_char = True
                    else:
                        i = upp_alpha_dict[i]
                        upp_char = True

                    while counter > 0:
                        if i != 26:
                            i += 1
                            counter -=1
                        else:
                            i = 1
                            counter -= 1
                    
                    if low_char == True:
                        for ki, vi in low_alpha_dict.items():
                            if i == vi:
                                i = ki
                                ciphered_list.append(i)
                    if upp_char == True:
                        for ki, vi in upp_alpha_dict.items():
                            if i == vi:
                                i = ki
                                ciphered_list.append(i)
                else:
                    ciphered_list.append(i)
            
            ciphered_str:str = ""
            for i in ciphered_list:
                ciphered_str += i

            return ciphered_str

        elif choice == "decrypt":
            for i in list_to_cipher:
                low_char:bool = False
                upp_char:bool = False
                if i in low_alphabet\
                or i in upp_alphabet:
                    counter:int = shift_value
                    if i in low_alphabet:
                        i = low_alpha_dict[i]
                        low_char = True
                    else:
                        i = upp_alpha_dict[i]
                        upp_char = True

                    while counter > 0:
                        if i != 1:
                            i -= 1
                            counter -=1
                        else:
                            i = 26
                            counter -= 1
                    
                    if low_char == True:
                        for ki, vi in low_alpha_dict.items():
                            if i == vi:
                                i = ki
                                ciphered_list.append(i)
                    if upp_char == True:
                        for ki, vi in upp_alpha_dict.items():
                            if i == vi:
                                i = ki
                                ciphered_list.append(i)
                else:
                    ciphered_list.append(i)
            
            ciphered_str:str = ""
            for i in ciphered_list:
                ciphered_str += i

            return ciphered_str

        else:
            print("Error, invalid input.")

    

print(caesar_cipher("Signori, buonasera"))