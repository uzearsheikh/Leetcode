class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = []
        for i in nums:
            if i!=0:
                arr.append(i)
        
        n = len(nums)
        k = len(arr)
        
        nums[:] = arr + [0] * (n - k)