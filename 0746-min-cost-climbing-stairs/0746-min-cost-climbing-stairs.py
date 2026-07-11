class Solution:

    def rec(self, i, cost, dp):

        # Base Case
        if i >= len(cost):
            return 0

        # Memoization Check
        if dp[i] != -1:
            return dp[i]

        # Recursive Calls
        one_step = self.rec(i + 1, cost, dp)
        two_step = self.rec(i + 2, cost, dp)

        # Store Answer
        dp[i] = cost[i] + min(one_step, two_step)

        return dp[i]

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # 1D DP
        dp = [-1] * len(cost)

        return min(
            self.rec(0, cost, dp),
            self.rec(1, cost, dp)
        )