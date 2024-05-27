class Solution:
    def toHex(self, num: int) -> str:
        hexadecimal:str = ""
        
        binary:str = ""

        hex_conv:dict = {0: 0,
                        1: 1,
                        2: 2,
                        3: 3,
                        4: 4,
                        5: 5,
                        6: 6,
                        7: 7,
                        8: 8,
                        9: 9,
                        10: "a",
                        11: "b",
                        12: "c",
                        13: "d",
                        14: "e",
                        15: "f",
                        16: 10}

        if num < 0:
            num += 2**32
        
        while num > 16:
            remaind:int = num % 16
            hex_note:str = str(hex_conv[remaind])
            hexadecimal = hex_note + hexadecimal
            num //= 16
        num = str(hex_conv[num])
        hexadecimal = num + hexadecimal
            
        return hexadecimal