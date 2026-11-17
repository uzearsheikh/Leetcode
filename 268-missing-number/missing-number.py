class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s = set()
        n = len(nums)

        for i in range(n):
            s.add(nums[i])

        for i in range(n+1):
            if i not in s:
                return i