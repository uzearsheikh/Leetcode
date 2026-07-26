class Solution:

    def rec(self, target, nums, dp):

        if target == 0:
            return 1

        if target < 0:
            return 0

        if dp[target] != -1:
            return dp[target]

        ans = 0

        for num in nums:
            ans += self.rec(target - num, nums, dp)

        dp[target] = ans
        return ans

    def combinationSum4(self, nums, target):

        dp = [-1] * (target + 1)

        return self.rec(target, nums, dp)