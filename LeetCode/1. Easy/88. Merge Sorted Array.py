class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while True:
            if nums1[-1] == 0\
            and len(nums1) != 1\
            and len(nums1) > m:
                nums1.pop(-1)
            elif len(nums1) == 1\
            and nums1[0] == 0:
                nums1.clear()
                break
            else:
                break
    
        nums1 += nums2
        nums1.sort()
    
        return nums1 