class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        officer_balls:list = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        officer_balls.append(i)
                        officer_balls.append(j)
                        return officer_balls
                    
solution:Solution = Solution()

print(solution.twoSum([3,2,4], 6))