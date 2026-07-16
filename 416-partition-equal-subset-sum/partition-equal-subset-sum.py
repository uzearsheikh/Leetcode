class Solution:

    def rec(self, i, nums, tot, dp,target):

        

        if tot == target:
            return True

        if tot > target:
            return False

        if i == len(nums):
            return False

        if dp[i][tot] != -1:
            return dp[i][tot]

        take = self.rec(i + 1, nums, tot + nums[i], dp, target)

        not_take = self.rec(i + 1, nums, tot, dp, target)

        dp[i][tot] = take or not_take

        return dp[i][tot]

    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = [[-1] * (target + 1) for _ in range(len(nums) + 1)]

        return self.rec(0, nums, 0, dp, target)