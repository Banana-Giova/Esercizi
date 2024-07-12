from abc import ABC
import abc

class CodificatoreMessaggio(ABC):
    
    def codifica(str_to_cipher:str):
        pass

class DecodificatoreMessaggio(ABC):
    
    def decodifica(cipher_to_str:str):
        pass



class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, key:int) -> None:
        super().__init__()
        self.key = key
    
    def codifica(self, str_to_cipher: str):
        az:dict[str, str] = {'z':'a', 'Z':'A'}
        str_list:list[str] = list(str_to_cipher)
        output:str = ''
        for i in str_list[:]:
            if i.isalpha():
                for j in range(self.key):
                    if i not in az:
                        curr:str = chr(ord(i)+1)
                    else:
                        curr = az[i]
                output += curr
            else:
                output += i
        return output

    def decodifica(self, cipher_to_str: str):
        za:dict[str, str] = {'a':'z', 'A':'Z'}
        ciph_list:list[str] = list(cipher_to_str)
        output:str = ''
        for i in ciph_list[:]:
            if i.isalpha():
                for j in range(self.key):
                    if i not in za:
                        curr:str = chr(ord(i)-1)
                    else:
                        curr = za[i]
                output += curr
            else:
                output += i
        return output



class CifrarioACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, key:int) -> None:
        super().__init__()
        self.key = key

    def codifica(self, str_to_cipher:str):
        output:str = ''
        stren:int = len(str_to_cipher)
        halved:int = stren//2

        if stren%2 == 0:
            for i in range(halved):
                output += str_to_cipher[i]
                output += str_to_cipher[i+halved]
        if stren%2 != 0:
            for i in range(halved):
                output += str_to_cipher[i]
                output += str_to_cipher[i+(halved+1)]
            output += str_to_cipher[halved]

        return output