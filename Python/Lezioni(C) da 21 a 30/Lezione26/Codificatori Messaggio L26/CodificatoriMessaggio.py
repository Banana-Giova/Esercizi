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
                        i:str = chr(ord(i)+1)
                    else:
                        i = az[i]
                output += i
            else:
                output += i\
                
        return output

    def decodifica(self, cipher_to_str: str):
        za:dict[str, str] = {'a':'z', 'A':'Z'}
        ciph_list:list[str] = list(cipher_to_str)
        output:str = ''
        for i in ciph_list[:]:
            if i.isalpha():
                for j in range(self.key):
                    if i not in za:
                        i:str = chr(ord(i)-1)
                    else:
                        i = za[i]
                output += i
            else:
                output += i
                
        return output
    
    def leggiDaFile(self, path:str) -> str:
        with open(path, 'r') as reader:
            self.current_text = reader.read()
        
        return self.current_text
    
    def codificaSuFile(self, path:str) -> None:
        self.leggiDaFile(path=path)
        with open(path, 'w') as file:
            encoded = self.codifica(self.current_text)
            file.write(encoded)
            
    def decodificaSuFile(self, path:str) -> None:
        self.leggiDaFile(path=path)
        with open(path, 'w') as file:
            encoded = self.decodifica(self.current_text)
            file.write(encoded)


class CifrarioACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, key:int) -> None:
        super().__init__()
        self.key = key

    def codifica(self, str_to_cipher:str):
        output:str = ''
        stren:int = len(str_to_cipher)
        halved:int = stren//2

        for times in range(self.key):
            if stren%2 == 0:
                for i in range(halved):
                    output += str_to_cipher[i]
                    output += str_to_cipher[i+halved]
            if stren%2 != 0:
                for i in range(halved):
                    output += str_to_cipher[i]
                    output += str_to_cipher[i+(halved+1)]
                output += str_to_cipher[halved]
            str_to_cipher = output
            output = ''

        return str_to_cipher
    
    def decodifica(self, cipher_to_str: str):
        output:str = ''
        lastput:str = ''
        stren:int = len(cipher_to_str)

        for times in range(self.key):
            for i in range(stren):
                if i%2 == 0:
                    output += cipher_to_str[i]
                else:
                    lastput += cipher_to_str[i]
            cipher_to_str = output+lastput
            output = ''
            lastput = ''

        return cipher_to_str
    
    def leggiDaFile(self, path:str) -> str:
        with open(path, 'r') as reader:
            self.current_text = reader.read()
        
        return self.current_text
    
    def codificaSuFile(self, path:str) -> None:
        self.leggiDaFile(path=path)
        with open(path, 'w') as file:
            encoded = self.codifica(self.current_text)
            file.write(encoded)

    def decodificaSuFile(self, path:str) -> None:
        self.leggiDaFile(path=path)
        with open(path, 'w') as file:
            encoded = self.decodifica(self.current_text)
            file.write(encoded)