class Solution:
    def rec(self,i,amount,coins , dp):
        if amount == 0:
            return 1
        if i == len(coins):
            return 0
        if dp[i][amount]!=-1:
            return dp[i][amount]
        
        take = 0
        if coins[i] <= amount:
            take = self.rec(i, amount - coins[i], coins , dp)
        
        not_take = self.rec(i+1,amount,coins , dp)

        dp[i][amount] = take + not_take
        return dp[i][amount]

    def change(self, amount: int, coins: list[int]) -> int:
        dp = [[-1] * (amount+1) for _ in range(len(coins))]
        return self.rec(0, amount, coins,dp)
    