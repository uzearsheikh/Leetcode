class Solution:
    def rec(self, n,dp):
        if n == 0:
            return 0
        if dp[n]!=-1:
            return dp[n]

        ans = float('inf')

        i = 1

        while i * i <= n:
            square = i * i

            ans = min(ans, 1 + self.rec(n - square,dp))
            

            i += 1
        dp[n]=ans
        return dp[n]

    def numSquares(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.rec(n,dp)