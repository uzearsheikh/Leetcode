class Solution:

    def rec(self, i, state, prices,dp):

        # Saare days khatam
        if i >= len(prices):
            return 0
        if dp[i][state] != -1:
            return dp[i][state]
        # State = 0 → stock nahi hai
        if state == 0:

            # Buy karo
            buy = -prices[i] + self.rec(i + 1, 1, prices,dp)

            # Buy nahi karo
            skip = self.rec(i + 1, 0, prices,dp)

            dp[i][state] = max(buy, skip)
            return dp[i][state]

        # State = 1 → stock hai
        else:

            # Stock ko hold karo
            hold = self.rec(i + 1, 1, prices,dp)

            # Stock sell karo
            # i+2 because next day cooldown
            sell = prices[i] + self.rec(i + 2, 0, prices,dp)
            dp[i][state] = max(sell,hold)
            return dp[i][state]

    def maxProfit(self, prices):
        dp = [[-1] * 2 for _ in range(len(prices))]

        return self.rec(0, 0, prices,dp)