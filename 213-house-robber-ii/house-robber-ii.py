class Solution:

    def rec(self, i, nums, dp):

        if i >= len(nums):
            return 0

        if dp[i] != -1:
            return dp[i]

        take = nums[i] + self.rec(i + 2, nums, dp)

        not_take = self.rec(i + 1, nums, dp)

        dp[i] = max(take, not_take)

        return dp[i]

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        nums1 = nums[:-1]
        nums2 = nums[1:]

        dp1 = [-1] * len(nums1)
        dp2 = [-1] * len(nums2)

        case1 = self.rec(0, nums1, dp1)
        case2 = self.rec(0, nums2, dp2)

        return max(case1, case2)