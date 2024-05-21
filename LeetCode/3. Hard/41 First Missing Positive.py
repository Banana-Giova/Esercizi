class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        max_num:int = max(nums)
        nums = list(set(nums))
        nums.sort()
        neums:list[int] = []
        for i in nums:
            if i > 0:
                neums.append(i)
        if max_num > 0:
            for i in range(max_num):
                if i+1 != neums[i]:
                    return i+1
            return max_num+1
        else:
            return 1
        
solution:Solution = Solution()
print(solution.firstMissingPositive([1,2,0]))