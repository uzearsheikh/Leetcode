class Solution:
    def rec(self,i,j,m,n,dp):
        if i == m-1 and j == n-1:
            return 1
        # Grid ke bahar chale gaye
        if i >= m or j >= n:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        up = self.rec(i+1,j,m,n,dp)
        down = self.rec(i,j+1,m,n,dp)
        dp[i][j] = up+down
        return dp[i][j]
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*(n+1) for _ in range(m+1)]
        return self.rec(0,0,m,n,dp)
        
        