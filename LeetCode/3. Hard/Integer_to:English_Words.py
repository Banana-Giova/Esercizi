class Solution:
    def numberToWords(self, num: int) -> str:
        #The input will be smaller than 2*31-1 (IE: 2 billion)
        zero_to_nine:dict[int, str] = {0: "", 1:"One", 2:"Two", 3:"Three", 
                                       4:"Four", 5:"Five", 6:"Six", 
                                       7:"Seven", 8:"Eight", 9:"Nine"}

        ten_nineteen:dict[int, str] = {10:"Ten", 11:"Eleven", 12:"Twelve",
                                    13:"Thirteen", 14:"Fourteen",
                                    15:"Fifteen", 16:f"{zero_to_nine[6]}teen",
                                    17:f"{zero_to_nine[7]}teen",
                                    18:f"{zero_to_nine[8]}een",
                                    19:f"{zero_to_nine[9]}teen"}
        
        twenty_ninety:dict[int, str] = {2:"Twenty", 3:"Thirty", 4:"Forty",
                                        5:"Fifty", 6:"Sixty", 7:"Seventy",
                                        8:"Eighty", 9:"Ninety"}
        
        piotta:dict[int, str] = {"H": "Hundred", "K": "Thousand",
                                 "M":"Million", "B":"Billion"}
        
        output:str = ''
        num_to_str:str = str(num)

        if len(num_to_str) == 10:
            output = zero_to_nine[int(num_to_str[0])] + " " + piotta["B"] + " "
            num_to_str = num_to_str[1:]

        if len(num_to_str) == 9:
            output += zero_to_nine[int(num_to_str[0])] + " " + piotta["H"] + " "
            num_to_str = num_to_str[1:]

        if len(num_to_str) == 8:
            if int(num_to_str[0:2]) in ten_nineteen:
                output += ten_nineteen[int(num_to_str[0:2])]\
                        + " " + piotta["M"] + " "
            else:
                output += (twenty_ninety[int(num_to_str[0])]\
                        + " " + zero_to_nine[int(num_to_str[1])])\
                        + " " + piotta["M"] + " "
            num_to_str = num_to_str[2:]

        if len(num_to_str) == 7:
            output += zero_to_nine[int(num_to_str[0])] + " " + piotta["M"] + " "
            num_to_str = num_to_str[1:]

        if len(num_to_str) == 6:
            output += zero_to_nine[int(num_to_str[0])] + " " + piotta["H"] + " "
            num_to_str = num_to_str[1:]

        if len(num_to_str) == 5:
            if int(num_to_str[0:2]) in ten_nineteen:
                output += ten_nineteen[int(num_to_str[0:2])]\
                        + " " + piotta["K"] + " "
            else:
                output += (twenty_ninety[int(num_to_str[0])]\
                        + " " + zero_to_nine[int(num_to_str[1])])\
                        + " " + piotta["K"] + " "
            num_to_str = num_to_str[2:]

        if len(num_to_str) == 4:
            output += zero_to_nine[int(num_to_str[0])] + " " + piotta["K"] + " "
            num_to_str = num_to_str[1:]

        if len(num_to_str) == 3:
            output += zero_to_nine[int(num_to_str[0])] + " " + piotta["H"] + " "
            num_to_str = num_to_str[1:]

        if len(num_to_str) == 2:
            if int(num_to_str) in ten_nineteen:
                output += ten_nineteen[int(num_to_str)]
            else:
                output += (twenty_ninety[int(num_to_str[0])]\
                        + " " + zero_to_nine[int(num_to_str[1])])
                
        if len(num_to_str) == 1:
            if num_to_str != "0":
                output = zero_to_nine[int(num_to_str)]
            else:
                output = "Zero"

        output = output.strip()
        return output
    
solution:Solution = Solution()
print(solution.numberToWords(401))