class Solution:
    def rec(self,i,j,s,t,dp):
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        
        if s[i]==t[j]:
            take = self.rec(i+1,j+1,s,t,dp)
            skip = self.rec(i+1,j,s,t,dp)
        else:
            return self.rec(i+1,j,s,t,dp)
        dp[i][j]=take+skip
        return dp[i][j]
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1]*(len(t)+1) for _ in range(len(s)+1)]
        return self.rec(0,0,s,t,dp)
        