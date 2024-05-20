class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        max_num:int = max(nums)
        if max_num > 0:
            for i in range(1, max_num):
                if i not in nums:
                    return i
            return max_num + 1
        else:
            return 1