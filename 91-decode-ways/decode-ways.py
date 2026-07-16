class Solution:
    def rec(self,i,s,dp):
        if i == len(s):
            return 1
        if s[i]=="0":
            return 0 
        if dp[i]!=-1:
            return dp[i]
        one_step = self.rec(i+1,s,dp)
        two_step=0

        if i + 1 < len(s) and 10<=int(s[i:i+2])<=26:
            two_step = self.rec(i+2,s,dp)
        dp[i]= one_step +two_step
        
        return dp[i]


    def numDecodings(self, s: str) -> int:
        dp = [-1]*(len(s)+1)
        return self.rec(0,s,dp)
        