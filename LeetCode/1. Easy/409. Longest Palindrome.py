class Solution:
    def longestPalindrome(self, s: str) -> int:
        output = 1
        s_to_list:list[str] = list(s)
        if reversed(s_to_list) == s_to_list:
            return len(s_to_list)
        else:
            palindict:dict[int, str] = {}
            for i in s_to_list:
                if i not in palindict:
                    palindict[i] = s_to_list.count(i)
            
            all_good:bool = True
            for ki, vi in palindict.items():
                if vi%2 == 0:
                    output += vi
                elif vi == 1:
                    all_good = False
                else:
                    all_good = False
                    if (vi-1)%2 == 0\
                    and vi-1 > 0:
                        output += vi-1


        if all_good == True:
            output -= 1

        return output