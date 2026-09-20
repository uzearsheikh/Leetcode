class Solution:

    def rec(self, i, nums, tot, dp,target):

        

        if tot == target:
            return True

        if tot > target:
            return False

        if i == len(nums):
            return False

        if dp[i][tot] is not None:
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

        dp = [[None] * (target + 1) for _ in range(len(nums) + 1)]

        return self.rec(0, nums, 0, dp, target)

        # yaha dp arraye me none islie liya hai qki ham baad me dp me true or false store krenge to none lena sahi rahega professional laegaga -1 bhi lenge to chalega but professinal nhi lagega