class Solution:
    def numberToWords(self, num: int) -> str:
        #The input will be smaller than 2*31-1 (IE: 2 billion)
        zero_to_nine:dict[int, str] = {0: "", 1:"One", 2:"Two", 3:"Three", 
                                       4:"Four", 5:"Five", 6:"Six", 
                                       7:"Seven", 8:"Eight", 9:"Nine"}

        ten_nineteen:dict[int, str] = {'00':'', '01':"One", '02':"Two", '03':"Three", 
                                       '04':"Four", '05':"Five", '06':"Six", 
                                       '07':"Seven", '08':"Eight", '09':"Nine", 
                                       '10':"Ten", '11':"Eleven", '12':"Twelve",
                                       '13':"Thirteen", '14':"Fourteen",
                                       '15':"Fifteen", '16':f"{zero_to_nine[6]}teen",
                                       '17':f"{zero_to_nine[7]}teen",
                                       '18':f"{zero_to_nine[8]}een",
                                       '19':f"{zero_to_nine[9]}teen"}
        
        twenty_ninety:dict[int, str] = {1: "Ten", 2:"Twenty", 3:"Thirty", 4:"Forty",
                                        5:"Fifty", 6:"Sixty", 7:"Seventy",
                                        8:"Eighty", 9:"Ninety"}
        
        karats:dict[str, str] = {"H": "Hundred", "K": "Thousand",
                                 "M":"Million", "B":"Billion"}
        
        output:str = ''
        num_to_str:str = str(num)

        if len(num_to_str) == 10:
            if int(num_to_str[1:]) == 0:
                output += zero_to_nine[int(num_to_str[0])]\
                        + " " + karats["B"]
            else:
                output = zero_to_nine[int(num_to_str[0])] + " " + karats["B"] + " "
                num_to_str = num_to_str[1:]

        if len(num_to_str) == 9:
            if num_to_str[0] != '0':
                if int(num_to_str[1:]) == 0:
                    output += zero_to_nine[int(num_to_str[0])]\
                            + " " + karats["H"] + " " + karats["M"]
                    return output
                else:
                    if int(num_to_str[1:3]) == 0:
                        output += zero_to_nine[int(num_to_str[0])]\
                                + " " + karats["H"] + " " + karats["M"] + " "
                    else:
                        output += zero_to_nine[int(num_to_str[0])] + " " + karats["H"] + " "

            num_to_str = num_to_str[1:]
        
        if len(num_to_str) == 8:
            if int(num_to_str[1:]) == 0:
                output += twenty_ninety[int(num_to_str[0])]\
                        + " " + karats["M"]
                return output
            else:
                if int(num_to_str[2:]) == 0:
                    if num_to_str[:2] in ten_nineteen:
                        output += ten_nineteen[num_to_str[0:2]]\
                            + " " + karats["M"]
                    else:
                        output += twenty_ninety[int(num_to_str[0])]\
                        + " " + zero_to_nine[int(num_to_str[1])] + " " + karats["M"]
                    return output 

                else:
                    if int(num_to_str[0:2]) == 0:
                        pass

                    else:
                        if num_to_str[0:2] in ten_nineteen:
                            output += ten_nineteen[num_to_str[0:2]]\
                                    + " " + karats["M"] + " "
                        else:
                            output += twenty_ninety[int(num_to_str[0])]\
                                    + " " + zero_to_nine[int(num_to_str[1])]
                            output = output.strip()
                            output += " " + karats["M"] + " "
                    num_to_str = num_to_str[2:]

        if len(num_to_str) == 7:
            if num_to_str[0] != '0':
                if int(num_to_str[1:]) == 0:
                    output += zero_to_nine[int(num_to_str[0])]\
                            + " " + karats["M"]
                    return output
                else:
                    output += zero_to_nine[int(num_to_str[0])] + " " + karats["M"] + " "
            num_to_str = num_to_str[1:]

        if len(num_to_str) == 6:
            if num_to_str[0] != '0':
                if int(num_to_str[1:]) == 0:
                    output += zero_to_nine[int(num_to_str[0])]\
                            + " " + karats["H"] + " " + karats["K"]
                    return output
                else:
                    if int(num_to_str[1:3]) == 0:
                        output += zero_to_nine[int(num_to_str[0])]\
                                + " " + karats["H"] + " " + karats["K"] + " "
                    else:
                        output += zero_to_nine[int(num_to_str[0])] + " " + karats["H"] + " "

            num_to_str = num_to_str[1:]
        
        if len(num_to_str) == 5:
            if int(num_to_str[1:]) == 0:
                output += twenty_ninety[int(num_to_str[0])]\
                        + " " + karats["K"]
                return output
            else:
                if int(num_to_str[2:]) == 0:
                    if num_to_str[:2] in ten_nineteen:
                        output += ten_nineteen[num_to_str[0:2]]\
                            + " " + karats["K"]
                    else:
                        output += twenty_ninety[int(num_to_str[0])]\
                        + " " + zero_to_nine[int(num_to_str[1])] + " " + karats["K"]
                    return output 

                else:
                    if int(num_to_str[0:2]) == 0:
                        pass

                    else:
                        if num_to_str[0:2] in ten_nineteen:
                            output += ten_nineteen[num_to_str[0:2]]\
                                    + " " + karats["K"] + " "
                        else:
                            output += twenty_ninety[int(num_to_str[0])]\
                                    + " " + zero_to_nine[int(num_to_str[1])]
                            output = output.strip()
                            output += " " + karats["K"] + " "
                    num_to_str = num_to_str[2:]

        if len(num_to_str) == 4:
            if int(num_to_str[1:]) == 0:
                output += zero_to_nine[int(num_to_str[0])]\
                        + " " + karats["K"]
            else:
                output += zero_to_nine[int(num_to_str[0])] + " " + karats["K"] + " "
                num_to_str = num_to_str[1:]

        if len(num_to_str) == 3:
            if num_to_str[0] != '0':
                if int(num_to_str[1:]) == 0:
                    output += zero_to_nine[int(num_to_str[0])]\
                            + " " + karats["H"]
                    return output
                else:
                    output += zero_to_nine[int(num_to_str[0])] + " " + karats["H"] + " "
            num_to_str = num_to_str[1:]

        if len(num_to_str) == 2:
            if num_to_str in ten_nineteen:
                output += ten_nineteen[num_to_str]
            else:
                output += twenty_ninety[int(num_to_str[0])]\
                        + " " + zero_to_nine[int(num_to_str[1])]
                
        if len(num_to_str) == 1:
            if num != 0:
                output = zero_to_nine[int(num_to_str)]
            else:
                output = "Zero"

        output = output.strip()
        return output
    
solution:Solution = Solution()

print(solution.numberToWords(3200348))