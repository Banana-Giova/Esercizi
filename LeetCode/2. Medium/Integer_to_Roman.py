class Solution:
    def intToRoman(self, num: int) -> str:

        num_to_convert: int = num

        roman_num: str = ""
        num_to_str: str = str(num_to_convert)

        nine_count = False
        ninety_count = False
        ninehundred_count = False

        if num_to_str[-1] == "9":
            num_to_convert -= 9
            nine_count: bool = True
        try:
            if num_to_str[-2] == "9":
                num_to_convert -= 90
                ninety_count: bool = True
        except Exception:
            pass
        try:
            if num_to_str[-3] == "9":
                num_to_convert -= 900
                ninehundred_count: bool = True
        except Exception:
            pass

        while True:
            if num_to_convert >= 1000:
                num_to_convert -= 1000
                roman_num += "M"
                continue
            if ninehundred_count == True:
                roman_num += "CM"
                ninehundred_count = False
            if num_to_convert < 1000 and num_to_convert >= 500:
                num_to_convert -= 500
                roman_num += "D"
                continue
            if num_to_convert < 500 and num_to_convert >= 100:
                num_to_convert -= 100
                roman_num += "C"
                continue
            if ninety_count == True:
                roman_num += "XC"
                ninety_count = False
            if num_to_convert < 100 and num_to_convert >= 50:
                num_to_convert -= 50
                roman_num += "L"
                continue
            if num_to_convert < 50 and num_to_convert >= 10:
                num_to_convert -= 10
                roman_num += "X"
                continue
            if nine_count == True:
                roman_num += "IX"
                nine_count = False
            if num_to_convert < 10 and num_to_convert >= 5:
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
