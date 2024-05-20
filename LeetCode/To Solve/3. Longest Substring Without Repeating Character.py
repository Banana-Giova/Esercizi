class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sling:list[str] = list(s)
        counter:int = 1
        max_count:int = 1
        blacklist:list = []
        last_blacked = ""

        for i in range(len(sling)):
            try:
                if sling[i] != sling[i+1]\
                and sling[i+1] not in blacklist:
                    counter += 1
                    blacklist.append(sling[i])
                    last_blacked = i
                else:
                    counter = 1
                    blacklist = []
            except IndexError:
                pass
            if counter > max_count:
                max_count = counter

        if s == "":
            return 0
        else:
            return max_count
        
solution:Solution = Solution()
print(solution.lengthOfLongestSubstring("anviaj"))  #should be 5