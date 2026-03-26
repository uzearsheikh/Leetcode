class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        a = max(nums)
        res = nums.index(a)
        return res
        