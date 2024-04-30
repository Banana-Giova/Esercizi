"""
7. Roman Numeral Conversion:

    Create a function that converts a given integer to its Roman numeral representation.
    Handle numbers from 1 to 3999.
    Use a combination of string manipulation and conditional statements to build the Roman numeral.

    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
"""
import sys
sys.path.append('/home/banana/Desktop/Coding/Esercizi')
from Personal_Collection import int_inputter

def roman_numerals_converter() -> str:
    
    print("""Welcome to the Roman Numeral Conversion program!
Input the number that you want to convert into roman numerals!""")
    num_to_convert:int = int_inputter()

    roman_num:str = ""
    num_to_str:str = str(num_to_convert)
    
    nine_count = False
    ninety_count = False
    ninehundred_count = False

    if num_to_convert > 3999:
        return "Error, number too big. It has to be less than 3999."

    if num_to_str[-1] == "9":
            num_to_convert -= 9
            nine_count:bool = True
    if num_to_str[-2] == "9":
            num_to_convert -= 90
            ninety_count:bool = True
    if num_to_str[-3] == "9":
            num_to_convert -= 900
            ninehundred_count:bool = True


    while True:
        if num_to_convert >= 1000:
            num_to_convert -= 1000
            roman_num += "M"
            continue
        if ninehundred_count == True:
            roman_num += "CM"
            ninehundred_count = False
        if num_to_convert < 1000 \
        and num_to_convert >= 500:
            num_to_convert -= 500
            roman_num += "D"
            continue
        if num_to_convert < 500 \
        and num_to_convert >= 100:
            num_to_convert -= 100
            roman_num += "C"
            continue
        if ninety_count == True:
            roman_num += "XC"
            ninety_count = False
        if num_to_convert < 100 \
        and num_to_convert >= 50:
            num_to_convert -= 50
            roman_num += "L"
            continue
        if num_to_convert < 50 \
        and num_to_convert >= 10:
            num_to_convert -= 10
            roman_num += "X"
            continue
        if nine_count == True:
            roman_num += "IX"
            nine_count = False
        if num_to_convert < 10 \
        and num_to_convert >= 5:
            num_to_convert -= 5
            roman_num += "V"
            continue
        if num_to_convert < 5 \
        and num_to_convert >= 1:
            num_to_convert -= 1
            roman_num += "I"
            continue
        if num_to_convert == 0:
            break
    
    roman_num = roman_num.replace("CCCC", "CD")
    roman_num = roman_num.replace("XXXX", "XL")
    roman_num = roman_num.replace("IIII", "IV")
    
    return roman_num

print(roman_numerals_converter())