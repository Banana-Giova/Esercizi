"""class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        output:int = 0
        for n1 in nums:
            output += n1
        for n2 in range(len(nums)):
            for n3 in nums:
                if nums[n2] != n3:
                    temp_list:list = []
                    output += nums[n2] + n3
                    temp_list.append(n3)
                    


        return output
    
solution:Solution = Solution()
solution.subsetXORSum(nums = [5,1,6])"""

#Unfinished because boring